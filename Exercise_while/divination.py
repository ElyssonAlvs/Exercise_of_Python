# Faça um jogo de adivinhação / Make to a guessing game;
from random import randint
print('The machine will choose a number between 0 and 100, try to get it right!')
user_number = int(input('Choice a number : '))
secret_number = randint(0, 101)
counter = 0
while secret_number != user_number:
    if (user_number > secret_number):
        print('Try again! The number you chose was greater than the secret number')
    else:
        print('Try again! The number you chose was less than the secret number')
    counter += 1
    user_number = int(input('Choice a number : '))
print('Thank you for play!You are right! In {} attempts'.format(counter + 1))
