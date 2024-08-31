from neomodel import (
    RelationshipTo,
    RelationshipFrom,
    BooleanProperty,
    OneOrMore,
    StringProperty,
    FloatProperty,
    ArrayProperty,
    StructuredNode,
)

from models.audit import AuditInformation
from models.connection import Connection


class Station(StructuredNode, AuditInformation):
    station_name = StringProperty(unique_index=True)
    end_of_line = BooleanProperty(default=False)
    location = StringProperty(default="[lon, lat]")

    tube_lines = ArrayProperty(required=True)
    tube_line_identifiers = ArrayProperty(required=True)
    station_identifier = StringProperty(required=True)

    wiggle_ranking = FloatProperty(default=0.0)

    next = RelationshipTo(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
    previous = RelationshipFrom(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )

    piccadilly = RelationshipTo(
        cls_name="Station",
        relation_type="PICCADILLY",
        cardinality=OneOrMore,
        model=Connection,
    )
