"""
Задание №3
Погружение в Python | Коллекции
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

user_input = (12, "war", 434.54, "hello", (1, 3, "world"), -534.553, True, None, -45, [1, 2, 3])
answer_dict = dict()
for item in user_input:
    t = type(item)
    if t in answer_dict:
        answer_dict[t].append(item)
    else:
        answer_dict[t] = [item]
print(answer_dict)
