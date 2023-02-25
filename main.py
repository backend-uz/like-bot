from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
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
    bot.send_message(chat_id, f"LIKE:{like}  DISLIKE:{dislike}", reply_markup=keyboard)

def count_like_dislike(update, context):
    bot = context.bot

    chat_id = update.message.chat.id
    text = update.message.text

    if text[0] == "\U0001F44D":
        user_data = likeDB.add_like(str(chat_id))
    
    elif text[0] == "\U0001F44E":
        user_data = likeDB.add_dislike(str(chat_id))

    like = user_data['like']
    dislike = user_data['dislike']
    btn1 = KeyboardButton(text=f'\U0001F44D {like}')
    btn2 = KeyboardButton(text=f'\U0001F44E {dislike}')

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]])
    bot.send_message(chat_id, f"LIKE:{like}  DISLIKE:{dislike}", reply_markup=keyboard)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, count_like_dislike))

updater.start_polling()
updater.idle()
