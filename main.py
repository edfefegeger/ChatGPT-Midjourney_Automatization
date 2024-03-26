import time
import openai
import os
import base64
import configparser
from PIL import Image
from tkinter import filedialog, Tk  # Импортируем необходимые модули из tkinter
import keyboard

# Чтение API-ключей из файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')
api_key1 = config['API']['api_key']
api_key2 = config['API']['api_key2']
api_key3 = config['API']['api_key3']
api_key4 = config['API']['api_key4']
api_key5 = config['API']['api_key5']
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

# Индекс текущего используемого ключа API
current_api_key_index = 0

# Функция для получения текущего ключа API
def get_current_api_key():
    return api_keys[current_api_key_index]

# Обработка каждого изображения
for image_file in image_files:
    attempts = 0
    
    # Получение текущего ключа API
    api_key = get_current_api_key()
    
    # Определяем, какой ключ использовать для текущего файла
    file_count = f"Ключ {current_api_key_index + 1}"

    # Увеличиваем индекс для следующего использования ключа
    current_api_key_index = (current_api_key_index + 1) % len(api_keys)

    # Установка ключа API
    openai.api_key = api_key
    
    # Флаг для проверки состояния паузы
    paused = False
    
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
            gpt_response = response.choices[0]["message"]["content"]

            if "--ar 16:9" not in gpt_response:
                # Если не соответствует, повторяем запрос
                print("Ошибка формата ответа. Повторный запрос.")
                attempts += 1
                continue


            # Разбиваем ответ на параграфы
            paragraphs = gpt_response.split("\n\n")

            # Выводим информацию о тегах и названии файла
            print(f"File: '{image_file}' Обработан ключом: {file_count}! \n{response.choices[0]['message']['content']}\n")

            # Проверяем, сколько параграфов найдено
            if len(paragraphs) >= 1:
                result_1 = paragraphs[0]
                print("Найден параграф 1")

            if len(paragraphs) >= 2:
                result_2 = paragraphs[1]
                print("Найден параграф 2")

            if len(paragraphs) >= 3:
                result_3 = paragraphs[2]
                print("Найден параграф 3")

            else:
                print("Не найдены все параграфы")

            print("---------------------------------------")

        except Exception as e:
            print("Ошибка при обработке файла:", e)
            attempts += 1
            continue

        except openai.error.APIError as e:
            if "You’ve reached the current usage cap for GPT-4" in str(e):
                pause_for_two_hours()
                continue

        # Ждем, пока не будет нажата клавиша
        while True:
            if keyboard.is_pressed('-') and not paused:
                paused = True
                print("Программа поставлена на паузу")
            elif keyboard.is_pressed('+') and paused:
                paused = False
                print("Программа возобновлена")
                break


    # Если после 5 попыток ответ все еще содержит запрещенные слова, переходим к следующему файлу
    if attempts == attempts_max:
        print(f"Достигнуто максимальное количество попыток ({attempts_max}) для файла {image_file}. Переходим к следующему файлу.", "\n")

        
print("Все файлы успешно обработаны!")
input("Для выхода нажмите Enter...")
