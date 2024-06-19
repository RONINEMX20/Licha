from gpytranslate import SyncTranslator
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from AvishaRobot import pbot as app
from AvishaRobot import dispatcher
from pyrogram.types import *
from AvishaRobot.modules.disable import DisableAbleCommandHandler
from pyrogram.types import InputMediaVideo
import random
trans = SyncTranslator()


def totranslate(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    reply_msg = message.reply_to_message
    if not reply_msg:
        message.reply_text(
            "⬤ ᴜsᴇ ➥ `/tl en` ғᴏʀ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴅᴇᴛᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪᴛ ɪɴᴛᴏ ᴇɴɢʟɪsʜ.",
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"❖ <b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> ➥\n\n"
        f"♥︎ {translation.text}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ʟ ɪ c ʜ ᴀ ࿐"
    )

    message.reply_text(reply, parse_mode=ParseMode.HTML)


TRANSLATE_HANDLER = DisableAbleCommandHandler(["tl"], totranslate, run_async=True)

dispatcher.add_handler(TRANSLATE_HANDLER)

__command_list__ = ["tl"]
__handlers__ = [TRANSLATE_HANDLER]

#####

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AvishaRobot import OWNER_ID, dispatcher
from AvishaRobot import pbot as client

AVISHA = "https://graph.org/file/dcc62e53435a919373a0a.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=AVISHA,
        caption=f"""❖ ʜᴇʏ {message.from_user.mention()}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ♥︎\n\n⬤ ɪғ ʏᴏᴜ ᴡᴀɴᴛ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ",user_id=OWNER_ID
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ",
                        callback_data="gib_source",
                    ),
                ]
            ]
        ),
    )


@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/ba8d2f578ca9e95f200b6.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [close_button]
            ]
        ),
        )
close_button = InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")

@app.on_callback_query(filters.regex("close"))
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return

