from csv import DictReader

from neomodel import config, db

from models.station import Station
from models.tube_line_list import TubeLine, TubeLineList
from project_root import get_project_root
from settings.environment_variables import NEO4J_DATABASE_URL

config.DATABASE_URL = NEO4J_DATABASE_URL


def load_connections(tube_line: TubeLine) -> None:
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

            if getattr(from_station, tube_line.data_file_name.lower()).is_connected(
                to_station
            ):
                continue

            getattr(from_station, tube_line.data_file_name.lower()).connect(
                to_station,
                {
                    "line_name": tube_line.line_name,
                    "line_colour": tube_line.line_colour,
                    "forward_travel": row["forward_travel"] == "True",
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
                station_identifier=row["station_identifier"]
            ):
                station.update_tube_lines(tube_line.line_name)
                station.update_tube_line_identifiers(row["tube_line_identifier"])
                station.save()
            else:
                Station(
                    station_name=row["station_name"],
                    end_of_line=row["end_of_line"] == "True",
                    tube_lines=[tube_line.line_name],
                    tube_line_identifiers=[row["tube_line_identifier"]],
                    station_identifier=row["station_identifier"],
                    location=row["location"],
                    year_opened=int(row["year_opened"]) if row["year_opened"] else 0,
                    wiggle_ranking=row["wiggle_ranking"],
                ).save()
    print(f"Loaded stations for {tube_line.line_name} line")


def load_tube_lines() -> None:
    tll = TubeLineList()
    load_tube_stations(tll.piccadilly)
    load_connections(tll.piccadilly)
    load_tube_stations(tll.central)
    load_connections(tll.central)


if __name__ == "__main__":
    db.cypher_query("MATCH (n) DETACH DELETE n;")
    load_tube_lines()
