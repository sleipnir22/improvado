import io
from datetime import datetime

import dateutil.parser
import pandas as pd

from improvado.dataschemas.request import FriendsGetRequest
from improvado.services.base import ReportGenerator, Report, ReportType


class CsvReportGenerator(ReportGenerator):
    REPORT_TYPE = ReportType.csv
    def generate_report(self, user_id: int) -> Report:
        request = FriendsGetRequest(user_id=user_id)
        users = self.client.get_user_friends(request)
        df = pd.DataFrame()
        for item in users.response.items:
            df = pd.concat(
                [df, pd.Series(
                    {
                        "id": item.id,
                        "first_name": item.first_name,
                        "last_name": item.last_name,
                        "country": item.country.title if item.country is not None else "not found",
                        "city": item.city.title if item.city is not None else "not found",
                        "sex": item.sex.name,
                        "bdate": item.bdate.replace(".", "-") if item.bdate is not None else "not found"
                    }
                ).to_frame().T],
                ignore_index=True,
            )
        file_stream = io.StringIO(df.to_csv(index=False), newline="\n")
        return file_stream