from app.enums import MessageType
from pydantic import UUID4, BaseModel


class CreateMessageParams(BaseModel):
    user_id: UUID4
    thread_id: UUID4
    message_type: MessageType
    content: str
