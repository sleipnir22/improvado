import pandas as pd

from improvado.logger import logger


def users_to_df(user_chunks):
    df = pd.DataFrame()

    for user_chunk in user_chunks:
        for user in user_chunk.__root__:
            df = pd.concat(
                [df, pd.Series(
                    {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "country": user.country.title if user.country is not None else "not found",
                        "city": user.city.title if user.city is not None else "not found",
                        "sex": user.sex.name,
                        "bdate": user.bdate.replace(".", "-") if user.bdate is not None else "not found"
                    }
                ).to_frame().T],
                ignore_index=True,
            )
    logger.debug(f"dataframe :{df}")
    df = df.sort_values(by=["first_name", "last_name"])
    return df
