import re
from pyrogram import filters

# -------- BASIC CONFIGURATION -------- #
API_ID = 23806690
API_HASH = "06622b826df7aabc426a2ab4166f726e"
BOT_TOKEN = "7315305564:AAGOerjP2guIqUdeUbyNhJGI4SLGwQBJ664"
BOT_USERNAME = "@Arush_mbot"

MONGO_DB_URI = "mongodb+srv://Arush:Aryan%40123@arushkamusic.phagtir.mongodb.net/?retryWrites=true&w=majority&appName=ArushkaMusic"

OWNER_ID = 5242138546
LOGGER_ID = -4908653940

SUPPORT_CHANNEL = "https://t.me/arushka_support"
SUPPORT_CHAT = "https://t.me/arush_support"

AUTO_LEAVING_ASSISTANT = True
AUTO_LEAVE_ASSISTANT_TIME = 600

DURATION_LIMIT_MIN = 200
SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 5242880000
TG_VIDEO_FILESIZE_LIMIT = 5242880000

STRING1 = "BQGrkTsAHrD_fPDGimCEvHhxZIh6cpPx2IkkyHYRblisFbU3OcDCIMFVYzKVR1vOkgtsBvcCa5gTLp7Ezatu0fMXk_G-Fqsnu3lOY1Y3FDfyv1nc0RK9qQVsjfqfamiofljxn5vzfSBTSjZAMi54xXJ-ZIjXF7tGN_Bdre2M076o54K85b3he95JSgeJtxhVW--2wHd5nlU-aLSFsRSMYjjoR0SncoH5X4D79OVa4y0qPAH4OC1ff0EVhlis94pA_AXRYyHZV0CUiJNh_68dScDGGyC0DE20IrIEXdXOwapz3DqO-OLEjELkJYPLnJokPAkrWTfHhKTB7ZClNfLUvNYPLYG-ngAAAAE_rViZAA"
STRING2 = STRING3 = STRING4 = STRING5 = STRING6 = STRING7 = None

SPOTIFY_CLIENT_ID = "1c21247d714244ddbb09925dac565aed"
SPOTIFY_CLIENT_SECRET = "709e1a2969664491b58200860623ef19"

UPSTREAM_REPO = "https://github.com/Ishatgrepo/honeymusic1"
UPSTREAM_BRANCH = "main"
GIT_TOKEN = ""

HEROKU_API_KEY = None
HEROKU_APP_NAME = None

PLAYLIST_FETCH_LIMIT = 25
SERVER_PLAYLIST_LIMIT = 300

START_IMG_URL = "https://graph.org/file/1df484ee2b80ec2e2bd2e.jpg"
PING_IMG_URL = "https://graph.org/file/0dfcbd2935f41b21af907.jpg"

PLAYLIST_IMG_URL = STATS_IMG_URL = TELEGRAM_AUDIO_URL = TELEGRAM_VIDEO_URL = STREAM_IMG_URL = SOUNCLOUD_IMG_URL = YOUTUBE_IMG_URL = SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e02fcc6bbfa0a882d6c8b.jpg"

# -------- RUNTIME LOGIC -------- #
def time_to_seconds(time):
    return sum(int(x) * 60**i for i, x in enumerate(reversed(str(time).split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
    )

# -------- GLOBAL DICTS FOR FEATURES -------- #
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
