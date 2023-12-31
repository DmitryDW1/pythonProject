"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран
"""

from decimal import Decimal

items = {
    "ключи": 0.3,
    "кошелек": 0.3,
    "телефон": 0.8,
    "зажигалка": 0.1
}
max_weight = 1.0

# Введите ваше решение ниже

max_weight_items = Decimal(str(max_weight))
backpack = {}
for i in items:
    if max_weight_items >= Decimal(str(items[i])):
        if i not in backpack:
            backpack.setdefault(i, items[i])
        max_weight_items -= Decimal(str(items.get(i)))
    else:
        continue
print(backpack)
