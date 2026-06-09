from pydantic import HttpUrl, SecretStr, BaseModel


class TelegramConfig(BaseModel):
    token: SecretStr
    proxy_url: HttpUrl
