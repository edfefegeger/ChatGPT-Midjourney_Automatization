import logging

# Конфигурация логгера
logging.basicConfig(filename='LOGS.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    if 'ошибка' in formatted_message or 'Ошибка' in formatted_message or 'Error' in formatted_message:
        logging.error(formatted_message)  # Запись в файл журнала
        print(formatted_message)  # Вывод на консоль
    else:
        logging.info(formatted_message)  # Запись в файл журнала
        print(formatted_message)  # Вывод на консоль
