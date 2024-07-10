import datetime
import time
import openai
import os
import base64
import configparser
from PIL import Image
from tkinter import filedialog, Tk  # Импортируем необходимые модули из tkinter
import keyboard
import http.client
import json
import pprint
import urllib.request
import threading
from logger import log_and_print
from pause import toggle_pause, toggle_pause2, pause_check, pause_for_two_hours
from sep_files import separate_files

current_api_key_index = 0
current_midjourney_key_index = 0
txt_couner = 1
log_and_print("Запуск программы")

now = datetime.datetime.now()
# Форматируем дату и время в строку
file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

file_date = now.strftime("%Y-%m-%d_%H-%M-%S")
# Путь к файлу в корне проекта
file_path = os.path.join(os.getcwd(), file_name)






# Чтение API-ключей из файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')
api_key1 = config['API']['api_key']
api_key2 = config['API']['api_key2']
api_key3 = config['API']['api_key3']
api_key4 = config['API']['api_key4']
api_key5 = config['API']['api_key5']

all_api_keys = [
    config['API']['api_key'],
    config['API']['api_key2'],
    config['API']['api_key3'],
    config['API']['api_key4'],
    config['API']['api_key5']
]

api_keys = [key for key in all_api_keys if key]

# Если список пуст, выходим из программы
if not api_keys:
    log_and_print("Ошибка. Нет доступных API-ключей. Программа завершает работу.")
    exit()

promt = config['API']['promt']
detail = config['API']['detail']
attempts_max = int(config['API']['max_attempts'])
max_tokens = int(config['API']['max_tokens'])
temp = int(config['API']['temp'])
model = config['API']['model']

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

print("Выберите 'Общую' папку с вашими изображениями", "\n")
# Путь к папке с изображениями
# Предложите пользователю выбрать директорию
folder_path = filedialog.askdirectory(title="Выберите 'Общую' папку с изображениями")

# Если папка не выбрана, завершите программу
if not folder_path:
    log_and_print("Ошибка. Папка не выбрана. Программа завершает работу.")
    exit()

def get_current_api_key():
    return api_keys[current_api_key_index]

# Получите список всех папок в выбранной директории
subdirectories = [os.path.join(folder_path, d) for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

def process_images(files, subdir):
    global current_api_key_index
    global current_midjourney_key_index
    global paused
    global sorted_image_files
    global num_successful_files  # Объявляем счетчик как глобальную переменную
    global txt_couner  # Объявляем txt_couner как глобальную переменную

    for image_file in files:
        attempts = 0
        api_key = get_current_api_key()
        # Определяем, какой ключ использовать для текущего файла
        file_count = f"Ключ {current_api_key_index + 1}"
        midjourney_key_count = f"Ключ {current_midjourney_key_index + 1}"
        # Увеличиваем индекс для следующего использования ключа
        current_api_key_index = (current_api_key_index + 1) % len(api_keys)
        # Установка ключа API
        openai.api_key = api_key
        # Цикл для обработки запросов с обработкой ошибок и ограничений
        while attempts < attempts_max:
            try:
                # Формируем полный путь к файлу
                image_path = os.path.join(folder_path, subdir, image_file)

                # Кодируем изображение в формат Base64
                base64_image = encode_image(image_path)
                pause_check()
                # Отправляем запрос к OpenAI API с изображением в формате Base64
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": promt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{base64_image}",
                                        "detail": detail,
                                        "temp": temp,
                                        "max_tokens": max_tokens
                                    }
                                }
                            ]
                        }
                    ]
                )
                # Получаем текстовый ответ от GPT
                gpt_response = response.choices[0]["message"]["content"].rstrip(".")


                # Разбиваем ответ на параграфы
                paragraphs = gpt_response.split("\n\n")
                if "--ar 16:9" not in gpt_response:
                    # Если не соответствует, повторяем запрос
                    log_and_print("Ошибка формата ответа с --ar 16:9 . Повторный запрос.", "(Ключ GPT: ", file_count,")")
                    attempts += 1
                    continue

                gpt_answer = {response.choices[0]['message']['content']}
                # Выводим информацию о тегах и названии файла
                log_and_print(f"File: '{image_file}' Обработан c CHAT GPT ключом: {file_count}! \n{response.choices[0]['message']['content']}\n")
                pause_check()
                # Проверяем, сколько параграфов найдено
                if len(paragraphs) >= 1:
                    result_1 = paragraphs[0].rstrip('.')
                    log_and_print("Найден параграф 1", "\n", "(Ключ GPT: ", file_count,")")

                pause_check()

                if len(paragraphs) >= 2:
                    result_2 = paragraphs[1].rstrip('.')
                    log_and_print("Найден параграф 2", "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")", "\n")
                    # data2 = {
                    # "prompt": result_2, }
                    # headers2 = {
                    #     'Authorization': f'Bearer {midjourney_key}',  
                    #     'Content-Type': 'application/json'
                    # }
                    # conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                    # conn.request("POST", "/items/images/", body=json.dumps(data2), headers=headers2)
                    # response2 = conn.getresponse()
                    # response_data2 = json.loads(response2.read().decode('utf-8'))
                    # log_and_print("Промт отправлен в Midjourney (2 параграф)", "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")")
                    # pprint.pp(response_data2)
                    # check_image_status(response_data2)
                pause_check()

                if len(paragraphs) >= 3:
                    result_3 = paragraphs[2].rstrip('.')
                    log_and_print("Найден параграф 3", "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")", "\n")
                    # data3 = {
                    # "prompt": result_3, }
                    # headers3 = {
                    #     'Authorization': f'Bearer {midjourney_key}',  # <<<< TODO: remember to change this
                    #     'Content-Type': 'application/json'
                    # }
                    # conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                    # conn.request("POST", "/items/images/", body=json.dumps(data3), headers=headers3)
                    # response3 = conn.getresponse()
                    # response_data3 = json.loads(response3.read().decode('utf-8'))
                    # log_and_print("Промт отправлен в Midjourney (3 параграф)", "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")")
                    # pprint.pp(response_data3)
                    # check_image_status(response_data3)
                pause_check()



                log_and_print(f"File: '{image_file}' Обработан ключом: {midjourney_key_count}!", "\n")
                print("---------------------------------------")
            except Exception as e:
                if str(e) == "'data'":
                    log_and_print(f"Пропущен файл {image_file} из-за ошибки: {e}", "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")")
                    break  # Переходим к следующему файлу
                else:
                    log_and_print("Ошибка при обработке файла:", e, "(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")")
                    attempts += 1
                    continue
            except openai.error.APIError as e:
                if "You’ve reached the current usage cap for GPT-4" in str(e):
                    pause_for_two_hours()
                    continue

            with open(file_path, 'a') as file:
                    file.write(f"{txt_couner}. {gpt_response}\n \n")
                    txt_couner += 1

            num_successful_files += 1
            pause_check()
            break
        if attempts == attempts_max:
            log_and_print(f"Достигнуто максимальное количество попыток ({attempts_max}) для файла {image_file}. Переходим к следующему файлу.", "\n","(Ключ GPT: ", file_count, "Ключ Midjounrey: ", midjourney_key_count,")", "\n")
