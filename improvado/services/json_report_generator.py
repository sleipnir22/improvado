import io
import json

from improvado.dataschemas.request import FriendsGetRequest
from improvado.services.base import ReportGenerator, Report, ReportType
from improvado.services.utils import users_to_df


class JsonReportGenerator(ReportGenerator):
    REPORT_TYPE = ReportType.json
    def generate_report(self, user_id: int) -> Report:
        request = FriendsGetRequest(user_id=user_id)
        users_chunks = self.client.get_user_friends(request)
        df = users_to_df(users_chunks)
        users_json = df.to_json(orient="table", index=False)
        users_json = json.loads(users_json)
        users_json = users_json["data"]
        users_json = json.dumps(users_json, indent=4)
        file_stream = io.StringIO(users_json)
        return file_stream