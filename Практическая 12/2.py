def find_max():
    num = int(input("Введите число: "))
    if num == 0:
        return 0
    else:
        max_num = find_max()
        return max_num if max_num > num else num

max_value = find_max()
print("Наибольшее значение числа в последовательности:", max_value)