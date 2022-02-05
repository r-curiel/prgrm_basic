"""
Enunciado: Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.

Resolução: 
"""

import math


radius = float(input("Insert the cylinder's radius: "))

print("%.2f" % (math.pi * radius ** 2))

"""
Comentário: Utilização da biblioteca math para aplicação do pi. Ademais, a operação 
foi retornada a partir da leitura simples do valor do rádio.
"""