from csv import DictReader
from dataclasses import dataclass

from project_root import get_project_root


@dataclass
class TubeStation:
    line_name: str
    line_colour: str
    data_file_name: str


@dataclass
class TubeStationList:
    piccadilly = TubeStation("Piccadilly", "#1C1865", "piccadilly")


def load_connections() -> None:
    pass


def load_tube_stations(tube_station: TubeStation) -> None:
    with open(f'{get_project_root()}/data/lines/{tube_station.data_file_name}.csv', newline='\n') as csvfile:
        records = DictReader(csvfile, delimiter=',', quotechar='"')
        for row in records:
            print(row)


def load_tube_line() -> None:
    pass


if __name__ == '__main__':
    tsl = TubeStationList()
    load_tube_stations(tsl.piccadilly)