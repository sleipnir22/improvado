from abc import ABC, abstractmethod
import typing as t

from aiohttp import ClientSession


class Client(ABC):
    API_URL: str = ""

    def __init__(self):
        self.session = ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.session.close()


T_Client = t.TypeVar("T_Client", bound=Client)