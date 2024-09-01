from uuid import uuid4

from project_root import get_project_root

LINE_CODE = "P"


def list_to_stations() -> None:

    with open(f"{get_project_root()}/data/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")
    print(
        "station_name,end_of_line,tube_line_identifier,location,year_opened,wiggle_ranking"
    )
    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        # station_name,end_of_line,tube_line_identifier,location,year_opened,wiggle_ranking
        print(
            f'{item},False,{LINE_CODE}{index},"[lon, lat]",,0.0'
        )


def list_to_connections() -> None:

    with open(f"{get_project_root()}/data/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")
    print(
        "station_name,from_station,to_station,forward_travel,travel_time_seconds,distance_km,uuid"
    )
    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        if index == 0:
            print(f"{item},{LINE_CODE}{index},{LINE_CODE}1,True,0,0,{uuid4()}")
        elif index == len(file_contents_list) - 1:
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{len(file_contents_list[:-2])},False,0,0,{uuid4()}"
            )
        else:
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{index - 1},False,0,0,{uuid4()}"
            )
            print(
                f"{item},{LINE_CODE}{index},{LINE_CODE}{index + 1},True,0,0,{uuid4()}"
            )


if __name__ == "__main__":
    list_to_stations()
    print("\n\n\n")
    list_to_connections()
