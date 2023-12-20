# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

space = ' '
star = '*'
CONST1 = 1
CONST2 = 2

rows = int(input('Input number: '))
spaces = rows - CONST1
stars = CONST1

for i in range(rows):
    print((space * spaces) + (star * stars))
    stars += CONST2
    spaces -= CONST1
