#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("20906636", default=None, cast=int)
API_HASH = config("5b018a376badfd32a45ef92cc3af9aca", default=None)
BOT_TOKEN = config("7034268835:AAHjwgROSgipCvFmr5rwF-U0HhZuHzFz9Kc", default=None)
SESSION = config("1BJWap1sBu0T1R7hm-11Bz2d_4nrTpRr6bL_lUhBDyVtFmRqQTdZMeRx7r6qEGHd1-zHb1bgh0-zBFFRKezijQrUOaEsICXQucChxo_-Qo8_tDQfIOhrOEI0gpZ7QG77Qq8b9BnckU3NBmpXfaWv8X5WK0X4sWEsNJqZToE53F6wQ3EYwJm06ZeBrIaCvJN_Mro2yOIx2MG50PijKR4eVKrbJK5RcK0yK_m2M1wILcTKdk1ADItlDqdpVPn-1loU5IjdQkZPRjLc0qeW6Elb6AbBZoJf-rPY_Te37nwC4bvD3kKuNfsr5jBnC0v4rTJ9za1nZVwi96fPyHTo3SYPZd1-IPs9Ewwg=", default=None)
FORCESUB = config("CCLoadedBot", default=None)
AUTH = config("6038063445", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
