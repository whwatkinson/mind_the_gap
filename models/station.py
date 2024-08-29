from neomodel import RelationshipTo, RelationshipFrom, BooleanProperty, OneOrMore
from neomodel import StringProperty, FloatProperty

from models.base_node import BaseNode


class Station(BaseNode):
    station_name = StringProperty(unique_index=True, required=True)
    end_of_line = BooleanProperty(default=False, required=True)
    location = StringProperty(default="[lon, lat]")

    line_identifier = StringProperty(required=True)
    line_name = StringProperty(default="line_name", required=True)
    line_colour = StringProperty(default="#ABCDEFG", required=True)

    wiggle_ranking = FloatProperty(deleted_at=0.0)

    next = RelationshipTo(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
    previous = RelationshipFrom(
        cls_name="Station", relation_type="NEXT", cardinality=OneOrMore
    )
