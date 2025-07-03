import logging
import logging.config
from pyrogram import Client 
from config import BT, API_ID, API_HASH

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

Nectar = Client("Telegram-Guy",api_id=API_ID,api_hash=API_HASH,bot_token=BT)
