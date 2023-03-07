from improvado.clients.base import Client
from improvado.dataschemas.request import FriendsGetRequest
from improvado.dataschemas.user import Users
from improvado.exceptions import BadID, PrivateProfile, BadParameter


class VkClient(Client):
    API_URL: str = "https://api.vk.com/method"
    CHUNK_STEP = 5000

    def __init__(self, token: str):
        super().__init__()
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    @staticmethod
    def handle_exceptions(data, request):
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

    def chunks(self, request, url) -> Users:
        response = self.session.get(url=url, params=request.dict(exclude_none=True), headers=self.headers)
        data = response.json()
        self.handle_exceptions(data, request)
        yield Users.parse_obj(data["response"]["items"])

        while data["response"]["count"] >= 5000:
            request.offset += 5000
            request.order = ""
            response = self.session.get(url=url, params=request.dict(exclude_none=True), headers=self.headers)
            data = response.json()
            if not len(data["response"]["items"]):
                break
            yield Users.parse_obj(data["response"]["items"])


    def get_user_friends(self, request: FriendsGetRequest):
        url = f"{self.API_URL}/friends.get"
        data_chunks = self.chunks(request, url)

        return data_chunks
