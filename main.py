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

# Чтение API-ключей из файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')
api_key1 = config['API']['api_key']
api_key2 = config['API']['api_key2']
api_key3 = config['API']['api_key3']
api_key4 = config['API']['api_key4']
api_key5 = config['API']['api_key5']
api_key_midjorney = config['API']['api_key_midjourney']
api_key_midjorney2 = config['API']['api_key_midjourney2']
api_key_midjorney3 = config['API']['api_key_midjourney3']
api_key_midjorney4 = config['API']['api_key_midjourney4']
api_key_midjorney5 = config['API']['api_key_midjourney5']
api_key_midjorney6 = config['API']['api_key_midjourney6']
api_key_midjorney7 = config['API']['api_key_midjourney7']
api_key_midjorney8 = config['API']['api_key_midjourney8']
api_key_midjorney9 = config['API']['api_key_midjourney9']
api_key_midjorney10 = config['API']['api_key_midjourney10']

promt = config['API']['promt']
detail = config['API']['detail']
attempts_max = int(config['API']['max_attempts'])
max_tokens = int(config['API']['max_tokens'])
temp = int(config['API']['temp'])
model = config['API']['model']

# Функция для кодирования изображения в формат Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Функция для приостановки работы программы на два часа при превышении лимита запросов
def pause_for_two_hours():
    print("Превышен лимит запросов. Остановка работы на два часа.")
    time.sleep(7200)  # 7200 секунд = 2 часа

print("Выберите папку с вашими изображениями")
# Путь к папке с изображениями
folder_path = filedialog.askdirectory(title="Выберите папку с изображениями")

# Если пользователь не выбрал папку, завершаем программу
if not folder_path:
    print("Папка не выбрана. Программа завершает работу.")
    exit()

# Получаем список файлов в порядке их имени, учитывая числовой порядок
image_files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))

print("Ваш запрос:", promt, "\n")

# Переменные для хранения результатов обработки изображений
result_1 = ""
result_2 = ""
result_3 = ""

# Список всех API-ключей
api_keys = [api_key1, api_key2, api_key3, api_key4, api_key5]

midjourney_api_keys = [
    api_key_midjorney,
    api_key_midjorney2,
    api_key_midjorney3,
    api_key_midjorney4,
    api_key_midjorney5,
    api_key_midjorney6,
    api_key_midjorney7,
    api_key_midjorney8,
    api_key_midjorney9,
    api_key_midjorney10
]

# Индекс текущего используемого ключа API
current_api_key_index = 0
current_midjourney_key_index = 0
# Функция для получения текущего ключа API
def get_current_api_key():
    return api_keys[current_api_key_index]
def get_current_midjourney_key():
    return midjourney_api_keys[current_midjourney_key_index]

# Функция для обработки нажатия клавиши "-"
# def on_pause():
#     global paused
#     if not paused:
#         paused = True
#         print("Программа поставлена на паузу")

# # Функция для обработки нажатия клавиши "+"
# def on_resume():
#     global paused
#     if paused:
#         paused = False
#         print("Программа возобновлена")

# Создаем горячие клавиши для постановки на паузу и возобновления
# keyboard.add_hotkey('-', on_pause)
# keyboard.add_hotkey('+', on_resume)

