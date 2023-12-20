# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

num = int(input('Input number (1 - 999): '))
CONST1 = 10
CONST2 = 100
CONST3 = 1000

while True:
    if num in range(1, 1000):
        if num < CONST1:
            result = num ** 2
        elif num < CONST2:
            result = (num % 10) * (num // 10)
        else:
            ones = num % CONST1
            houndred = num // CONST2
            dosens = (num % CONST2) // CONST1
            result = ones * CONST2 + dosens * CONST1 + houndred
        break
print(result)
