from neomodel import RelationshipTo, RelationshipFrom, OneOrMore
from neomodel import StringProperty, FloatProperty

from models.base import BaseStation


class Station(BaseStation):

    location = StringProperty(default="lon, lat")
    name = StringProperty(unique_index=True)
    colour = StringProperty(default="#004225")
    wiggle_ranking = FloatProperty(deleted_at=0.0)

    next = RelationshipTo(cls_name="Station", relation_type="NEXT", cardinality=OneOrMore)
    previous = RelationshipFrom(cls_name="Station", relation_type="NEXT", cardinality=OneOrMore)

