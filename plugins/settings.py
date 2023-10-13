"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('settings'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("✆ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ ✆",callback_data = "upgrade")], 
        			[InlineKeyboardButton("✎  ᴄᴀᴩᴛɪᴏɴ",callback_data = "kingppt"),
        			InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ ⟲ ",callback_data = "kingmahip")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["settings"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("✆ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ ✆",callback_data = "upgrade")], 
        			[InlineKeyboardButton("✎  ᴄᴀᴩᴛɪᴏɴ",callback_data = "kingppt"),
        			InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ ⟲ ",callback_data = "kingmahip")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
