from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    deactivated: str
    is_closed: bool
    can_access_closed: bool

    country: str | None
    city: str | None
    bdate: str | None
    sex: int | None

class User(BaseModel):
    first_name: str
    last_name: str
    country: str
    city: str
    bdate: str
    gender: str