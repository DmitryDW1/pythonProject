# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа

user_text = input()


def user_dict(text: str) -> dict[int:int]:
    """Формирование словаря"""
    dict_user = {}
    test = text.split('/')
    dict_user.setdefault(test[1], test[0])
    dict_user.setdefault(test[2], tuple(test[3:]))
    return dict_user


print(user_dict(user_text))

# def dict_with_int(text: str) -> dict[int:int]:
#     first, second, third, *another = (int(i) for i in text.split("/"))
#     return {second: first, third: tuple(another)}
#
#
# print(dict_with_int(text))
