from pydantic import BaseModel

from improvado.dataschemas.dictionary import Sex


class Item(BaseModel):
    id: int
    title: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str

    country: Item | None
    city: Item | None
    bdate: str | None
    sex: Sex
    track_code: str
    can_access_closed: bool
    is_closed: bool