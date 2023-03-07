import io

from improvado.dataschemas.request import FriendsGetRequest
from improvado.services.base import ReportGenerator, Report, ReportType
from improvado.services.utils import users_to_df


class CsvReportGenerator(ReportGenerator):
    REPORT_TYPE = ReportType.tsv
    def generate_report(self, user_id: int) -> Report:
        request = FriendsGetRequest(user_id=user_id)
        users_chunks = self.client.get_user_friends(request)
        df = users_to_df(users_chunks)
        file_stream = io.StringIO(df.to_csv(index=False, sep = "\t"))
        return file_stream