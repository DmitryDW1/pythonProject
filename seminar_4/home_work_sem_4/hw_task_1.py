# Транспонирование матрицы

# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает
# транспонированную матрицу.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(matrix):
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return res


transposed_matrix = transpose(matrix)
print(transposed_matrix)
