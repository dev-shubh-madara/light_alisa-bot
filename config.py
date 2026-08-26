# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "sasuke_qt")
BOT_USERNAME = getenv("BOT_USERNAME", "MikasaMusicRobot")
BOT_NAME = getenv("BOT_NAME", "Alisa")
ASSUSERNAME = getenv("ASSUSERNAME", "Aiused")


# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", None))
OWNER_ID = int(getenv("OWNER_ID", 8762430892))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ragini19854-prog/light_alisa-bot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_ABOUT_SASUKE_ll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AnimeWorld_pfp")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))


# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Debugging
DEBUG_IGNORE_LOG = getenv("DEBUG_IGNORE_LOG", "False").lower() == "true"

# Additional group/channel IDs
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", getenv("LOGGER_ID", "0")))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", SUPPORT_CHAT)

# Image URLs
SHASHANK_IMG = getenv("SHASHANK_IMG", "https://h.uguu.se/rbricwLU.jpg").split(",") if "," in getenv("SHASHANK_IMG", "https://h.uguu.se/QaXTztiw.jpg") else [getenv("SHASHANK_IMG", "https://h.uguu.se/AQYquknW.jpg")]

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/5go4t6.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ohezme.jpg")
PLAYLIST_IMG_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
STATS_IMG_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
TELEGRAM_AUDIO_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
TELEGRAM_VIDEO_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
STREAM_IMG_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
YOUTUBE_IMG_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
SPOTIFY_ARTIST_IMG_URL = "https://image.zaw-myo.workers.dev/image/fd0887f6-d2dc-41c6-9f6c-05c62f8928c6"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ohezme.jpg"


# Helper function
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://"
    )

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://"
    )
