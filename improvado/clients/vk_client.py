from improvado.clients.base import Client
from improvado.dataschemas.user import User


class VkClient(Client):
    API_URL: str = "https://api.vk.com"

    def __init__(self, token: str):
        super().__init__()
        self.token = token
        self.header = {
            "Authorization": f"Bearer {token}"
        }

    async def get_user_friends(
            self,
            user_id: str,
            order: str,
            list_id: str,
            count: int,
            offset: int,
            fields: str) -> list[User]:
        url = f"{self.API_URL}/friends.get"
        params = {
            "user_id": user_id,
            "order": order,
            "list_id": list_id,
            "count": count,
            "offset": offset,
            "fields": fields,
        }
        response = await self.session.get(url=url, params=params)
