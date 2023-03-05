from improvado.clients.base import Client


class VkClient(Client):
    async def get_user_friends(self, user_id: str):
        pass

    async def close(self):
        pass