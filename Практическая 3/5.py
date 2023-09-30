# -- coding: utf-8 --
def main(z,x,c):
    numbers = [z,x,c]
    return min(numbers)

z = int(input('Введите первое число: '))
x = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Минимальное число: ', main(z,x,c))