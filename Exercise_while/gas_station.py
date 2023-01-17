"""
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva
um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel
4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até
que seja válido). O programa será encerrado quando o código informado for o número 4. Deve ser escrito a
mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme
exemplo.

A gas station wants to determine which of its products are preferred by its customers. Write
an algorithm to read the type of fuel supplied (coded as follows: 1.Alcohol 2.Gasoline 3.Diesel
4.End). If the user enters an invalid code (outside the range 1 to 4), a new code must be requested (until
that is valid). The program will be closed when the informed code is number 4. It must be written to
message: "VERY THANK YOU" and the number of customers who supplied each type of fuel, as
example.

"""
Alcohol = 0
Gasoline = 0
Diesel = 0
type = int(input("""
    Choice this option of fuel 
    1.Alcohol
    2.Gasoline
    3.Diesel
    4.Fim
    : """))
while type != 4:
    if type == 1:
        Alcohol += 1
    elif type == 2:
        Gasoline += 1
    elif type == 3:
        Diesel += 1
    type = int(input("""
    Choice this option of fuel 
    1.Alcohol
    2.Gasoline
    3.Diesel
    : """))
print("Thank you very munch!")
print("Alcohol: {} ".format(Alcohol))
print("Gasoline: {} ".format(Gasoline))
print("Diesel: {} ".format(Diesel))
