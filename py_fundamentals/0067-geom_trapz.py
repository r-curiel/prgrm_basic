"""
Enunciado: Faça um programa que calcule e mostre a área de um trapézio.

Resolução: 
"""

sbase = float(input('Insert the smallest base: '))
bbase = float(input('Insert the biggest base: '))
height = float(input('Insert the height: '))

if sbase > 0 and bbase > 0:
   print(((sbase + bbase) * height) / 2)


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""