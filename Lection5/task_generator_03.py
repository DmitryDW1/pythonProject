# При работе с генераторами стоит помнить, что для каждого витка внешнего цикла
# внутренний перебирает все элементы от начала до конца. Например:

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

# Создаём генератор на основе двух списков x и y. 7 элементов в первом списке и 6 во
# втором. Всего 13. Генератор считает сумму пар элементов.
# Генератор перебирает все значения списка x и оставляет только нечётные.
# Исключаем 2 и 8, т.е. оставляем 5 из 7 элементов списка для вычисления суммы. В
# списке y исключаем единицу, т.е. оставляем 5 из 6 элементов. Новичок может
# подумать, что на выходе получим 10 элементов - 5 из x и 5 из y. Но циклы вложены
# друг в друга, следовательно, количество элементов на выходе 5х5=25. А
# асимптотика данного генератора квадратичная, O(NхM), где N и M - длина списков x
# и y.
# 🔥 Важно! На асимптотическую сложность генератора влияют только
# количество циклов. Наличие if проверок конечно же замедляет генерацию
# значений. Но if воспринимается как константа в вычислении асимптотики. 4
# вложенных цикла без проверок будут иметь асимптотику 4 степени, а 3 цикла с
# 3 проверками — асимптотику 3-й степени. Не стоит злоупотреблять
# количеством вложенных циклов.