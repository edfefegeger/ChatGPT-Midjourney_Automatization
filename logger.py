import logging
import telebot
from telebot import types
TELEGRAM_BOT_TOKEN = '7065557253:AAGZresPiOWD8uBNDDnbuV0sSthdEvt5FsY'

# Ваш chat_id, куда будут отправляться сообщения об ошибках
CHAT_ID = '811079407'
CHAT_ID2 = '783897764'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
# Конфигурация логгера
logging.basicConfig(filename='LOGS.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    if 'ошибка' in formatted_message or 'Ошибка' in formatted_message or 'Error' in formatted_message:
        logging.error(formatted_message)
        print(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)

    if 'Конец' in formatted_message:
        logging.info(formatted_message)
        print(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)

    if 'Запуск' in formatted_message:
        logging.info(formatted_message)
        print(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)

    else:
        logging.info(formatted_message)
        print(formatted_message)
