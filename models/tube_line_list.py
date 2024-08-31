from dataclasses import dataclass


@dataclass
class TubeLine:
    line_name: str
    line_colour: str
    data_file_name: str


@dataclass
class TubeLineList:
    piccadilly = TubeLine("Piccadilly", "#1C1865", "piccadilly")
    central = TubeLine("Central", "#E32017", "central")
