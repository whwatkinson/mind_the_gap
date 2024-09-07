from dataclasses import dataclass


@dataclass
class TubeLine:
    line_name: str
    line_colour: str
    data_file_name: str


@dataclass
class TubeLineList:
    master_station_names = TubeLine(
        "Master Station Names", "#000000", "master_station_names"
    )
    piccadilly = TubeLine("Piccadilly", "#1C1865", "piccadilly")
    central = TubeLine("Central", "#E32017", "central")
    victoria = TubeLine("Victoria", "#0098D4", "victoria")
    bakerloo = TubeLine("Bakerloo", "#894E24", "bakerloo")
    jubilee = TubeLine("Jubilee", "#A9BDB4", "jubilee")
    metropolitan = TubeLine("Metropolitan", "#751056", "metropolitan")
    hammersmith_and_city = TubeLine(
        "Hammersmith & City", "#F3A9BB", "hammersmith_and_city"
    )
    district = TubeLine("District", "#007229", "district")
    northern = TubeLine("Northern", "#000000", "northern")
    waterloo_and_city = TubeLine("Waterloo & City", "#95CDBA", "waterloo_and_city")
