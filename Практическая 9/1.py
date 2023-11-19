def calculate_sum_and_count(matrix):
    sum_positive = 0
    count_positive = 0

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] > 0:
                sum_positive += matrix[i][j]
                count_positive += 1

    return sum_positive, count_positive

# Пример матрицы A
A = [[1, -2, 3],
     [4, 5, 6],
     [7, 8, -9]]

# Вызов функции calculate_sum_and_count и вывод результатов
sum_positive, count_positive = calculate_sum_and_count(A)
print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")
print(f"Количество положительных элементов над главной диагональю: {count_positive}")