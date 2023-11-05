def main():
    n = 0
    previous_number = 1

    while True:
        number = int(input('Введите число последовательности: '))
        if number == 0:
            break

        if number > previous_number:
            n += 1

        previous_number = number

    return n

print(main())