import time
import openai
import os
import base64
import configparser
from PIL import Image
import piexif
from tkinter import filedialog, Tk  # Импортируем необходимые модули из tkinter

# Чтение API-ключей из файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')
api_key1 = config['API']['api_key']
api_key2 = config['API']['api_key2']
promt = config['API']['promt']
detail = config['API']['detail']
attempts_max = int(config['API']['max_attempts'])
max_tokens = int(config['API']['max_tokens'])
temp = int(config['API']['temp'])
model = config['API']['model']

result_1 = ""
result_2 = ""
result_3 = ""
# Функция для кодирования изображения в формат Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
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

for image_file in image_files:
    attempts = 0
    # Определяем, какой ключ использовать для текущего файла
    if api_key2:
        if image_files.index(image_file) % 2 == 0:  # Четные файлы используют второй ключ
            api_key = api_key1
            file_count = "Первый"
        else:  # Нечетные файлы используют второй ключ
            api_key = api_key2
            file_count = "Второй"
    else: 
        api_key = api_key
        file_count = "Первый"

    openai.api_key = api_key
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


            paragraphs = gpt_response.split("\n\n")
            result_1 = paragraphs[0]
            result_2 = paragraphs[1]
            result_3 = paragraphs[2]


            if result_1:
                print("Найден параграф 1:")
            if result_2:
                print("Найден параграф 2:")
            if result_3:
                print("Найден параграф 3:")
                
            # Выводим информацию о тегах и названии файла
            print(f"File: '{image_file}' Обработан ключом: {file_count}! \n{response.choices[0]['message']['content']}")
            print("---------------------------------------")



            # # Проверяем наличие запрещенных слов
            # if title_line and description and ("the photo shows" in title_line or "In the picture" in title_line or "the photo shows" in description or "In the picture" in description):
            #     print("Ошибка: найдены запрещенные слова в ответе")
            #     attempts += 1  # Увеличиваем счетчик попыток
            #     continue  # Повторяем обработку файла

            # Загружаем изображение
            # img = Image.open(image_path)

            # Проверяем наличие метаданных Exif
            # Проверяем наличие метаданных Exif

            # exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}

            # # Кодировка строк в UTF-16LE для совместимости с XP тегами
            # if title_line:
            #     encoded_title = title_line.encode('utf-16le')
            # if description:
            #     encoded_description = description.encode('utf-16le')
            # if tags_line:
            #     encoded_tags = tags_line.encode('utf-16le')

            # # Добавление метаданных
            # if title_line:
            #     exif_dict['0th'][piexif.ImageIFD.XPTitle] = encoded_title
            # if description:
            #     exif_dict['0th'][piexif.ImageIFD.XPSubject] = encoded_description
            # if tags_line:
            #     exif_dict['0th'][piexif.ImageIFD.XPKeywords] = encoded_tags

            # Сохранение изменений
            # exif_bytes = piexif.dump(exif_dict)
            # img.save(image_path, exif=exif_bytes, format='JPEG')

        except Exception as e:
            print("Ошибка при обработке файла:", e)
            attempts += 1  # Увеличиваем счетчик попыток
            continue  # Повторяем обработку файла

        except openai.error.APIError as e:
            if "You’ve reached the current usage cap for GPT-4" in str(e):
                pause_for_two_hours()
                continue  # Продолжаем обработку файла после ожидания

        break  # Выходим из цикла while, если ответ не содержит запрещенных слов или достигнуто ограничение по попыткам

    # Если после 5 попыток ответ все еще содержит запрещенные слова, переходим к следующему файлу
    if attempts == attempts_max:
        print(f"Достигнуто максимальное количество попыток ({attempts_max}) для файла {image_file}. Переходим к следующему файлу.", "\n")

        
print("Все файлы успешно обработаны!")
input("Для выхода нажмите Enter...")
