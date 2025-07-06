from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from db import tg 
from config import LG_C

@Client.on_message(filters.command("start"))
async def s_command(client, message):
  if await tg.get_user(message.from_user.id) is None:
        await tg.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LG_C, text="#New_User\n\nUser: {}ID: {}".format(message.from_user.mention, message.from_user.id))
  s_m = (
    "Hello there! I'm a advance bot create by @The_TGguy"
  )
  await message.reply_text(s_m)


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "Send any text to echo it back!"
    )
    await message.reply_text(help_text)
