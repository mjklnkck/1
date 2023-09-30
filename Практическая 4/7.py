def factorial(n):
    result = 1
    sum_of_factorials = 0
    for i in range(1, n + 1):
        result *= i
        sum_of_factorials += result
    return sum_of_factorials

n = int(input('Введите число n: '))
result = factorial(n)
print(result)