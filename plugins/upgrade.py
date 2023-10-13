"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """ **🏷 ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ** :- ```Free```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```2.0 GB```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```5 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```1```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```Life Time```

**ꜱᴩᴇᴇᴅ ᴅᴇᴩᴇɴᴅ ʏᴏᴜʀ ᴅᴄ ɪᴅ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🎗️ ʙʀᴏɴᴢᴇ",callback_data = "32jlt4"), InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏅 ᴩʟᴀᴛɪᴜᴍ",callback_data = "gdrsyne"), InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """ **🏷 ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ** :- ```Free```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```2.0 GB```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```5 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```1```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```Life Time```

**ꜱᴩᴇᴇᴅ ᴅᴇᴩᴇɴᴅ ʏᴏᴜʀ ᴅᴄ ɪᴅ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🎗️ ʙʀᴏɴᴢᴇ",callback_data = "32jlt4"), InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏅 ᴩʟᴀᴛɪᴜᴍ",callback_data = "gdrsyne"), InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
