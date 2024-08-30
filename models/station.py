from neomodel import (
    RelationshipTo,
    RelationshipFrom,
    BooleanProperty,
    OneOrMore,
    StringProperty,
    FloatProperty,
)

from models.audit import AuditInformation


class Station(AuditInformation):
    station_name = StringProperty(unique_index=True)
    end_of_line = BooleanProperty(default=False)
    location = StringProperty(default="[lon, lat]")

    line_identifier = StringProperty(required=True)
    line_name = StringProperty(required=True)
    line_colour = StringProperty(required=True)

    wiggle_ranking = FloatProperty(deleted_at=0.0)

    next = RelationshipTo(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
    previous = RelationshipFrom(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
