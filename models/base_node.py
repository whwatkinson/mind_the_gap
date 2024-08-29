from datetime import datetime
from uuid import uuid4

from neomodel import StructuredNode, StringProperty, DateTimeProperty


class BaseNode(StructuredNode):
    created_at = DateTimeProperty(default_now=True, required=True)
    updated_at = DateTimeProperty(default_now=True, required=True)
    uuid = StringProperty(unique_index=True, default=uuid4, required=True)

    def post_create(self):
        self.created_at = datetime.now()

    def pre_save(self):
        self.updated_at = datetime.now()
