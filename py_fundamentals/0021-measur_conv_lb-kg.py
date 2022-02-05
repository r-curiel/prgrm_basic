"""
Enunciado: Leia um valor de massa em libras e apresente-o convertido em quilogramas. A 
fórmula de conversão é: K = L* 0,45, sendo K a massa em quilogramas e L a massa em 
libras.

Resolução: 
"""

lbs = float(input('Insert the weight in libbers: '))

print('{0}lbs are equals {1:.2}kg!'.format(lbs, (lbs * 0.45)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""