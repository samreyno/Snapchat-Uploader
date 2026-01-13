import os
from dotenv import load_dotenv

load_dotenv()

SNAPCHAT_ACCESS_TOKEN = os.getenv("SNAPCHAT_ACCESS_TOKEN")
SNAPCHAT_ACCOUNT_ID = os.getenv("SNAPCHAT_ACCOUNT_ID")

if not SNAPCHAT_ACCESS_TOKEN:
    raise RuntimeError("SNAPCHAT_ACCESS_TOKEN is not set")

if not SNAPCHAT_ACCOUNT_ID:
    raise RuntimeError("SNAPCHAT_ACCOUNT_ID is not set")
