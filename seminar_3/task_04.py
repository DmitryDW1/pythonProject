"""
Задание №4

✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

user_list = [1, 2, 3, 1, "hello", 4, "hello"]
print(set(user_list))# это удалены дубликаты элементов

for item in set(user_list):
    if user_list.count(item) == 2:
        user_list.remove(item)
        user_list.remove(item)
print(user_list) # это удалены все повторяющиеся элементы
