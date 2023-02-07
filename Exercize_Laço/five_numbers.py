'''
Faça um programa que leia 5 números e informe o maior número.

Write a program that reads 5 numbers and reports the largest number.
'''
repetetions = int(input('How many numbers ? '))

number1 = int(input('Number 1 : '))
counter = 0
maior = number1

while counter < repetetions:
    counter += 1
    number1 = int(input('New Number : '))
    if number1 > maior:
        maior = number1
print('Higher number : %d' % maior)