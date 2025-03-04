from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    # Postgresql Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    #JWT Signing keys
    JWT_PRIVATE: str
    JWT_PUBLIC: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )
settings = Settings()