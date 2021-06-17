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
    pic_url = "https://drive.google.com/file/d/1DmfpdV43PHg5sRyP3yrIrAcfs_T_rvZi/view?usp=drivesdk"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Konnichiwa senpai!

Please read all the instructions about the bot before surfing on...

See /whats_new to know about latest updates...""", reply_markup=reply_markup, parse_mode="markdown")
