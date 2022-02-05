"""
Enunciado: Faça um programa que identifique o tipo de triângulo a partir dos seus lados.

Resolução: 
"""

A = int(input('Insert the first number: '))
B = int(input('Insert the second number: '))
C = int(input('Insert the third number: '))

if A < (B + C) and B < (A + C) and C < (A + B):
   if A == B and A == C and B == C:
       print('Equilateral triangle')
   elif A == B or A == C or B == C:
       print('Isosceles triangle')
   else:
       print('Scalene triangle')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""