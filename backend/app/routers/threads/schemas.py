from typing import Optional

from app.enums import MessageType
from pydantic import UUID4, BaseModel


class CreateThreadParams(BaseModel):
    name: Optional[str] = None
    thread_id: UUID4
    message_type: MessageType
    content: str
