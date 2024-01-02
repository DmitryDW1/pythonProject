def my_func():
    pass

# Плохо:
if a != 5:
    pass
else:
    a += 1

# Уже лучше:
if a == 5:
    a += 1
else:
    pass
# Отлично. Ничего лишнего:
if a == 5:
    a += 1