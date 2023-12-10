def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def (x, n):
    if n == 0:
        return 1
    else:
        return (x**n) / factorial(n)

X = 2
N = 3
result = expression(X, N)
print(result)