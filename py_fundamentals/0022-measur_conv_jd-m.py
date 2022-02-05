"""
Enunciado: Leia um valor de comprimento em jardas e apresente-o convertido em metros. 
A fórmula de conversão é: M = 0,91 *J, sendo J o comprimento em jardas e M o comprimento
 em metros.

Resolução: 
"""

yards = float(input('Insert yards: '))

print('{0} yards are equals {1} meters.'.format(yards, (yards * 0.91)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""