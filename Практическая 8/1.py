import math

# Функция для вычисления площади круга
def circle_area(radius):
    return math.pi * radius**2

# Функция для вычисления площади прямоугольника
def rectangle_area(length, width):
    return length * width

# Функция для вычисления площади треугольника
def triangle_area(base, height):
    return 0.5 * base * height

# Функция для вычисления площади квадрата
def square_area(side):
    return side**2

# Пример использования:
print(circle_area(2)) # вычислит площадь круга с радиусом 2
print(rectangle_area(3, 4)) # вычислит площадь прямоугольника с длиной 3 и шириной 4
print(triangle_area(5, 6)) # вычислит площадь треугольника с основанием 5 и высотой 6
print(square_area(7)) # вычислит площадь квадрата со стороной 7