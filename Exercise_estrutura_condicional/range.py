"""Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos
seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em
nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

You must write a program that reads any value and displays a message saying which of the
following intervals ([0,25], (25,50], (50,75], (75,100]) this value is found. Obviously if the value is not in
none of these ranges, the message “Out of range” should be printed.
"""
range = float(input('Choose the range : '))
if 0 < range <= 25:
    print('Range [0,25]')
elif 25 < range <= 50:
    print('Range (25,50]')
elif 50 < range <= 75:
    print('Range (50,75]')
elif 75 < range <= 100:
    print('Range (75,100]')
elif range < 0:
    print('not range')
