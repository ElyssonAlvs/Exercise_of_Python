"""
Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro
casas decimais conforme exemplos.
Fórmula da área: area = π . raio2
Considere o valor de π = 3.14159

Make a program to read the value of the radius of a circle, and then show the value of the area of ​​this circle with four
decimal places as examples.
Area formula: area = π . radius2
Consider the value of π = 3.14159
"""
from math import pow
PI = 3.14159
radius = float(input("Write this radius of the circle : "))
area = PI * pow(radius, 2)
print("The area of the circle is {:.2f}".format(area))
