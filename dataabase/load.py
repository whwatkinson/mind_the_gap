from csv import DictReader
from dataclasses import dataclass
from typing import Union

from neomodel import config, db

from settings.environment_variables import NEO4J_DATABASE_URL

# from models.tube_lines import Piccadilly
from models.station import Station
from project_root import get_project_root

config.DATABASE_URL = NEO4J_DATABASE_URL


@dataclass
class TubeLine:
    line_name: str
    line_colour: str
    data_file_name: str


@dataclass
class TubeLineList:
    piccadilly = TubeLine("Piccadilly", "#1C1865", "piccadilly")


def load_connections(tube_line: TubeLine) -> None:
    with open(
        f"{get_project_root()}/data/lines/{tube_line.data_file_name}.csv",
        newline="\n",
    ) as csvfile:
        records = DictReader(csvfile, delimiter=",", quotechar='"')
        for row in records:
            pass


def load_tube_stations(tube_line: TubeLine) -> None:
    with open(
        f"{get_project_root()}/data/lines/{tube_line.data_file_name}.csv",
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
                    end_of_line=row["end_of_line"],
                    tube_lines=[tube_line.line_name],
                    tube_line_identifiers=[row["tube_line_identifier"]],
                    station_identifier=row["station_identifier"],
                    location=row["location"],
                    wiggle_ranking=row["wiggle_ranking"],
                ).save()


def load_tube_line() -> None:
    pass


if __name__ == "__main__":
    # db.cypher_query("MATCH (n) DETACH DELETE n;")
    tll = TubeLineList()
    load_tube_stations(tll.piccadilly)
