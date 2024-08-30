from datetime import datetime
from uuid import uuid4

from neomodel import StringProperty, DateTimeProperty


class AuditInformation:
    created_at = DateTimeProperty(default_now=True)
    updated_at = DateTimeProperty(default_now=True)
    uuid = StringProperty(unique_index=True, default=uuid4)

    def post_create(self):
        self.created_at = datetime.now()

    def pre_save(self):
        self.updated_at = datetime.now()
