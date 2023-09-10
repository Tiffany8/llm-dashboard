from app.enums import EventType, ResourceType
from app.models.base import BaseModel
from sqlalchemy import JSON, Column, Enum
from sqlalchemy.dialects.postgresql import UUID


class Event(BaseModel):
    event_type = Column(Enum(EventType), nullable=False)
    metadadta = Column(JSON, nullable=False)
    resource_id = Column(UUID(as_uuid=True), nullable=False)
    resource_type = Column(Enum(ResourceType), nullable=False)
