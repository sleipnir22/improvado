import pandas as pd

from improvado.dataschemas.response import FriendsGetResponse
from improvado.logger import logger


def users_to_df(users: FriendsGetResponse):
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
    logger.debug(f"dataframe :{df}")
    return df