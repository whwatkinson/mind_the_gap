from datetime import datetime
from uuid import uuid4

from neomodel import StructuredRel, StringProperty, DateTimeProperty

from models.audit import AuditInformation


class Connection(AuditInformation):
    pass
