from pydantic import UUID4, BaseModel


class CreateUserParams(BaseModel):
    name: str
    organization_name: str
    role_id: UUID4
