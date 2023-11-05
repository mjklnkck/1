def count_sequence():
    sequence_length = 0
    while True:
        number = int(input('Введите число последовательности: '))
        if number == 0:
            break
        sequence_length += 1
    return sequence_length

def main():
    n = count_sequence()
    return n

print(main())