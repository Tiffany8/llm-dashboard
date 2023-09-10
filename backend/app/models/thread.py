from enum import Enum

from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class ThreadState(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"


class Thread(BaseModel):
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("userprofile.id"))
    name = Column(Text, nullable=True)
    thread_state = Column(SAEnum(ThreadState), default=ThreadState.ACTIVE)

    created_by = relationship("UserProfile", back_populates="threads")
    messages = relationship("Message", back_populates="thread")
