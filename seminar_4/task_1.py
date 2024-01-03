# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


some_text = 'Задание №1' \
            'Погружение в Python | Функции' \
            '✔ Напишите функцию, которая принимает строку текста. ' \
            'Вывести функцией каждое слово с новой строки.' \
            '✔ Строки нумеруются начиная с единицы.' \
            '✔ Слова выводятся отсортированными согласно кодировки Unicode.' \
            '✔ Текст выравнивается по правому краю так, чтобы у самого' \
            ' длинного слова был один пробел между ним и номером строки.'


def word_processing(text):
    len_word = 0
    some_words = sorted(text.split(' '))
    for word in some_words:
        if len(word) > len_word:
            len_word = len(word)
    for n, word in enumerate(some_words, 1):
        print(f'{n} {word:>{len_word}}')


word_processing(some_text)