from math import sqrt

#Прямоугольник
a = 20
b = 10

#Вычисление периметра
P=(a+b)*2

#Вычисление площади
S = a*b

#Вычисление диагонали
D = sqrt(a**2 + b**2)
print(f'Прямоуголник со сторонами {a} и {b} \n Периметр: {P} \n Площадь: {S} \n Длина диагонали: {D:.2f}')