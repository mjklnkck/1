M = int(input("Введите размерность массива: "))
arr = []

# Ввод элементов массива с клавиатуры
print("Введите", M, "элементов массива:")
for i in range(M):
    arr.append(int(input()))

# Поиск максимального элемента
max_element = arr[0]
for i in range(1, M):
    if arr[i] > max_element:
        max_element = arr[i]

# Вывод массива в обратном порядке
print("Массив в обратном порядке:")
for i in range(M - 1, -1, -1):
    print(arr[i])

# Вывод максимального элемента
print("Максимальный элемент:", max_element)