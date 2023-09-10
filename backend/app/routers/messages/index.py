from app.routers import router
from app.routers.messages.schemas import CreateMessageParams
from pydantic import UUID4


@router.get("/messages/{message_id}")
# trunk-ignore(ruff/ARG001)
async def get_message_by_id(message_id: UUID4):
    pass


@router.post("/messages")
# trunk-ignore(ruff/ARG001)
async def post_message(message: CreateMessageParams):
    pass
