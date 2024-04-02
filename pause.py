import time
from logger import log_and_print

paused = False
Not_paused = True

def toggle_pause(threads):
    global paused
    paused = not paused
    global Not_paused
    Not_paused = False
    log_and_print("Нажато '-', ожидание выполнения текущих запросов в потоках и ставим на паузу")
    if paused:
        pause_all_threads(threads)

def pause_all_threads(threads):
    for thread in threads:
        thread.paused = True

def toggle_pause2():
    global paused
    paused = False
    global Not_paused
    Not_paused = True
    log_and_print("Нажато '+'")

def pause_check():
    if paused == True:
        log_and_print("Поток на паузе", "\n")
        while Not_paused == False:
            time.sleep(10)
        log_and_print("Снятие с паузы", "\n")

def pause_for_two_hours():
    log_and_print("Превышен лимит запросов. Остановка работы на два часа.")
    time.sleep(7200)  # 7200 секунд = 2 часа
