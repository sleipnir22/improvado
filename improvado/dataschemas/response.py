from pydantic import BaseModel

from improvado.dataschemas.user import User


class FriendsGetResponse(BaseModel):
    class Response(BaseModel):
        items: list[User]
        count: int

    response: Response
