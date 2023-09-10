from app.enums import MessageType
from app.models.base import BaseModel
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Message(BaseModel):
    content = Column(Text, nullable=False)
    message_type = Column(Enum(MessageType), nullable=False)
    thread_id = Column(UUID(as_uuid=True), ForeignKey("thread.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("userprofile.id"), nullable=False)

    user = relationship("UserProfile", back_populates="messages")
    thread = relationship("Thread", back_populates="messages")

    __table_args__ = (Index("idx_message_thread_id", "thread_id"),)
