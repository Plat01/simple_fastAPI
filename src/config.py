import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

# use only for DB_PASS
load_dotenv()

class ProgBaseSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=find_dotenv('.env'),
        env_file_encoding='utf-8',
        extra='ignore',
    )


class DBSetting(ProgBaseSettings):
    """
    Database settings
    :return DB URL in format: postgresql+asyncpg://user:password@host:port/database
    """

    SCHEME: str = None
    CONNECTOR: Optional[str] = None
    DB_HOST: str = None
    DB_PORT: int = None
    DB_USER: str = None
    # __DB_PASS: str = None
    DB_NAME: str = None

    DATABASE_URI: str = "{SCHEME}+{CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    @field_validator("DATABASE_URI", mode='before', check_fields=True)
    def set_db_uri(cls, v: str, info: ValidationInfo):
        return v.format(
            SCHEME=info.data.get("SCHEME"),
            CONNECTOR=info.data.get("CONNECTOR"),
            DB_USER=info.data.get("DB_USER"),
            DB_PASSWORD=os.environ.get('DB_PASS'),
            DB_HOST=info.data.get("DB_HOST"),
            DB_PORT=info.data.get("DB_PORT"),
            DB_NAME=info.data.get("DB_NAME"),
        )



DB = DBSetting()

if __name__ == '__main__':
    print(DB.DB_NAME)
    # print(DB.__DBSetting__DB_PASS)
    print(DB.DATABASE_URI)


