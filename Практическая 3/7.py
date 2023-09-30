# -- coding: utf-8 --
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 'Да'
    else:
        return 'Нет'

def main():
    n = int(input('Введите год: '))
    result = is_leap_year(n)
    return result

print(main())