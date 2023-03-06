import io

from improvado.dataschemas.request import FriendsGetRequest
from improvado.services.base import ReportGenerator, Report, ReportType


class JsonReportGenerator(ReportGenerator):
    REPORT_TYPE = ReportType.json
    def generate_report(self, user_id: int) -> Report:
        request = FriendsGetRequest(user_id=user_id)
        users = self.client.get_user_friends(request)
        users_json = users.json()
        file_stream = io.StringIO(users_json)
        return file_stream