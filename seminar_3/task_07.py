"""
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

user_text = input("Введите текст: ")
my_set = set(user_text)

my_dist_1 = {}

# count = 0
# for i in my_set:
#     for j in range(len(user_text)): # Без использования .count()
#         if user_text[j] == i:
#             count += 1
#     my_dist_1[i] = count
#     count = 0
# print(my_dist_1)

# for i in my_set:
#     my_dist_1.setdefault(i, user_text.count(i)) # С использованием .count()
# print(my_dist_1)

for i in user_text:
    my_dist_1[i] = my_dist_1.get(i, 0) + 1 # Через .get()
print(my_dist_1)
