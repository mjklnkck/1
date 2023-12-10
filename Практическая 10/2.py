def swap_min_max(matrix):
    for row in matrix:
        min_index = row.index(min(row))
        max_index = row.index(max(row))

        row[0], row[min_index] = row[min_index], row[0]
        row[-1], row[max_index] = row[max_index], row[-1]

    return matrix


def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            matrix.append(row)
    return matrix


def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(str(num) for num in row))
            file.write('\n')


# Чтение матрицы из файла
A = read_matrix_from_file("Кириченко_Иван_Владимирович_У-232_vvod_2.txt")

# Вызов функции swap_min_max и получение измененной матрицы
new_matrix = swap_min_max(A)

# Запись результата в файл
write_matrix_to_file("Кириченко_Иван_Владимирович_У-232_vivod_2.txt", new_matrix)