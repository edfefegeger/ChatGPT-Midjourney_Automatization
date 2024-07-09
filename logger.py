import logging
import telebot
from telebot import types
TELEGRAM_BOT_TOKEN = '7122429695:AAEUBZ8vWdCf8JQnSjU80f63tijwl4CUj18'

# Ваш chat_id, куда будут отправляться сообщения об ошибках
CHAT_ID = '441882529'
CHAT_ID2 = '441882529'
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

    if 'Всего успешно обработано файлов GPT:' in formatted_message:
        logging.info(formatted_message)
        print(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)
            
    if 'Обработка подпапки' in formatted_message:
        logging.info(formatted_message)
        print(formatted_message)
        bot.send_message(CHAT_ID, formatted_message)
        if CHAT_ID2!= CHAT_ID:
            bot.send_message(CHAT_ID2, formatted_message)

    else:
        logging.info(formatted_message)
        print(formatted_message)
