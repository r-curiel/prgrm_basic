"""
Enunciado: Escreva um programa que leia as coordenadas x e y de dois pontos e calcule 
a distância entre eles.

Resolução: 
"""

A = {'x': int(input('A(x): ')), 'y': int(input('A(y): '))}
B = {'x': int(input('B(x): ')), 'y': int(input('B(y): '))}

distance = ((B.get('x') - A.get('x')) ** 2 + (B.get('y') - A.get('y')) ** 2) ** 0.5

print(f"The distance from origin of A{tuple(A.values())} and B{tuple(B.values())} is {round(distance)}.")


"""
Comentário: A resolução consistiu na criação de dois dicionários representando dois 
pontos, com chamadas para input de 'x' e 'y'. Calculada a distância entre eles, o 
retorno demonstrou as coordenadas e o resultado solicitado.
"""