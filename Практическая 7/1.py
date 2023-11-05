n = int(input("Введите размер массива: "))
arr = []

for i in range(n):
    arr.append(int(input("Введите элемент массива: ")))

max_element = max(arr)
print("Максимальный элемент: ", max_element)

reversed_arr = arr[::-1]
print("Массив в обратном порядке: ", reversed_arr)
