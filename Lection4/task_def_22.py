# ● Не локальные переменные:

def main(a):
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1

    return x + func(a)


x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')


# Функция func вложена в функцию main. Благодаря команде nonlocal мы смогли
# получить доступ к x = 1. В результат внутри func x увеличился до 101. В отличии от
# команды global, мы не смогли увидеть внешний x = 42. nonlocal позволяет заглянуть
# на верхний уровень вложенности, но не выходить на глобальные переменные
# модуля.
