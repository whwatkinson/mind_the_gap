from neomodel import (
    RelationshipTo,
    RelationshipFrom,
    BooleanProperty,
    OneOrMore,
    StringProperty,
    FloatProperty,
    ArrayProperty,
    StructuredNode,
    IntegerProperty,
)

from models.audit import AuditInformation
from models.connection import Connection


class Station(StructuredNode, AuditInformation):
    station_name = StringProperty(unique_index=True)
    end_of_line = BooleanProperty(default=False)
    location = StringProperty(default="[lon, lat]")
    year_opened = IntegerProperty(default=0)

    tube_lines = ArrayProperty(StringProperty(), required=True)
    tube_line_identifiers = ArrayProperty(StringProperty(), required=True)

    wiggle_ranking = FloatProperty(default=0.0)

    def update_tube_lines(self, new_tube_line: str) -> None:
        if new_tube_line not in self.tube_lines:
            self.tube_lines.append(new_tube_line)

    def update_tube_line_identifiers(self, tube_line_identifier: str) -> None:
        if tube_line_identifier not in self.tube_line_identifiers:
            self.tube_line_identifiers.append(tube_line_identifier)

    next = RelationshipTo(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
    previous = RelationshipFrom(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )

    bakerloo = RelationshipTo(
        cls_name="Station",
        relation_type="BAKERLOO",
        cardinality=OneOrMore,
        model=Connection,
    )

    central = RelationshipTo(
        cls_name="Station",
        relation_type="CENTRAL",
        cardinality=OneOrMore,
        model=Connection,
    )

    hammersmith_and_city = RelationshipTo(
        cls_name="Station",
        relation_type="HAMMERSMITH_AND_CITY",
        cardinality=OneOrMore,
        model=Connection,
    )

    jubilee = RelationshipTo(
        cls_name="Station",
        relation_type="JUBILEE",
        cardinality=OneOrMore,
        model=Connection,
    )

    metropolitan = RelationshipTo(
        cls_name="Station",
        relation_type="METROPOLITAN",
        cardinality=OneOrMore,
        model=Connection,
    )

    piccadilly = RelationshipTo(
        cls_name="Station",
        relation_type="PICCADILLY",
        cardinality=OneOrMore,
        model=Connection,
    )

    victoria = RelationshipTo(
        cls_name="Station",
        relation_type="VICTORIA",
        cardinality=OneOrMore,
        model=Connection,
    )

    def __repr__(self) -> str:
        return f"{self.station_name}"
