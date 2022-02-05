"""
Enunciado: Leia um valor de comprimento em metros e apresente-o convertido em jardas. 
A fórmula de conversão é: J = M/0,91 = sendo J o comprimento em jardas e M o comprimento
 em metros.

Resolução: 
"""

meters = float(input('Insert meters: '))

yards = meters / 0.91

print('%.2f meters are equals %.2f yards.' % (meters, yards))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""