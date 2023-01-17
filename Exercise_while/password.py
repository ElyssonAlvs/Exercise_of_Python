"""
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha
incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser
impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

Write a program that repeats reading a password until it is valid. For every password read
entered, write the message "Password Invalid". When the password is entered correctly, it must be
the message "Access Permitted" is printed and the algorithm terminated. Assume that the correct password is the value 2002.
"""
password = int(input("Write this password : "))
while password != 2002:
    print("Invalid password")
    password = int(input("Write this password : "))
print("Access permited")
