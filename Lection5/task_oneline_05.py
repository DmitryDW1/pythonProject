# ● Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
# Для упаковки может применяться символ “звёздочка” перед именем переменной.
# Такая переменная превратиться в список и соберёт в себя все значения, не
# поместившиеся в остальные переменные.


link ='https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')
