"""
Enunciado: Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula 
de conversão é: R = G* pi/180, sendo G o ângulo em graus pi em radianos.

Resolução: 
"""

import math


degrees = float(input('Insert degrees: '))

print(f'{degrees} degrees are equals {(degrees * (math.pi / 180))} radians!')

"""
Comentário: A resolução utiliza o método pi da biblioteca math. Desta forma, 
utilizou-se o pi com maior precisão para a solução do exercício.
"""