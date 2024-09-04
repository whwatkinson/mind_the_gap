from csv import DictReader, DictWriter
from uuid import uuid4

from project_root import get_project_root

LINE_CODE = "N"


def list_to_stations() -> None:

    with open(f"{get_project_root()}/data/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")
    print(
        "station_name,end_of_line,tube_line_identifier"
    )
    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        # station_name,end_of_line,tube_line_identifier
        print(f'{item},False,{LINE_CODE}{index}')


def list_to_connections() -> None:

    with open(f"{get_project_root()}/data/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")
    print(
        "station_name,from_station,to_station,heading_west,travel_time_seconds,distance_km,uuid"
    )
    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        if index == 0:
            print(f"{item},{LINE_CODE}{index},{LINE_CODE}1,False,0,0,{uuid4()}")
        elif index == len(file_contents_list) - 1:
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{len(file_contents_list[:-2])},True,0,0,{uuid4()}"
            )
        else:
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{index - 1},False,0,0,{uuid4()}"
            )
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{index + 1},True,0,0,{uuid4()}"
            )


def update_master_stations_list():
    with open(
        f"{get_project_root()}/data/stations/master_station_names.csv",
        newline="\n",
    ) as csvfile:
        existing_stations_names = set()
        existing_stations = list()
        for record in DictReader(csvfile, delimiter=",", quotechar='"'):
            existing_stations_names.add(record["station_name"])
            existing_stations.append(record)

    lines = [
        "bakerloo",
        "central",
        # "circle",
        "district",
        "hammersmith_and_city",
        "jubilee",
        "metropolitan",
        "northern",
        "piccadilly",
        "victoria",
        # "waterloo_and_city",
    ]

    new_records = list()
    new_records_seen = set()

    for line in lines:
        with open(
            f"{get_project_root()}/data/stations/{line}.csv",
            newline="\n",
        ) as csvfile:
            for record in DictReader(csvfile, delimiter=",", quotechar='"'):
                station_name = record["station_name"]
                if (
                    station_name not in existing_stations_names
                    and station_name not in new_records_seen
                ):

                    new_records.append(record)
                    new_records_seen.add(station_name)

    all_records = sorted(
        [x for x in (existing_stations + new_records)], key=lambda x: x["station_name"]
    )

    with open(
        f"{get_project_root()}/data/stations/master_station_names.csv",
        mode="w",
        newline="\n",
    ) as csvfile:
        fieldnames = ["station_name", "location", "year_opened", "wiggle_ranking"]
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in all_records:

            # TODO REMOVE temp
            record = {k: v for k, v in record.items() if k not in ("tube_line_identifier", "end_of_line")}

            writer.writerow(record)


if __name__ == "__main__":
    # update_master_stations_list()
    list_to_stations()
    print("\n\n\n")
    # list_to_connections()
