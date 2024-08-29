from project_root import get_project_root


def list_to_stations():

    with open(f"{get_project_root()}/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")

    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'
        # station_name,end_of_line,line_identifier,connections,location,wiggle_ranking
        print(f'{item},False,P{index},,"[lon, lat]",0.0')


def list_to_connections():

    with open(f"{get_project_root()}/helper_scripts/clipboard.txt") as file_handle:
        file_contents_list = file_handle.read().split("\n")

    for index, item in enumerate(file_contents_list):
        if "," in item:
            item = f'"{item}"'

        connections = []
        if index == 0:
            connections.append("P1")
        elif index == len(file_contents_list) - 1:
            connections.append(f"P{len(file_contents_list[:-2])}")
        else:
            connections.append(f"P{index - 1}")
            connections.append(f"P{index + 1}")

        # station_name,line_identifier,connections,travel_time,distance_km
        print(f'{item},P{index},"{connections}",0,0')


if __name__ == "__main__":
    # list_to_stations()
    list_to_connections()
