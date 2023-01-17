"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema
cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo
menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Write a program to read the (X,Y) coordinates of an undetermined number of points in the system
Cartesian. For each point write the quadrant it belongs to. The algorithm will terminate when at least
least one of two coordinates is NULL (in this situation without writing any message).

"""
# Take the coordinates
coord_X = int(input("Write a coordinate for X : "))
coord_Y = int(input("Write a coordinate for Y : "))
# Comparate the coordinate and check if they exist
while coord_X != 0 and coord_Y != 0:
    if coord_X > 0 and coord_Y > 0:
        print('First Quadrant')
    elif coord_X < 0 and coord_Y > 0:
        print('Second Quadrant')
    elif coord_X < 0 and coord_Y < 0:
        print('Third Quadrant')
    else :
        print('Fourth Quadrant')
    coord_X = int(input("Write a coordinate for X : "))
    coord_Y = int(input("Write a coordinate for Y : "))
print("Fim!")