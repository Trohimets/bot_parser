import os
import telegram
from telegram import Bot
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from dotenv import load_dotenv

load_dotenv()

# 5002789883:AAHyYXw4E7ayfpRYbQhQbs5ZfplmX306o-4

auth_token = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=auth_token)
updater = Updater(token=auth_token)

chat_id = 995177

text = 'Вам телеграмма!'
bot.send_message(chat_id, text) 

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, пришли мне название и артикул товара!')

def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что включили меня')

# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle() 