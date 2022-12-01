import os
import telegram
from telegram import Bot
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from dotenv import load_dotenv
from parser import search_in_wb, find_item_in_page


load_dotenv()

auth_token = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=auth_token)
updater = Updater(token=auth_token)

chat_id = 995177

text = 'Пришлите сообщение вида: <артикул>  <ключевые слова для поиска>'
bot.send_message(chat_id, text) 

def get_article_and_words(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    text_message = update['message']['text']
    article = text_message.split(sep = ' ', maxsplit = 1)[0]
    search_words = text_message.split(sep = ' ', maxsplit = 1)[1]
    search_in_wb(search_words)
    index = find_item_in_page(article)
    # try:
    #     index = article_list.index(article)
    # except ValueError:
    #     index = -1
    context.bot.send_message(chat_id=chat.id, text=index)


updater.dispatcher.add_handler(MessageHandler(Filters.text, get_article_and_words))
updater.start_polling()
updater.idle() 