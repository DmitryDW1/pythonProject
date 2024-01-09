# ● Функция iter
# Функция iter имеет формат iter(object[, sentinel]). object является обязательным
# аргументом. Если объект не реализует интерфейс итерации через методы __iter__
# или __getitem__, получим ошибку TypeError.

a = 42
# iter(a) # TypeError: 'int' object is not iterable

# Получим итератор списка

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

# Напрямую извлечь данные из итератора не получится. Python сообщает, что
# переменная list_iter указывает на <list_iterator object at 0x0000025383D29400>, т.е.
# объект итератор списка. Для кортежа функция iter вернёт tuple_iterator, для
# множеств set_iterator, а например для dict.items() вернётся dict_itemiterator.
# Один из простейших способов получить элементы - распаковать итератор через
# звёздочку.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

# 🔥 Внимание! Обратите внимание, что итератор является одноразовым
# объектом. Получив все элементы коллекции один раз он перестаёт работать.
# Для повторного извлечения элементов необходимо создать новый итератор