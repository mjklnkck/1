def main():
    y = 1
    previous_number = 1
    current_length = 1

    while True:
        number = int(input('Введите число последовательности: '))
        if number == 0:
            break

        if number == previous_number:
            current_length += 1
        else:
            current_length = 1

        if current_length > y:
            y = current_length

        previous_number = number

    return y

print(main())