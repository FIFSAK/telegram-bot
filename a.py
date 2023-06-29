import time
import threading


def print_message():
    while not gather_links_done.is_set():
        print("Сообщение обрабатывается...")
        time.sleep(1)


def gather_links():
    # здесь ваш асинхронный процесс сбора ссылок, который занимает пару минут
    time.sleep(5)  # для демонстрации, сделаем просто паузу в 2 минуты
    print("links")
    a = 5
    gather_links_done.set()
    return a



gather_links_done = threading.Event()

thread1 = threading.Thread(target=print_message)
thread2 = threading.Thread(target=gather_links)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(gather_links())