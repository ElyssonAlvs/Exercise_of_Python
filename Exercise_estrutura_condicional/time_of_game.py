"""Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode
começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Read the start time and end time of a game. Then calculate the duration of the game, knowing that it can
start on one day and end on another, with a minimum duration of 1 hour and a maximum duration of 24 hours.
"""
start_time = int(input('What is start time to the game ? : '))
ending_time = int(input('and the ending ? : '))
duration = int
if start_time < ending_time:
    duration = start_time - ending_time
else:
    duration = 24 - start_time + ending_time
print('The game lasted {} hour(s)'.format(duration))
