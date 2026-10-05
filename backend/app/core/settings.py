import os

from dotenv import load_dotenv

from dataclasses import dataclass


load_dotenv()


@dataclass
class Settings:
    """
    Klasa przechowująca ustawienia aplikacji.
    """
    app_name: str = "Report Studio"

    app_version: str = "0.1.0"

    api_prefix: str = "/api/v1"

    mssql_server: str | None = os.getenv(
        "MSSQL_SERVER"
    )

    mssql_database: str | None = os.getenv(
        "MSSQL_DATABASE"
    )

    mssql_username: str | None = os.getenv(
        "MSSQL_USERNAME"
    )

    mssql_password: str | None = os.getenv(
        "MSSQL_PASSWORD"
    )

    mssql_schema: str | None = os.getenv(
    "MSSQL_SCHEMA"
    )


settings = Settings()
