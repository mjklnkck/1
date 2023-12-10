def calculate_sum_and_count(matrix):
    sum_positive = 0
    count_positive = 0

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] > 0:
                sum_positive += matrix[i][j]
                count_positive += 1

    return sum_positive, count_positive

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            matrix.append(row)
    return matrix

def write_results_to_file(file_name, sum_positive, count_positive):
    with open(file_name, 'w') as file:
        file.write(f"Сумма положительных элементов над главной диагональю: {sum_positive}\n")
        file.write(f"Количество положительных элементов над главной диагональю: {count_positive}\n")

# Чтение матрицы из файла
A = read_matrix_from_file("Кириченко_Иван_Владимирович_У-232_vvod.txt")

# Вызов функции calculate_sum_and_count
sum_positive, count_positive = calculate_sum_and_count(A)

# Запись результатов в файл
write_results_to_file("Кириченко_Иван_Владимирович_У-232_vivod.txt", sum_positive, count_positive)