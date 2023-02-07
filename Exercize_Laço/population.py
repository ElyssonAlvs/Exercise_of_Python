'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento
de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população 
do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

Assume that the population of country A is of the order of 80000 inhabitants with an annual growth
rate of 3% and that the population of B is 200000 inhabitants with a growth rate of 1.5%. 
Write a program that calculates and writes the number of years required for the population of country A to exceed or equal the population of country B,
growth rates maintained.

'''

popA = int(input('Population for A : '))
while popA < 0:
    popA = int(input('Population A : '))
tax_A = float(input('Growth porcentage to A : '))
popB = int(input('Population for B : '))
while popB < 0:
    popB = int(input('Population B : '))
tax_B = float(input('Growwth porcentage to B : '))

years = 0

while popA <  popB:
    years+=1
    popA = int((1 + (tax_A/100))*popA)
    popB = int((1 +(tax_B/100))*popB)
print('Would exceed %d years' % years)