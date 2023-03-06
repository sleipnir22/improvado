from abc import ABC, abstractmethod
import typing as t
from enum import Enum

from improvado.clients.base import T_Client

Report = t.NewType("Report", t.IO)

class ReportType(str, Enum):
    csv = "csv"
    tsv = "tsv"
    json = "json"

class ReportGenerator(ABC):
    REPORT_TYPE: ReportType
    def __init__(self, client: T_Client):
        self.client = client

    @abstractmethod
    def generate_report(self, user_id: int) -> Report:
        ...

T_ReportGenerator = t.TypeVar("T_ReportGenerator", bound=ReportGenerator)
