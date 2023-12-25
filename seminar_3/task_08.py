"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

friends_stuff = {
'Олег': ('палатка', 'топор','еда','пиво'),
'Игорь': ('палатка', 'вилка','вода','пиво'),
'Гусь': ('палатка', 'топор','вода','пиво'),
'Стоун': ('палатка', 'топор','вода','лимонад')
}

set_1 = set()
for k in friends_stuff:
    if not set_1:
        set_1 = set(friends_stuff[k])
    else:
        set_1 &= set(friends_stuff[k])
print("Вещи друзей: ", set_1)

my_tuple = friends_stuff.keys()

my_set = set()
for friends in my_tuple:
    my_set = set(friends_stuff[friends])

    for other_friends in [i for i in my_tuple if i != friends]:
        my_set = my_set - set(friends_stuff[other_friends])
    if my_set:
        print(f"Вещи уникальны, есть только у {friends}:", *my_set)

for friends in my_tuple:
    my_set = set()
    to_remove = set(friends_stuff[friends])
    for other_friends in [i for i in my_tuple if i != friends]:
        if not my_set:
            my_set = set(friends_stuff[other_friends])
        else:
            my_set = my_set & set(friends_stuff[other_friends])
    my_set -= to_remove

    if my_set:
        print(f'{friends} не взял \" {my_set}')