name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Hello World!'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
print('Some text')

res = input('Print your text: ')
print('Ты написал ', res)

ADULT = 18
age = int(input('Сколько тебе лет? '))
how_old = ADULT - age
print(how_old, 'Осталось до совершеннолетия')

