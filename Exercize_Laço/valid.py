"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).

Write a program that reads and validates the following information:
Name: greater than 3 characters;
Age: between 0 and 150;
Salary: greater than zero;
Gender: 'f' or 'm';
Marital Status: 's', 'c', 'v', 'd';
Use the len(string) function to find out the length of a text (number of characters).

s -> single (solteiro)
c ->married (casado(a))
v -> widower (viúvo(a))
d -> divorced (divorciado(a))

"""

name = input('Write a name : ')
age = int(input('Write a age : '))
salary = float(input('Write a salary : '))
gender = input('Write a gender, f to female and m to masculine : ')
marital_status = input('Write a Marital Status : ')

while len(name) < 3:
    name = input('The name must be minimum 4 characters : ')
while age < 0 or age > 150:
    age = input('The age must be betwen 0 and 150 : ')
while (salary)<0:
    salary = float(input('The salary must be greater than zero : '))
while gender != 'f' and gender != 'm':
    gender = input('The gender must be f(female) or m(masculine) : ')
while marital_status != 's' and marital_status != 'c' and marital_status != 'v' and  marital_status != 'd':
    marital_status = input('The Marital Status must be equal a s, c, v, d :')
print('''Great! Valid Registrration.
        name : {}
        age : {}
        salary : {}
        gender : {}
        marital status : {}'''.format(name, age, salary, gender, marital_status))