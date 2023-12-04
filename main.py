# №1
import threading
import time

def fast_operation(a, b):
    result = a + b
    return result

def slow_operation(a):
    time.sleep(a)
    result = a ** 2
    return result

def execute_fast_operation(a, b):
    result = fast_operation(a, b)
    print("Быстрая операция, result:", result)

def execute_slow_operation(a):
    result = slow_operation(a)
    print("Медленная операция result:", result)

# Задаем аргументы для выполнения функций
a = 2
b = 3

# Создаем два потока для выполнения функций
fast_thread = threading.Thread(target=execute_fast_operation, args=(a, b))
slow_thread = threading.Thread(target=execute_slow_operation, args=(a,))

# Запускаем потоки на выполнение
fast_thread.start()
slow_thread.start()

# Ожидаем завершения выполнения потоков
fast_thread.join()
slow_thread.join()

print("Оба потока завершили выполнение.")

# №2
import asyncio

async def handle_phone_calls():
    while True:
        # Обработка телефонных звонков
        await asyncio.sleep(1)
        print("Обработка телефонных звонков")

async def handle_visitors():
    while True:
        # Обработка посетителей
        await asyncio.sleep(2)
        print("Обработка посетителей")

async def book_flight_tickets():
    while True:
        # Бронирование билетов на самолет
        await asyncio.sleep(3)
        print("Бронирование билетов на самолет")

async def control_meeting_schedules():
    while True:
        # Контроль графиков встреч
        await asyncio.sleep(4)
        print("Контроль графиков встреч")

async def fill_documents():
    while True:
        # Заполнение документов
        await asyncio.sleep(5)
        print("Заполнение документов")

async def secretary():
    # Запуск всех задач
    tasks = [
        handle_phone_calls(),
        handle_visitors(),
        book_flight_tickets(),
        control_meeting_schedules(),
        fill_documents()
    ]
    await asyncio.gather(*tasks)

# Запуск асинхронного кода
asyncio.run(secretary())




