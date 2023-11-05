# Функция для нахождения суммы элементов в массиве
def sum_array(array):
    return sum(array)

# Функция для нахождения среднеарифметического значения в массиве
def average_array(array):
    return sum(array) / len(array)

# Пример использования:
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
array3 = [11, 12, 13, 14, 15]

print(sum_array(array1)) # вычислит сумму элементов в array1
print(average_array(array1)) # вычислит среднеарифметическое значение в array1

print(sum_array(array2)) # вычислит сумму элементов в array2
print(average_array(array2)) # вычислит среднеарифметическое значение в array2

print(sum_array(array3)) # вычислит сумму элементов в array3
print(average_array(array3)) # вычислит среднеарифметическое значение в array3