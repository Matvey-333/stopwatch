import time


minutes = int(input("Введите количество минут: "))
seconds = int(input("Введите количество секунд: "))


total_seconds = minutes * 60 + seconds

while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)
    print(f"Осталось: {mins} минут {secs} секунд")
    time.sleep(1)  # Ожидание 1 секунду
    total_seconds -= 
print("Время вышло!")
