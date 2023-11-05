def main():
    n = 0
    total_sum = 0

    for i in iter(int, 0):
        i = int(input('Введите число последовательности: '))
        total_sum += i
        n += 1

    average = total_sum / (n - 1)
    return average

print(main())