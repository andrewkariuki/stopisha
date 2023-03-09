import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

from stopisha.utilities.custom_logger import custom_logger

load_dotenv()


class Settings(BaseSettings):
    """Base configuration"""

    BASE_DIR = Path(__file__).parent.parent
    TESTING = False

    TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
    TWITTER_API_KEY_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
    TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
    TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")


class TestConfig(Settings):
    """Test configuration"""

    DEBUG = False
    TESTING = True


class StagingConfig(Settings):
    """Staging configuration"""

    DEBUG = False


class DevelopmentConfig(Settings):
    """Development configuration"""

    DEBUG = True


class ProductionConfig(Settings):
    """Production configuration"""

    DEBUG = False


settings = {
    "default": DevelopmentConfig(),
    "development": DevelopmentConfig(),
    "production": ProductionConfig(),
    "staging": StagingConfig(),
    "test": TestConfig(),
}

config = settings[os.environ.get("APP_ENV", "default")]

syslog = custom_logger("stopisha")
