from abc import ABC, abstractmethod
import typing as t

import requests

class Client(ABC):
    API_URL: str = ""

    def __init__(self):
        self.session = requests.Session()

    @abstractmethod
    def get_user_friends(self, request):
        ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.session.close()


T_Client = t.TypeVar("T_Client", bound=Client)
