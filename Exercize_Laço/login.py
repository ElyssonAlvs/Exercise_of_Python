"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações

 Make a program that reads a username and password and does not accept the password equal to the username, 
 showing an error message and asking for the information again

"""

username = input('Write a usarname : ')
password = input('Write a password : ')

while username == password:
    print('Password must be different from login\n')
    password = input('Password :')
print('Ok! Valid registration.')