"""
Enunciado: Leia um ângulo em radianos e apresente-o convertido em graus. A fórmulade
 conversão é: G = R* 180/pi, sendo G o ângulo em graus e pi em radianos.

Resolução: 
"""

import math


radians = float(input('Insert radians: '))

degrees = radians * (180 / math.pi)

print('%.2f radians are equals %.2f degrees!' % (radians, degrees))

"""
Comentário: A resolução utiliza da biblioteca math, importando a função math.pi. 
Desta forma, utilizou-se o pi com maior precisão para a solução do exercício.
"""