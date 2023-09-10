from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UserProfile(BaseModel):
    is_active = Column(Boolean, default=True)
    is_archived = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    name = Column(Text, nullable=False, unique=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organization.id"), nullable=False
    )
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"), nullable=False)

    messages = relationship("Message", back_populates="user")
    organization = relationship("Organization", back_populates="user")
    role = relationship("Role", back_populates="user")
