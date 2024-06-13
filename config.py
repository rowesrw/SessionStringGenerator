import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 29985150))

    API_HASH = os.environ.get("API_HASH", "3dfe3b92bc6cb022d7ff451d6fbd8f6b")
