# Задача 5 - HARD необязательная.
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в N-мерном пространстве. 
# Сначала задается N с клавиатуры, потом задаются координаты точек.

N = int(input('Введите значение N: '))
a = float(input('Введите координаты точки a: '))
b = float(input('Введите координаты точки b: '))


import math
distans = math.sqrt((a-b)**N)
print(f'Растояние между точками a и b = {distans}' )