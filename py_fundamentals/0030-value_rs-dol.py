"""
Enunciado: Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor 
correspondente em dólares.

Resolução: 
"""

real = float(input('Insert reals: '))

dolar = float(input("Insert the dollar's quote:"))

print('From R$ {0} to $ {1}'.format(real, (real * dolar)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""