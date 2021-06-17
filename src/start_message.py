# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://drive.google.com/file/d/1E0NVETNx4NjaIv4zjiLB971i_Vzzx9pL/view?usp=drivesdk"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Konnichiwa senpai!

Start searching anime by /search""", reply_markup=reply_markup, parse_mode="markdown")
