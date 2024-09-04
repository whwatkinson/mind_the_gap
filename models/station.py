from enum import Enum

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


class TubeLineEnum(Enum):
    BAKERLOO = "BAKERLOO"
    CENTRAL = "CENTRAL"
    DISTRICT = "DISTRICT"
    HAMMERSMITH_AND_CITY = "HAMMERSMITH_AND_CITY"
    JUBILEE = "JUBILEE"
    METROPOLITAN = "METROPOLITAN"
    NORTHERN = "NORTHERN"
    PICCADILLY = "PICCADILLY"
    WATERLOO_AND_CITY = "WATERLOO_AND_CITY"
    VICTORIA = "VICTORIA"


ALL_TUBE_LINES = "|".join(x.value for x in TubeLineEnum)


class Station(StructuredNode, AuditInformation):
    station_name = StringProperty(unique_index=True)
    location = StringProperty(default=None)
    year_opened = IntegerProperty(default=None)
    wiggle_ranking = FloatProperty(default=0.0)

    tube_lines = ArrayProperty(StringProperty(), default=list)
    tube_line_identifiers = ArrayProperty(StringProperty(), default=list)
    end_of_line_for = ArrayProperty(StringProperty(), default=list)

    def update_tube_lines(self, new_tube_line: str) -> None:
        if new_tube_line not in self.tube_lines:
            self.tube_lines.append(new_tube_line)

    def update_tube_line_identifiers(self, tube_line_identifier: str) -> None:
        if tube_line_identifier not in self.tube_line_identifiers:
            self.tube_line_identifiers.append(tube_line_identifier)

    def update_end_of_line_for(self, tube_line: str) -> None:
        if tube_line not in self.end_of_line_for:
            self.end_of_line_for.append(tube_line)

    next = RelationshipTo(
        cls_name="Station", relation_type=ALL_TUBE_LINES, cardinality=OneOrMore
    )
    previous = RelationshipFrom(
        cls_name="Station", relation_type=ALL_TUBE_LINES, cardinality=OneOrMore
    )

    bakerloo = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.BAKERLOO.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    central = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.CENTRAL.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    district = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.DISTRICT.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    hammersmith_and_city = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.HAMMERSMITH_AND_CITY.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    jubilee = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.JUBILEE.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    metropolitan = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.METROPOLITAN.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    northern = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.NORTHERN.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    piccadilly = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.PICCADILLY.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    waterloo_and_city = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.WATERLOO_AND_CITY.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    victoria = RelationshipTo(
        cls_name="Station",
        relation_type=TubeLineEnum.VICTORIA.value,
        cardinality=OneOrMore,
        model=Connection,
    )

    def __repr__(self) -> str:
        return f"{self.station_name}"
