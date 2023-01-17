"""
Fazer um programa para ler quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto
de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Make a program to read four integer values ​​A, B, C and D. Then calculate and show the difference of the product
of A and B by the product of C and D according to the formula: DIFFERENCE = (A * B - C * D).

"""
A = int(input("Write number A : "))
B = int(input("Write number B : "))
C = int(input("Write number C : "))
D = int(input("Write number D : "))

difference = (A * B - C * D)

print("The result of calcule is {}".format(difference))
