# -- coding: utf-8 --
def main():
    numbers = [int(input(f'Введите {i + 1}-е число: ')) for i in range(3)]
    u_numbers = len(set(numbers))

    if u_numbers == 1:
        return 3
    elif u_numbers == 2:
        return 2
    else:
        return 0


print(main())
