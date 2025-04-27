import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27903526"))
API_HASH = getenv("API_HASH", "34f58558a9b72175e378793462cda909")
BOT_USERNAME = "@ShagunMusicbot"
# Get your token from @BotFather on Telegram.main
BOT_TOKEN = getenv("BOT_TOKEN", "7646281973:AAE1SxceM1XMQerlP5EkyTpgSayLkx9Co5k")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sr7blackbirds:5mRE2CGlkCXmI5pL@cluster0.jsssmx8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 200))

SERVER_PLAYLIST_LIMIT = 300  # Set your desired limit here


# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002540021894))
OWNER_ID = int(getenv("OWNER_ID", 1716902346))

# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Ishatgrepo/honeymusic1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SR7_BLACKBIRD")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BINDAAS_BUDDIES")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQGpxiYAEGl3Bi7r-VR2WJOvbNqcrZjHHkjTlC-Mi5mFwkw-aljFFzZYCX7mK0UkRsUeVU4FLv-BUNNOXRavL2cuAAEmzi1ZRr31RcYbB_M3aGYgluvjM23EgJR45kt9wheVVCYfHRQPLiUCYXusIW6SBQPvIaCto3Jt0EzfJpv8MSv2xCH3PoMoYB2unEiIocEfpROhK_uVb7u4g2r78IKEDlvEE7kAKm2DeE6rvjuFYR6N32ajUGRgNMD14ToyBqMlcFHTJUQnFl2xiKkUGQkFwWq7zaGY48P7fo3J8U-KDeLQBX19MbNsGZcuXiHJrWc0o6hdken0etrLDh-cGsJHJ-n3iwAAAAHexHWmAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/1df484ee2b80ec2e2bd2e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/0dfcbd2935f41b21af907.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
STATS_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
