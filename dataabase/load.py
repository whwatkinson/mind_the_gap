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
class TubeStation:
    line_name: str
    line_colour: str
    data_file_name: str
    station_class: callable


@dataclass
class TubeStationList:
    piccadilly = TubeStation("Piccadilly", "#1C1865", "piccadilly", Station)


def load_connections() -> None:
    pass


def load_tube_stations(tube_station: TubeStation) -> None:
    with open(
        f"{get_project_root()}/data/lines/{tube_station.data_file_name}.csv",
        newline="\n",
    ) as csvfile:
        records = DictReader(csvfile, delimiter=",", quotechar='"')
        for row in records:

            tube_station.station_class(
                station_name=row["station_name"],
                end_of_line=row["end_of_line"],
                tube_lines=[tube_station.line_name],
                tube_line_identifiers=[row["tube_line_identifier"]],
                station_identifier=row["station_identifier"],
                location=row["location"],
                wiggle_ranking=row["wiggle_ranking"],
            ).save()


def load_tube_line() -> None:
    pass


if __name__ == "__main__":
    db.cypher_query("MATCH (n) DETACH DELETE n;")
    tsl = TubeStationList()
    load_tube_stations(tsl.piccadilly)
