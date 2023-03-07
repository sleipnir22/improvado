import io

from improvado.dataschemas.request import FriendsGetRequest
from improvado.services.base import ReportGenerator, Report, ReportType
from improvado.services.utils import users_to_df


class CsvReportGenerator(ReportGenerator):
    REPORT_TYPE = ReportType.csv
    def generate_report(self, user_id: int) -> Report:
        request = FriendsGetRequest(user_id=user_id)
        users = self.client.get_user_friends(request)
        df = users_to_df(users)
        file_stream = io.StringIO(df.to_csv(index=False))
        return file_stream