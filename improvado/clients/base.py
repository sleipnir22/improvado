from abc import ABC, abstractmethod
import typing as t

class Client(ABC):
    API_URL: str = ""

    def __init__(self, session):
        self.session = session

    @abstractmethod
    async def get_user_friends(self, user_id: str):
        ...

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    @abstractmethod
    async def close(self):
        self.session.close()

T_Client = t.TypeVar("T_Client", bound=Client)