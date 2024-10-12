import time

# Запрашиваем у пользователя количество минут и секунд
minutes = int(input("Введите количество минут: "))
seconds = int(input("Введите количество секунд: "))

# Преобразуем все время в секунды
total_seconds = minutes * 60 + seconds

# Запускаем цикл обратного отсчета
while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)  # Получаем минуты и секунды
    print(f"Осталось: {mins} минут {secs} секунд")
    time.sleep(1)  # Ожидание 1 секунду
    total_seconds -= 1

# Сообщение, когда время вышло
print("Время вышло!")