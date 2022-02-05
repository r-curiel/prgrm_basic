"""
Enunciado: Leia um valor de área em hectares e apresente-o convertido em metros 
quadrados m2. A fórmula de conversão é: M = H * 10000, sendo M a área em metros 
quadrados e H a área em hectares.

Resolução: 
"""

hectares = float(input('Insert hectares: '))

print('{0} hectares are equals {1} square meters!'.format(hectares, (hectares * 10000)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""