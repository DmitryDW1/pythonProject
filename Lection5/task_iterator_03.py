# ● Функция next
# Функция next имеет формат next(iterator[, default]). На вход функция принимает
# итератор, который вернула функция iter. Каждый вызов функции возвращает
# очередной элемент итератора.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter)) # StopIteration

# При завершении элементов выбрасывается исключение StopIteration. Данное
# исключение служит указанием циклу for in о завершении работы. Каждый раз когда
# происходит перебор коллекции в цикле создаётся исключение. Но цикл
# обрабатывает его как сигнал для завершения итерации и перехода к следующему
# блоку кода. Исключение не останавливает программу.
