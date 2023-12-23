"""
Python Style! Переменные spam и eggs используется в языке Python как временные
переменные. Эти названия, ветчина и яйца, используют True Python разработчики.
Ведь язык назван в честь комедийного шоу Летающий цирк Монти Пайтон. А одно
из их видео посвящено шуткам про ветчину и яйца.

"""

my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10) # IndexError: pop index out of range
