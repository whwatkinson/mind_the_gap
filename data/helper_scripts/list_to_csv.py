from uuid import uuid4

from project_root import get_project_root


def list_to_stations() -> None:

    with open(f"{get_project_root()}/data/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")
    print("station_name,end_of_line,tube_line_identifier,station_identifier,location,year_opened,wiggle_ranking")
    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        # station_name,end_of_line,tube_line_identifier,station_identifier,location,year_opened,wiggle_ranking
        print(f'{item},False,P{index},{hash(item.lower())},"[lon, lat]",,0.0')


# Earl's Court,False,P23,8968448765763071821,"[51.490616 0.195848]",8.6
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
            print(f"{item},P{index},P1,True,0,0,{uuid4()}")
        elif index == len(file_contents_list) - 1:
            print(
                f"{item},P{index},P{len(file_contents_list[:-2])},False,0,0,{uuid4()}"
            )
        else:
            print(f"{item},P{index},P{index - 1},False,0,0,{uuid4()}")
            print(f"{item},P{index},P{index + 1},True,0,0,{uuid4()}")


if __name__ == "__main__":
    list_to_stations()
    # list_to_connections()
