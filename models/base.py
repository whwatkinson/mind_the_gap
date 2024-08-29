from datetime import datetime
from uuid import uuid4

from neomodel import StructuredNode, StringProperty, DateTimeProperty, FloatProperty


class BaseStation(StructuredNode):

    created_at = DateTimeProperty(default_now=True)
    updated_at = DateTimeProperty(default_now=True)
    deleted_at = DateTimeProperty(default_now=True)
    uuid = StringProperty(unique_index=True, default=uuid4)

    def pre_save(self):
        self.updated_at = datetime.now()
