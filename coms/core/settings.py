import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    env: str = ""
    title: str = "Numan Communications"
    description: str = "Numan Communications"
    version: str = "1.0.0"
    debug: bool = False


class TestSettings(Settings):
    env: str = "test"
    debug: bool = False


class LocalSettings(Settings):
    env: str = "local"
    debug: bool = True


class ProductionSettings(Settings):
    env: str = "production"


class StagingSettings(Settings):
    env: str = "staging"


def init_settings() -> Settings:
    environment = os.environ.get("ENVIRONMENT", "local")
    match environment.lower():
        case "production":
            return ProductionSettings()
        case "staging":
            return StagingSettings()
        case "test":
            return TestSettings()
        case _:
            return LocalSettings()


settings = init_settings()
