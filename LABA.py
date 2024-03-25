from math import pi

# Функция для вычисления длины окружности
def calculate_circumference(radius):
    circumference = 2 * pi * radius
    return circumference

# Функция для вычисления площади окружности
def calculate_area(radius):
    area = pi * (radius ** 2)
    return area

# Функция для вычисления площади кругового сектора
def calculate_sector_area(radius, angle):
    sector_area = (angle / 360) * calculate_area(radius)
    return sector_area

# Пользовательский ввод радиуса окружности и угла кругового сектора
radius = float(input("Введите радиус окружности: "))
angle = float(input("Введите угол кругового сектора (в градусах): "))

# Вычисление и вывод результата
circumference = calculate_circumference(radius)
area = calculate_area(radius)
sector_area = calculate_sector_area(radius, angle)

print("Длина окружности: ", circumference)
print("Площадь окружности: ", area)
print("Площадь кругового сектора: ", sector_area)