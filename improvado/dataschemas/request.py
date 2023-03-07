from pydantic import BaseModel


class BaseRequest(BaseModel):
    v: str = '5.131'


class FriendsGetRequest(BaseRequest):
    user_id: int
    order: str = "name"
    list_id: int | None
    count: int | None
    offset: int | None = 0
    fields: str = "bdate," \
                  "city," \
                  "country," \
                  "sex"
