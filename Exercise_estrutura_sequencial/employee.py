"""
Fazer um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas
decimais.

Write a program that reads the number of an employee, the number of hours worked, the amount he receives for
hour and calculates the salary of that employee. Next, show the employee's number and salary, with two spaces
decimals.

"""
number_of_employee = int(input("Write number of the employee : "))
time_at_working = int(input("Time at work : "))
money_for_work = float(input("Money for working hour : "))
salary = money_for_work * time_at_working
print("Salary : R$ {:.2f}".format(salary))
