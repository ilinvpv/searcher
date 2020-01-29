from confi import BaseEnvironConfig, ConfigField, BooleanConfig, IntConfig


class Configuration(BaseEnvironConfig):
    # Flask configuration
    DEBUG = BooleanConfig(default=True)
    TESTING = BooleanConfig(default=False)
    DB_ECHO = BooleanConfig(default=False)
    SECRET_KEY = ConfigField(default=__name__, from_var='API_SECRET_KEY')
    SERVER_NAME = ConfigField()

    LOG_LEVEL = IntConfig(default=30)
