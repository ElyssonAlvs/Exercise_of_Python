"""
Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar

Write a program to read an integer and say if this number is even or odd
"""
number = int(input('Type a number : '))
if number % 2 == 0:
    print('This number is PAR')
else:
    print('This number is IMPAR')
