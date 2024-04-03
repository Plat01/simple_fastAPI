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
    try:
        SCHEME: str = None
        CONNECTOR: Optional[str] = None
        DB_HOST: str = None
        DB_PORT: int = None
        DB_USER: str = None
        # __DB_PASS: str = None
        DB_PASS: str = None
        DB_NAME: str = None
    except Exception as e:
        print(e)

    model_config = SettingsConfigDict(
        env_file='.env.dev',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    @property
    def db_url(self):
        url = PostgresDsn.build(
            scheme=f'{self.SCHEME}+{self.CONNECTOR}',
            username=self.DB_USER,
            # password=self._DBSetting__DB_PASS,
            password=self.DB_PASS,
            host=self.DB_HOST,
            path=self.DB_NAME,
            port=self.DB_PORT,
        )

        return str(url)
        # url = PostgresDsn(f"{self.SCHEME}+{self.CONNECTOR}://{self.DB_USER}:{self.DB_PASS}"
        #                   f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        # return url


DB = DBSetting()

if __name__ == '__main__':
    print(DB.db_url)
    print(type(DB.db_url))
