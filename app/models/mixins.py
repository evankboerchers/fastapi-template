from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UUIDPKMixin(object):
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

