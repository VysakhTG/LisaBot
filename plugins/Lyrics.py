from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.command("lyrics"))
async def lyrics(client, message):
    searchlyrics = message.text.split(" ", 1)
    if len(searchlyrics) == 1:
        message.reply_text("Usage:\n/lyrics [lyrics]") 
        return
    else:
        searchlyrics = searchlyrics[1]
        m = await message.reply_text("Searching...") 
        try:
          await mee.delete()
          await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/xd_botz")]]))
        except Exception as e:                            
             await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/xd_botz")]]))



def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made By Artificial Intelligence**'
        return text
