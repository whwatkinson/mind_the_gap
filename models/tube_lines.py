from models.station import Station
from neomodel import StringProperty


class Piccadilly(Station):
    line_name = StringProperty(default="Piccadilly")
    line_colour = StringProperty(default="#1C1865", required=True)
