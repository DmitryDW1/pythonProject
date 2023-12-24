my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items(): # Плохой способ
    print(tuple_data)
    print(f'{tuple_data[0] = } value before 100 - {100 - tuple_data[1]}')

for key, value in my_dict.items(): # Хороший способ
    print(f'{key = } value before 100 - {100 - value}')
