from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str = "7e12d43c7e12d43c7e12d43c3f7d00397e77e127e12d43c1a1150a33ec49d87a47a43c3"

settings = Settings()