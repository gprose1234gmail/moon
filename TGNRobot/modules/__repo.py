import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/52b1b195f0d7df5ff79b2.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [ALAN WALKER](t.me/alpha_romeo_06) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @missharelyluna «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ RECENT🔥", url=f"https://t.me/thecoolmoon"),
        InlineKeyboardButton(" JOIN 💫", url=f"https://t.me/theunstoppablesquadhang381"),
      ],[
        InlineKeyboardButton("moon ❣️", url="https://t.me/MISSHARELYLUNA"),
        InlineKeyboardButton("SUPPORT ⚡", url="https://t.me/luna_officials"),
      ],[
        InlineKeyboardButton("⚡ UPDATE ☑️", url="https://t.me/lunasupportz"),
        InlineKeyboardButton("GROUP ➡️", url="https://t.me/tamilchating_fed"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
