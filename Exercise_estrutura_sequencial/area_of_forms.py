"""
    Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e
    mostre:
        a) a área do triângulo retângulo que tem A por base e C por altura.
        b) a área do círculo de raio C. (pi = 3.14159)
        c) a área do trapézio que tem A e B por bases e C por altura.
        d) a área do quadrado que tem lado B.
        e) a área do retângulo que tem lados A e B.

Write a program that reads in three double-precision floating-point values: A, B, and C. Then calculate and
    show:
        a) Find the area of ​​the right triangle that has A as its base and C as its height.
        b) the area of ​​the circle of radius C. (pi = 3.14159)
        c) the area of ​​the trapezoid that has A and B for bases and C for height.
        d) the area of ​​the square that has side B.
        e) the area of ​​the rectangle that has sides A and B.

"""
from math import pow
PI = 3.14
A = float(input("Choice value for A : "))
B = float(input("Choice value for B : "))
C = float(input("Choice value for C : "))

triangule = (A * C)/2
circle = PI * pow(C, 2)
trapeze = ((A+B))*C/2
square = B * B
rectangule = A * B

print(""" 
Area of triangle : {:.2f}
Area of circle : {:.2f}
Area of trapeze : {:.2f}
Area of square : {:.2f}
Area of rectangle : {:.2f}
""".format(triangule, circle, trapeze, square, rectangule))
