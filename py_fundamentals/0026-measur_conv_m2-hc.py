"""
Enunciado: Leia um valor de área em metros quadrados m2 e apresente-o convertido em 
hectares. A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e 
H a área em hectares.

Resolução: 
"""

smeters = float(input('Insert square meters: '))

print('{0} square meters are equals {1} hectares!'.format(smeters, (smeters * 0.0001)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""