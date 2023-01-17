"""
Fazer um programa para ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Calcule e mostre o valor a ser pago

Make a program to read the code of a piece 1, the number of pieces 1, the unit value of each piece 1, the
one piece code 2, the number of pieces 2 and the unit value of each piece 2. Calculate and show the amount to be paid

Entrada :               Saída :
12 1 5.30               VALOR A PAGAR: R$ 15.50
16 2 5.10               

"""
productA = int(input("Choice the first product : "))
amountA = int(input("the amount of first product :"))
priceA = float(input("Price of first product :"))
print("--------------------------------------------------")
productB = int(input("Choice the second product : "))
amountB = int(input("the amount of second product :"))
priceB = float(input("Price of second product :"))
print("--------------------------------------------------")
total = (priceA * amountA) + (priceB * amountB)
print("Price of buy : R$ {:.2f}".format(total))
