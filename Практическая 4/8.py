n = int(input('Введите число n: '))
for i in range(1, n + 1):
    print(''.join(map(str, range(1, i + 1))))