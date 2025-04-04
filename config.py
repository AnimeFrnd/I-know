import os
import logging
from logging.handlers import RotatingFileHandler

settings = {
    '_id': 1,  # don't change this line only, if you do you're dying by my hand
    "SPOILER": True,  # bool write True or False
    "FILE_AUTO_DELETE": 3600,  # in seconds
    "AUTO_DEL": True,  # bool write True or False
    "STICKER_ID": "CAACAgUAAxkBAAKVWGfW0Ubsz9f61_TZp-6Cm-KS0fTfAAKwFAACMgABqFaj6u1vyYYMpx4E",
    "stk_del_timer": 1, # in seconds
    "bot_admin": [6081617163] #e.g. 1963929292,38739292827 differetiate admins with a comma
}

HELP_MSG = """■ 𝗛𝗲𝗹𝗹𝗼, 𝗔𝗱𝗺𝗶𝗻𝘀!\n\n<blockquote expandable><b>ɴᴇᴇᴅ ʜᴇʟᴘ? ɪᴛ’s sɪᴍᴘʟᴇ: ᴊᴜsᴛ ᴋɴᴏᴄᴋ ᴏɴ <i> 𝐀ʀʏᴀ </i> ᴅᴏᴏʀ (ᴛʜᴀᴛ’s ᴍᴇ, ʙʏ ᴛʜᴇ ᴡᴀʏ). 🙋‍♂️ ᴡʜᴀᴛᴇᴠᴇʀ ɪᴛ ɪs—ǫᴜᴇsᴛɪᴏɴs, ᴄᴏɴᴄᴇʀɴs, ᴇxɪsᴛᴇɴᴛɪᴀʟ ᴄʀɪsᴇs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ʙᴏᴛ—ᴊᴜsᴛ ᴀsᴋ.</b></blockquote>\n\n<blockquote expandable><b>ᴡʜʏ ɪs ᴛʜɪs ᴍᴇssᴀɢᴇ sᴏ sʜᴏʀᴛ? ʙᴇᴄᴀᴜsᴇ ᴛʜɪs ʙᴏᴛ ʜᴀs ᴀʟʀᴇᴀᴅʏ ᴄᴏɴsᴜᴍᴇᴅ ᴀ ʀɪᴅɪᴄᴜʟᴏᴜs ᴀᴍᴏᴜɴᴛ ᴏғ ᴍʏ ᴛɪᴍᴇ, ᴀɴᴅ ɪ’ᴍ ɴᴏᴛ ɪɴ ᴛʜᴇ ᴍᴏᴏᴅ ᴛᴏ ᴡʀɪᴛᴇ ᴀ ɴᴏᴠᴇʟ ʜᴇʀᴇ. 🤷‍♂️ sᴏ, ʏᴇᴀʜ, ʀᴇᴀᴄʜ ᴏᴜᴛ, ᴀɴᴅ ɪ’ʟʟ sᴏʀᴛ ɪᴛ ᴏᴜᴛ.</b></blockquote>\n\n<blockquote><b>ɴᴏᴡ ɢᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴏsᴇ ʟɪɴᴋs ʟɪᴋᴇ ᴛʜᴇ ʀᴏᴄᴋsᴛᴀʀ ᴀᴅᴍɪɴ ʏᴏᴜ ᴀʀᴇ! 💪</b></blockquote>
"""  # shown only to admins

# Bot token @Botfather
TG_BOT_TOKEN = '7093426015:AAFSbuLahFRZ6jvDC1EC4y6BiVpCMcQhPjM'
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7515868"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")

# Your db channel Id
DB_CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002292066966"))

# NAME OF OWNER
OWNER = os.environ.get("OWNER", "𝐀ʀʏᴀ")

# OWNER ID
OWNER_ID = 6081617163

# SUDO: those who can edit admins in channel
SUDO = [6081617163]
if OWNER_ID not in SUDO:
    SUDO.append(OWNER_ID)

# Port
PORT = os.environ.get("PORT", "8108")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://animefrnd44:OEgLPjMjrAKR46kE@cluster0.arcfjym.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "AnimeMonarch")

# FSUBS configuration
FSUBS = [
    {'_id': -1002129412433, "CHANNEL_NAME": "Oɴɢᴏɪɴɢ Aɴɪᴍᴇ ❄"},
]


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>Hᴇʏ, {mention}✌🏻.  I ʜᴏᴘᴇ ʏᴏᴜ'ʀᴇ ғᴇᴇʟɪɴɢ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ 𝐒ʜᴀᴅᴏᴡ Mᴏɴᴀʀᴄʜ 😈.</b></blockquote>\n\n<blockquote expandable><b>I'ᴍ 𝐓ʜᴇ Uʟᴛɪᴍᴀᴛᴇ Fɪʟᴇ Sʜᴀʀɪɴɢ Bᴏᴛ, ʙᴜɪʟᴛ ᴛᴏ ʀᴜʟᴇ ᴛʜᴇ 𝐒ʜᴀᴅᴏᴡ Rᴇᴀʟᴍ 🖤\n\n‣ 🔱 Sᴛᴏʀᴇ & Sʜᴀʀᴇ Fɪʟᴇs ᴡɪᴛʜ ᴀ Sɪɴɢʟᴇ Cʟɪᴄᴋ.\n‣ 🛡️ Iɴꜰɪɴɪᴛᴇ Fɪʟᴇ Mᴀɴᴀɢᴇᴍᴇɴᴛ Sʏꜱᴛᴇᴍ.\n‣ 📂 Pᴏsᴛ Fɪʟᴇs ɪɴ 𝐀ɴɪᴍᴇ Mᴏɴᴀʀᴄʜ 👑 Tᴇᴍᴘʟᴀᴛᴇ.\n\n 𝐍ᴏᴡ, 𝐓ʜᴇ Fɪʟᴇ Rᴇᴀʟᴍ Iꜱ Uɴᴅᴇʀ Mʏ Cᴏɴᴛʀᴏʟ 😈.\n\n𝐀ʀᴇ Yᴏᴜ Rᴇᴀᴅʏ ᴛᴏ Dᴏᴍɪɴᴀᴛᴇ, {mention}-Sᴀᴍᴀ? 👑</b></blockquote>")
ADMINS = [6081617163]
# Add other admin IDs here as needed, ensuring not to include OWNER_ID
other_admin_ids = [6081617163]  # Replace with actual admin IDs
for admin_id in other_admin_ids:
    if admin_id != OWNER_ID:
        ADMINS.append(admin_id)

# Ensure OWNER_ID is not duplicated
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = '<blockquote expandable><b>{previouscaption}</b></blockquote>'

# Set True if you want to prevent users from forwarding files from the bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want to disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = True  # True or None

BOT_STATS_TEXT = "<blockquote><b>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
