import time
from logger import log_and_print

paused = False
def toggle_pause():
    global paused
    paused = not paused
    global Not_paused
    Not_paused = False
    log_and_print("Нажато '-', ожидание выполнения текущего запроса и ставим на паузу")
def toggle_pause2():
    global paused
    paused = False
    global Not_paused
    Not_paused = True
    log_and_print("Нажато '+'")
def pause_check():
    if paused == True:
        log_and_print("Вы на паузе", "\n")
        while Not_paused == False:
            time.sleep(10)                
            # Получаем значения из конфигурационного файла]
        log_and_print("Снятие с паузы", "\n")