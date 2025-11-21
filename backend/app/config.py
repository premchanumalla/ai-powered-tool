from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Email Triage Copilot"

    class Config:
        env_file = ".env"

settings = Settings()
