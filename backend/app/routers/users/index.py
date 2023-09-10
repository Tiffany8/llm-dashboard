from app import routers
from app.routers.users import schemas
from pydantic import UUID4


@routers.post("/users")
async def post_user(user: schemas.CreateUserParams):
    pass


@routers.get("/users")
async def get_users():
    pass


@routers.get("/users/{user_id}")
async def get_user(user_id: UUID4):
    pass
