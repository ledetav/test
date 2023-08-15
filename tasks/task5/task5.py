import random

# Запрос ввода диапазона у пользователя
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

# Генерация случайного числа в заданном диапазоне
random_number = random.randint(min_value, max_value)

# Вывод результата
print("Случайное число:", random_number)