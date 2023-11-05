n = int(input("Введите размер массива: "))
arr = []

for i in range(n):
    arr.append(float(input("Введите элемент массива: ")))

average = sum(arr) / len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = average

print("Массив после замены нулевых элементов: ", arr)
