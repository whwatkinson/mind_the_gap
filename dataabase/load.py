from csv import DictReader

from neomodel import config, db

from models.station import Station
from models.tube_line_list import TubeLine, TubeLineList
from project_root import get_project_root
from settings.environment_variables import NEO4J_DATABASE_URL

config.DATABASE_URL = NEO4J_DATABASE_URL


def load_connections(tube_line: TubeLine) -> None:

    if tube_line.data_file_name == "master_station_names":
        return None

    print(f"Loading connections for {tube_line.line_name} line")

    with open(
        f"{get_project_root()}/data/connections/{tube_line.data_file_name}.csv",
        newline="\n",
    ) as csvfile:
        records = DictReader(csvfile, delimiter=",", quotechar='"')
        for row in records:

            res, _ = db.cypher_query(
                """
                MATCH (n:Station), (m:Station)
                WHERE $FROM IN n.tube_line_identifiers
                AND $TO IN m.tube_line_identifiers
                RETURN n, m;
                """,
                {"FROM": row["from_station"], "TO": row["to_station"]},
                resolve_objects=True,
            )
            if not res:
                raise Exception(f"No stations found for {row=}")

            from_station, to_station = res[0]
            print(
                f"\t Connecting {from_station.station_name} "
                f"to {to_station.station_name} "
                f"heading_west {row['heading_west']}"
            )
            if getattr(from_station, tube_line.data_file_name.lower()).is_connected(
                to_station
            ):
                continue

            getattr(from_station, tube_line.data_file_name.lower()).connect(
                to_station,
                {
                    "line_name": tube_line.line_name,
                    "line_colour": tube_line.line_colour,
                    "heading_west": row["heading_west"] == "True",
                    "travel_time_seconds": float(row["travel_time_seconds"]),
                    "distance_km": float(row["distance_km"]),
                },
            )
    print(f"Loaded connections for {tube_line.line_name} line")


def load_tube_stations(tube_line: TubeLine) -> None:

    print(f"Loading stations for {tube_line.line_name} line")

    with open(
        f"{get_project_root()}/data/stations/{tube_line.data_file_name}.csv",
        newline="\n",
    ) as csvfile:
        records = DictReader(csvfile, delimiter=",", quotechar='"')
        for row in records:

            if station := Station.nodes.get_or_none(
                station_name=row["station_name"],
            ):
                if tube_line.data_file_name == "master_station_names":
                    print(f'\tUpdating from master {row["station_name"]}')
                    station.location = row["location"]
                    station.year_opened = int(row["year_opened"])
                    station.wiggle_ranking = float(row["wiggle_ranking"])
                else:
                    print(f'\tUpdating for {tube_line.line_name} {row["station_name"]}')
                    station.update_tube_lines(tube_line.line_name)
                    station.update_tube_line_identifiers(row["tube_line_identifier"])

            else:
                print(f'\tAdding {row["station_name"]}')
                if row["end_of_line"] == "True":
                    end_of_line_for = [tube_line.line_name]
                else:
                    end_of_line_for = []

                station = Station(
                    station_name=row["station_name"],
                    tube_lines=[tube_line.line_name],
                    tube_line_identifiers=[row["tube_line_identifier"]],
                    end_of_line_for=end_of_line_for,
                )

            station.save()
    print(f"Loaded stations for {tube_line.line_name} line")


def load_tube_lines() -> None:
    # TODO profile this

    with db.transaction:
        tll = TubeLineList()

        load_tube_stations(tll.piccadilly)
        load_tube_stations(tll.central)
        load_tube_stations(tll.victoria)
        load_tube_stations(tll.bakerloo)
        load_tube_stations(tll.jubilee)
        load_tube_stations(tll.metropolitan)
        load_tube_stations(tll.hammersmith_and_city)
        load_tube_stations(tll.district)
        load_tube_stations(tll.northern)
        load_tube_stations(tll.waterloo_and_city)
        load_tube_stations(tll.master_station_names)

    with db.transaction:
        load_connections(tll.piccadilly)
        load_connections(tll.central)
        load_connections(tll.victoria)
        load_connections(tll.bakerloo)
        load_connections(tll.jubilee)
        load_connections(tll.metropolitan)
        load_connections(tll.hammersmith_and_city)
        load_connections(tll.district)
        load_connections(tll.northern)
        load_connections(tll.waterloo_and_city)


if __name__ == "__main__":
    # db.cypher_query("MATCH (n) DETACH DELETE n;")
    load_tube_lines()
