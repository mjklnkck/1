def calculate_days(x, y):
    percent = 10 # Процентный прирост
    day_count = 0

    while x <= y:
        x += x * percent / 100
        day_count += 1

    return day_count

def main():
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))

    days_needed = calculate_days(x, y)
    print(days_needed)

main()