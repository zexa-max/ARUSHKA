import re
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME")

MONGO_DB_URI = getenv("MONGO_DB_URI")

OWNER_ID = int(getenv("OWNER_ID"))
LOGGER_ID = int(getenv("LOGGER_ID"))

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True") == "True"
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 600))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 200))

STRING1 = getenv("STRING_SESSION")

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/1df484ee2b80ec2e2bd2e.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/0dfcbd2935f41b21af907.jpg")
DEFAULT_IMG = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"

# All default fallback images
PLAYLIST_IMG_URL = DEFAULT_IMG
STATS_IMG_URL = DEFAULT_IMG
TELEGRAM_AUDIO_URL = DEFAULT_IMG
TELEGRAM_VIDEO_URL = DEFAULT_IMG
STREAM_IMG_URL = DEFAULT_IMG
SOUNCLOUD_IMG_URL = DEFAULT_IMG
YOUTUBE_IMG_URL = DEFAULT_IMG
SPOTIFY_ARTIST_IMG_URL = DEFAULT_IMG
SPOTIFY_ALBUM_IMG_URL = DEFAULT_IMG
SPOTIFY_PLAYLIST_IMG_URL = DEFAULT_IMG

def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with https://")
