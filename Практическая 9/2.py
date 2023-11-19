def swap_min_max(matrix):
    for row in matrix:
        min_index = row.index(min(row))
        max_index = row.index(max(row))

        row[0], row[min_index] = row[min_index], row[0]
        row[-1], row[max_index] = row[max_index], row[-1]

    return matrix


# Пример матрицы B
B = [[4, 2, 9],
     [1, 5, 3],
     [7, 6, 8]]

# Вызов функции swap_min_max и вывод измененной матрицы
new_matrix = swap_min_max(B)
for row in new_matrix:
    print(row)