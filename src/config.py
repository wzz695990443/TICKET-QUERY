from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GC_URL: str
    TICKET_URL: str
    ORGCODE:  str
    USER_CODE:  str
    PASSWORD:  str

    model_config = SettingsConfigDict(toml_file="config.toml")


def get_settings():
    return Settings()
