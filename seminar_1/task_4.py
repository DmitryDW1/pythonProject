Задание №4
Работа в консоли в режиме интерпретатора Python.
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.

Квадратное уравнение имеет вид

ax**2 + bx + c = 0
При его решении сначала вычисляют дискриминант по формуле

D = b**2 - 4ac
Если D > 0, то квадратное уравнение имеет два корня:

x_1 = (-b + math.sqrt(D)) / (a * 2)
x_2 = (-b - math.sqrt(D)) / (a * 2)

Если D = 0, то 1 корень:


И если D < 0, то делают вывод, что корней нет.

>>> a = 5
>>> b = -10
>>> c = -400
>>> d = b ** 2 - 4 * a * c
>>> d
8100
>>> import math
>>> sd = math.sqrt (d)
>>> sd
90.0
>>> x_1 = (-b + sd) / 2 / a
>>> x_2 = (-b - sd) / 2 / a
>>> x_1, x_2
(10.0, -8.0)
>>>

https://younglinux.info/python/task/quadratic