# Перебирайте каждую подпапку и обрабатывайте изображения


all_files = os.listdir(folder_path)
lock = threading.Lock()
numeric_files, text_files = separate_files(all_files)
sorted_numeric_files = sorted(numeric_files, key=lambda x: int(x.split('.')[0]))
sorted_text_files = sorted(text_files)
sorted_image_files = sorted_numeric_files + sorted_text_files

sorted_image_files = sorted_numeric_files + sorted_text_files
print("Для постановки на паузу нажмите '-', для снятие с паузы '+'")
print("Ваш запрос:", promt, "\n")

result_1 = ""
result_2 = ""
result_3 = ""



num_threads = 5  # Задаем количество потоков
chunk_size = len(sorted_image_files) // num_threads  # Вычисляем размер каждой части
if chunk_size == 0:
    chunk_size = 1  # Минимальный размер части
file_chunks = [sorted_image_files[i:i + chunk_size] for i in range(0, len(sorted_image_files), chunk_size)]

global num_successful_files

num_successful_files = 0
# Создаем и запускаем потоки
all_files = []
for subdir in subdirectories:
    all_files.extend(os.listdir(subdir))

# Разделите файлы на части для каждой папки
file_chunks_per_folder = {}
# Создайте список подпапок для обработки
subdirectories = [os.path.join(folder_path, d) for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

def log_processed_folder(folder_name):
    log_and_print(f"Обработка подпапки '{folder_name}' завершена.")

keyboard.add_hotkey('-', lambda: toggle_pause(threads))

keyboard.add_hotkey('+', toggle_pause2)

# Для каждой подпапки обработайте файлы
for subdir in subdirectories:
    # Получите список файлов в текущей подпапке
    all_files = os.listdir(subdir)
    numeric_files, text_files = separate_files(all_files)
    sorted_numeric_files = sorted(numeric_files, key=lambda x: int(x.split('.')[0]))
    sorted_text_files = sorted(text_files)
    sorted_image_files = sorted_numeric_files + sorted_text_files
    
    # Разделите файлы на части для каждой подпапки
    chunk_size = len(sorted_image_files) // num_threads
    if chunk_size == 0:
        chunk_size = 1
    file_chunks = [sorted_image_files[i:i + chunk_size] for i in range(0, len(sorted_image_files), chunk_size)]
    
    # Создайте и запустите потоки для обработки файлов из текущей подпапки
    threads = []
    for chunk in file_chunks:
        thread = threading.Thread(target=process_images, args=(chunk, subdir))
        thread.start()
        threads.append(thread)
    
    # Дождитесь завершения всех потоков перед переходом к следующей подпапке
    for thread in threads:
        thread.join()

    log_processed_folder(os.path.basename(subdir))

# Новое имя файла
new_file_name = file_date + '_' + str(num_successful_files) + '.txt'

# Путь к новому файлу в той же директории
new_file_path = os.path.join(os.getcwd(), new_file_name)

# Переименовываем файл
os.rename(file_path, new_file_path)

# После обработки всех подпапок выведите сообщение о завершении
log_and_print("Конец. Все файлы успешно обработаны!")

log_and_print("Всего успешно обработано файлов GPT:", num_successful_files)
input("Для выхода нажмите Enter...")
