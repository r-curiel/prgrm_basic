"""
Enunciado: Leia um valor de área em acres e apresente-o convertido em metros quadrados 
m2. A fórmula de conversão é: M = A* 4048,58, sendo M a área em metros quadrados e A a 
área em acres.

Resolução: 
"""

acres = float(input('Insert acres: '))

print('{0} acres are equals {1} square meters!'.format(acres, (acres * 4048.58)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""