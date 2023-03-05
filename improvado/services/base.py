from abc import ABC, abstractmethod
import typing as t

from improvado.clients.base import T_Client


class ReportGenerator(ABC):
    def __init__(self, client: T_Client):
        self.client = client

    @abstractmethod
    async def generate_report(self, user_id: str):
        ...

T_ReportGenerator = t.TypeVar("T_ReportGenerator", bound=ReportGenerator)