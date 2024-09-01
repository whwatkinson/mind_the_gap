from uuid import uuid4

from neomodel import StructuredRel, StringProperty, FloatProperty, BooleanProperty

from models.audit import AuditInformation


class Connection(StructuredRel, AuditInformation):
    uuid = StringProperty(unique_index=True, default=uuid4)
    line_name = StringProperty(required=True)
    line_colour = StringProperty(required=True)

    heading_west = BooleanProperty(default=True)
    travel_time_seconds = FloatProperty(default=0.0)
    distance_km = FloatProperty(default=0.0)
