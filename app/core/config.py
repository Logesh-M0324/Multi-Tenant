from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Modaglimmora"
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "modaglimmora_test"
    JWT_SECRET: str = "f63bfc74981b046563a5a9bb2190dc68"
    JWT_ALGO: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
