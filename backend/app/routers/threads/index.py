from app.routers import router
from app.routers.threads import schemas
from pydantic import UUID4


@router.get("/threads/{thread_id}")
async def get_thread_by_id(thread_id: UUID4):
    pass


@router.post("/messages")
async def post_thread(thread: schemas.CreateThreadParams):
    pass


@router.get("/threads/{thread_id}/messages")
async def get_messages_by_thread_id(thread_id: UUID4):
    pass
