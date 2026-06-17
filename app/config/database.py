from pydantic import BaseModel, PostgresDsn


class PostgresConfig(BaseModel):
    url: PostgresDsn