# Обработка каждого изображения
for image_file in image_files:
    attempts = 0
    
    # Получение текущего ключа API
    api_key = get_current_api_key()
    midjourney_key = get_current_midjourney_key()
    
    # Определяем, какой ключ использовать для текущего файла
    file_count = f"Ключ {current_api_key_index + 1}"
    midjourney_key_count = f"Ключ {current_midjourney_key_index + 1}"
    # Увеличиваем индекс для следующего использования ключа
    current_api_key_index = (current_api_key_index + 1) % len(api_keys)
    current_midjourney_key_index = (current_midjourney_key_index + 1) % len(midjourney_api_keys)

    # Установка ключа API
    openai.api_key = api_key
    
    # Флаг для проверки состояния паузы
    # paused = False
    
    # Цикл для обработки запросов с обработкой ошибок и ограничений
    while attempts < attempts_max:
        try:
            # Формируем полный путь к файлу
            image_path = os.path.join(folder_path, image_file)
            # Кодируем изображение в формат Base64
            base64_image = encode_image(image_path)
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

            if "--ar 16:9" not in gpt_response:
                # Если не соответствует, повторяем запрос
                print("Ошибка формата ответа с --ar 16:9 . Повторный запрос.")
                attempts += 1
                continue


            # Разбиваем ответ на параграфы
            paragraphs = gpt_response.split("\n\n")

            # Выводим информацию о тегах и названии файла
            print(f"File: '{image_file}' Обработан ключом: {file_count}! \n{response.choices[0]['message']['content']}\n")

            # Проверяем, сколько параграфов найдено
            if len(paragraphs) >= 1:
                result_1 = paragraphs[0].rstrip('.')
                print("Найден параграф 1", "\n")
                data1 = {
                    "prompt": result_1
                }
                headers1 = {
                    'Authorization': f'Bearer {midjourney_key}',
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data1), headers=headers1)
            
                response1 = conn.getresponse()
                response_data1 = json.loads(response1.read().decode('utf-8'))
            
                print("Промт отправлен в Midjourney (1 параграф)")
                pprint.pp(response_data1)
            
                def send_request(method, path, body=None, headers={}):
                    conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                    conn.request(method, path, body=json.dumps(body) if body else None, headers=headers)
                    response = conn.getresponse()
                    data = json.loads(response.read().decode())
                    conn.close()
                    return data
                               
                def check_image_status(response_data):
                    max_attempts = 3  # Максимальное количество попыток
                    attempts_mid = 0
                    while attempts_mid < max_attempts:
                        response_data = send_request('GET', f"/items/images/{response_data['data']['id']}", headers=headers1)
                        if response_data['data']['status'] == 'completed':
                            print(f"Статус: {response_data['data']['status']}")
                            print('Завершена обработка от Midjourney', "\n")
                            return True
                        elif response_data['data']['status'] == 'failed':
                            print('Обработка в Midjourney не удалась. Повторная попытка отправки...', "\n")
                            conn.request("POST", "/items/images/", body=json.dumps(data1), headers=headers1)
                            response1 = conn.getresponse()
                            response_data = json.loads(response1.read().decode('utf-8'))
                            attempts_mid += 1
                        else:
                            print(f"Изображение еще не завершило генерацию. Статус: {response_data['data']['status']}")
                            time.sleep(15)
                    print('Достигнуто максимальное количество попыток. Обработка в Midjourney не удалась.', "\n")
                    return False

                
                check_image_status(response_data1)


            if len(paragraphs) >= 1:
                result_1 = paragraphs[0].rstrip('.')
                data1 = {
                    "prompt": result_1
                }
                headers1 = {
                    'Authorization': f'Bearer {midjourney_key}',
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data1), headers=headers1)
            
                response1 = conn.getresponse()
                response_data1 = json.loads(response1.read().decode('utf-8'))
            
                print("Промт отправлен в Midjourney (1 параграф, второй раз)")
                pprint.pp(response_data1)
            
                
                check_image_status(response_data1)

            if len(paragraphs) >= 2:
                result_2 = paragraphs[1].rstrip('.')
                print("Найден параграф 2", "\n")
                data2 = {
                "prompt": result_2, }
                headers2 = {
                    'Authorization': f'Bearer {midjourney_key}',  # <<<< TODO: remember to change this
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data2), headers=headers2)

                response2 = conn.getresponse()
                response_data2 = json.loads(response2.read().decode('utf-8'))

                print("Промт отправлен в Midjourney (2 параграф)")

                pprint.pp(response_data2)

                check_image_status(response_data2)

            if len(paragraphs) >= 2:
                result_2 = paragraphs[1].rstrip('.')
                data2 = {
                "prompt": result_2, }
                headers2 = {
                    'Authorization': f'Bearer {midjourney_key}',  # <<<< TODO: remember to change this
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data2), headers=headers2)

                response2 = conn.getresponse()
                response_data2 = json.loads(response2.read().decode('utf-8'))

                print("Промт отправлен в Midjourney (2 параграф, второй раз)")

                pprint.pp(response_data2)

                check_image_status(response_data2)


            if len(paragraphs) >= 3:
                result_3 = paragraphs[2].rstrip('.')
                print("Найден параграф 3", "\n")
                data3 = {
                "prompt": result_3, }
                headers3 = {
                    'Authorization': f'Bearer {midjourney_key}',  # <<<< TODO: remember to change this
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data3), headers=headers3)

                response3 = conn.getresponse()
                response_data3 = json.loads(response3.read().decode('utf-8'))
                print("Промт отправлен в Midjourney (3 параграф)")
                pprint.pp(response_data3)

                check_image_status(response_data3)

            if len(paragraphs) >= 3:
                result_3 = paragraphs[2].rstrip('.')
                data3 = {
                "prompt": result_3, }
                headers3 = {
                    'Authorization': f'Bearer {midjourney_key}',  # <<<< TODO: remember to change this
                    'Content-Type': 'application/json'
                }
                conn = http.client.HTTPSConnection("cl.imagineapi.dev")
                conn.request("POST", "/items/images/", body=json.dumps(data3), headers=headers3)

                response3 = conn.getresponse()
                response_data3 = json.loads(response3.read().decode('utf-8'))
                print("Промт отправлен в Midjourney (3 параграф, второй раз)")
                pprint.pp(response_data3)

                check_image_status(response_data3)

            else:
                print("Не все параграфы найдены ")
            
            print("---------------------------------------")

        except Exception as e:
            print("Ошибка при обработке файла:", e)
            attempts += 1
            continue

        except openai.error.APIError as e:
            if "You’ve reached the current usage cap for GPT-4" in str(e):
                pause_for_two_hours()
                continue

        break  # Выходим из цикла while, если ответ не содержит запрещенных слов или достигнуто ограничение по попыткам
    # Если после 5 попыток ответ все еще содержит запрещенные слова, переходим к следующему файлу
    if attempts == attempts_max:
        print(f"Достигнуто максимальное количество попыток ({attempts_max}) для файла {image_file}. Переходим к следующему файлу.", "\n")

        
print("Все файлы успешно обработаны!")
input("Для выхода нажмите Enter...")
