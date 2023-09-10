from enum import Enum

from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import Enum as SAEnum
from sqlalchemy import Text


class RoleType(Enum):
    AGENT = "agent"
    USER = "user"


class Role(BaseModel):
    name = Column(SAEnum(RoleType), nullable=False, unique=True)
    description = Column(Text, nullable=False)
