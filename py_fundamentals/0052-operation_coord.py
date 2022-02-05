"""
Enunciado: Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule 
sua distância da origem (0:0).

Resolução: 
"""

A = {'x': int(input('A(x): ')), 'y': int(input('A(y): '))}

distance = ((0 - A.get('x')) ** 2 + (0 - A.get('y')) ** 2) ** 0.5

print(f"The distance from origin (0, 0) of A{tuple(A.values())} is {round(distance)}.")

"""
Comentário: A resolução do código consistiu na substituição das coordenadas do ponto 
B do exercício anterior pelas coordenadas da origem, isto é (0, 0).
"""