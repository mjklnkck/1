n = int(input('Введите N: '))

def main(n):
    results = [i**2 for i in range(n) if i**2 <= n]
    print(*results, sep='\n')

main(n)