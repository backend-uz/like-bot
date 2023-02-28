from telegram import (
    Update, 
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup)
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import os 
from db import LikeDB

TOKEN=os.environ.get('TOKEN')

likeDB = LikeDB('data.json')

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    user_data = likeDB.add_student(str(chat_id))
    like = user_data['like']
    dislike = user_data['dislike']
    btn1 = KeyboardButton(text=f'\U0001F44D {like}')
    btn2 = KeyboardButton(text=f'\U0001F44E {dislike}')
    keyboard = ReplyKeyboardMarkup([[btn1, btn2]])
    bot.send_message(chat_id, "Send me a photo")

def simpletext(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, "send me a command only)")

# def count_like_dislike(update, context):
#     bot = context.bot
#     chat_id = update.message.chat.id
#     text = update.message.text
#     if text[0] == "\U0001F44D":
#         user_data = likeDB.add_like(str(chat_id))
    
#     elif text[0] == "\U0001F44E":
#         user_data = likeDB.add_dislike(str(chat_id))

#     like = user_data['like']
#     dislike = user_data['dislike']
#     btn1 = KeyboardButton(text=f'\U0001F44D {like}')
#     btn2 = KeyboardButton(text=f'\U0001F44E {dislike}')
#     keyboard = ReplyKeyboardMarkup([[btn1, btn2]])
#     bot.send_message(chat_id, f"LIKE:{like}  DISLIKE:{dislike}", reply_markup=keyboard)

def photo(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    like = likeDB.all_dislikes(str(chat_id))
    dislike = likeDB.all_dislikes(str(chat_id))
    photo = update.message.photo[-1]["file_id"]
    button1 = InlineKeyboardButton(text = f"👍 {like}", callback_data="like")
    button2 = InlineKeyboardButton(text = f"👎 {dislike}", callback_data="dislike")
    keyboard = InlineKeyboardMarkup([[button1, button2]])
    bot.sendPhoto(chat_id=chat_id, photo=photo, reply_markup=keyboard)

def like_and_dislike(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data
    
    if data == "like":
        user_data = likeDB.add_like(str(chat_id))
    elif data == "dislike":
        user_data = likeDB.add_dislike(str(chat_id))
    like = user_data['like']
    dislike = user_data['dislike']
    button1 = InlineKeyboardButton(text = f"👍 {like}", callback_data="like")
    button2 = InlineKeyboardButton(text = f"👎 {dislike}", callback_data="dislike")
    keyboard = InlineKeyboardMarkup([[button1, button2]])
    query.answer(text='ishladi', show_alert=True)
    query.edit_message_reply_markup(reply_markup=keyboard)
updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, simpletext))
dp.add_handler(MessageHandler(Filters.photo, photo))
dp.add_handler(CallbackQueryHandler(like_and_dislike))

updater.start_polling()
updater.idle()
