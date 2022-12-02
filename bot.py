import os
import logging
from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

from parser import search_in_wb, find_in_all_pages


logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


load_dotenv()

auth_token = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=auth_token)


def get_article_and_words(update, context):
    chat = update.effective_chat
    text_message = update['message']['text']
    article = text_message.split(sep = ' ', maxsplit = 1)[0]
    search_words = text_message.split(sep = ' ', maxsplit = 1)[1]
    search_in_wb(search_words)
    index = find_in_all_pages(article)
    context.bot.send_message(chat_id=chat.id, text=index)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Пришлите сообщение вида: <артикул>  <ключевые слова для поиска>'.format(name)
    )


def main():
    updater = Updater(token=auth_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_article_and_words))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() 