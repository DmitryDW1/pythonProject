# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

import random

user_list = [random.randint(1, 10) for x in range(10)]


def buble_sort(user_list):
    n = len(user_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if user_list[j] > user_list[j + 1]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]


print(user_list)
buble_sort(user_list)
print(user_list)
