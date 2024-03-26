from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    PostgresDsn,
)


class DBSetting(BaseSettings):
    """
    Database settings
    :return DB URL in format: postgresql+asyncpg://user:password@host:port/database
    """
    CONNECTOR: Optional[str] = None
    SCHEME: Optional[str] = None
    PG_HOST: Optional[str] = None
    PG_PORT: Optional[int] = None
    PG_USER: Optional[str] = None
    __PG_PASS: Optional[str] = None
    PG_DB: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    @property
    def db_url(self):
        url = PostgresDsn.build(
            scheme=f'{self.SCHEME}+{self.CONNECTOR}',
            username=self.PG_USER,
            password=self.__PG_PASS,
            host=self.PG_HOST,
            path=self.PG_DB,
            port=self.PG_PORT,
        )
        return str(url)


DB = DBSetting()

if __name__ == '__main__':
    print(DB.db_url)
