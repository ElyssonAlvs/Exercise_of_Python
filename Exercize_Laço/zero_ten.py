"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
 e continue pedindo até que o usuário informe um valor válido.

Write a program that asks for a grade between zero and ten. Show a message if the value is invalid
 and keep prompting until the user enters a valid value.
 """
num = float(input('Write a number, betwen 0 and 10 : '))
while num < 0 or num >10:
    num = int(input('The number has to be between 0 and 10, try again :'))
print('OK! Valid number.')