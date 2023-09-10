from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, Text


class Organization(BaseModel):
    name = Column(Text, nullable=False)
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_archived = Column(Boolean, default=False)
