import asyncio
import random
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




DARK_IMG = (
https://telegra.ph/file/f0f501107bff1ddb8a109.jpg






START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(DARK_IMG),
        caption=f"""**━━━━━━━━━━━━━━━━━
ʜᴇʏ ʙᴀʙʏ, 🖤
    ᴛʜɪs ɪs ᴅᴀʀʟᴢᴢ ★ ᴍᴜsɪᴄ​ 🥀

๏ ᴅᴀʀʟᴢᴢ ᴍᴜꜱɪᴄꜱ ᴡɪʟʟ ᴘʟᴀʏ ʟᴀɢ ғʀᴇᴇ
ᴍusɪᴄ  ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ
ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs.
━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🛟 sᴜᴘᴘᴏʀᴛ", url="https://t.me/vanakkamda_mapla"),
            InlineKeyboardButton("🌾 ᴏᴡɴᴇʀ", url="https://t.me/kassim_darlzzz")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎃 ᴍᴏʀᴇ ɪɴғᴏ", callback_data="more_info")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        random.choice(DARK_IMG),
        caption=f"""ʏᴏᴜ ᴋɴᴏᴡ ɪ ᴀᴍ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. """,
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="🛟 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/vanakkamda_mapla"),
                InlineKeyboardButton(text="🎃 ᴏᴡɴᴇʀ", url=f"https://t.me/kassim_darlzzz"),
            ]
        ]
     ),
  ) 

@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    sumit = await message.reply_photo(
        random.choice(DARK_IMG),
        caption="ᴩɪɴɢɪɴɢ...",
    )
    await sumit.edit_text(
        f"""𝗣 𝗢 𝗡 𝗚 🎉 !! \n `{delta_ping * 1000:.3f} ᴍs`""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="🛟 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/vanakkamda_mapla"),
                InlineKeyboardButton(text="🎃 ᴏᴡɴᴇʀ", url=f"https://t.me/kassim_darlzzz"),
            ],
            [
                InlineKeyboardButton(text="🎓 ᴅᴇᴠᴇᴏᴘᴇʀ", url=f"https://t.me/kassim_darlzzz"),
            ]
        ]
     ),
  ) 

