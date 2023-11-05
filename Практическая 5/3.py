def find_power_and_exponent(n):
    exponent = 0
    power = 1
    while power <= n:
        power *= 2
        exponent += 1
    return exponent - 1, power // 2

def main():
    n = int(input('Введите N: '))
    exponent, power = find_power_and_exponent(n)
    print(f'Показатель: {exponent}, Степень: {power}')

main()