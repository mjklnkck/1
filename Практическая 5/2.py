def find_smallest_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return i
    return n

def main():
    n = 0
    while n < 2:
        n = int(input('Введите N, не меньшее 2: '))
        if n < 2:
            print('Число должно быть не меньше 2')
    smallest_divisor = find_smallest_divisor(n)
    print(smallest_divisor)

main()