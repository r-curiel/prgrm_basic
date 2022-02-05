"""
Enunciado: Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do circulo é pi * raio2.

Resolução: 
"""

import math


radius = float(input("Insert the circle's radius: "))

print("%2.2f" % (math.pi * (radius ** 2)))
