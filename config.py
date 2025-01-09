# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24300735"))
API_HASH = getenv("API_HASH", "753829e742c36c4491656e113cd74dcd")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7869658556").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saverestrictionsbot:ntxdcDZXhROjC4C7@cluster0.dh8r0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002279935644")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002473877253"))
