import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = os.getenv("DISCORD_PREFIX", "!")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
