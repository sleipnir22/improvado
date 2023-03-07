from improvado.clients.base import Client
from improvado.dataschemas.request import FriendsGetRequest
from improvado.dataschemas.response import FriendsGetResponse
from improvado.exceptions import BadID, PrivateProfile, BadParameter
from improvado.logger import logger


class VkClient(Client):
    API_URL: str = "https://api.vk.com/method"

    def __init__(self, token: str):
        super().__init__()
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_user_friends(self, request: FriendsGetRequest) -> FriendsGetResponse:
        url = f"{self.API_URL}/friends.get"
        params = request.dict(
            exclude_none=True
        )
        logger.debug(f"query params: {params}")
        response = self.session.get(url=url, params=params, headers=self.headers)
        data = response.json()

        logger.debug(f"VK API response: {data}")

        if "error" in data:
            error_code = data["error"]["error_code"]
            if error_code == 113:
                raise BadID
            if error_code == 30:
                raise PrivateProfile
            if error_code == 100:
                raise BadParameter

        if data["response"]["count"] == 0:
            raise BadID(request.user_id)

        return FriendsGetResponse.parse_obj(data)
