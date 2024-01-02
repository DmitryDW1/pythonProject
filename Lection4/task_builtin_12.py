# ● Функция globals()
# Функция возвращает словарь переменных из глобальной области видимости, т.е. из
# пространства модуля.

"""globals()"""
SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


print(globals())
print(f'{func(1, 2, 3) = }')
# Функция не сохраняет в словаре локальные переменные функций, даже если будет
# вызвана из тела функции.
# В словаре от globals содержаться и дандер переменные модуля. Они нужны Python
# для правильной работы кода.

# Внимание! Если вызвать функцию locals() из основного кода модуля, а не
# из функции, результат будет аналогичен работе функции globals()
x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)

