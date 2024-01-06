# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

user_text = input()


def user_dict(text: str) -> dict[chr:int]:
    """Создание словаря"""
    # dict_user = {}
    # for i in list(text):
    #     dict_user.setdefault(i, ord(i))
    # return dict_user
    return {i: ord(i) for i in text}


print(user_dict(user_text))
