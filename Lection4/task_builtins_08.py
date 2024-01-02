# ● Функция any()
# any(iterable)
# Функция возвращает истину, если хотя бы один элемент последовательности
# являются истиной. На Python создание функции any выглядело бы так:
"""any(iterable)"""
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# Функция any работает аналогично all. Но если all можно представить как if c
# цепочкой and, то any — это if с цепочкой or.
# Функция map заменила числа на True и False, далее all проверила все ли элементы
#

numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')