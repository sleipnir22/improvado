from improvado.clients.base import Client
from improvado.dataschemas.request import FriendsGetRequest
from improvado.dataschemas.user import Users
from improvado.exceptions import BadID, PrivateProfile, BadParameter


class VkClient(Client):
    API_URL: str = "https://api.vk.com/method"
    MAX_USERS: int = 5000
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
    # Здесь создается генератор с целью экономии оперативной памяти,
    # а также для пагинации, поскольку VK API возвращает максимум
    # 5000 записей
    # Генератор нужен для "ленивой" итерации без хранения всего массива объектов
    # в оперативной памяти
    def chunks(self, request, url):
        response = self.session.get(url=url, params=request.dict(exclude_none=True), headers=self.headers)
        data = response.json()
        self.handle_exceptions(data, request)
        yield Users.parse_obj(data["response"]["items"])

        while data["response"]["count"] == self.MAX_USERS:
            request.offset += self.MAX_USERS
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
