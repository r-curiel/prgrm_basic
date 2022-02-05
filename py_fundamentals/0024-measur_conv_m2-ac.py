"""
Enunciado: Leia um valor de área em metros quadrados m2 e apresente-o convertido em 
acres. A fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados 
e A a área em acres.

Resolução: 
"""

smeters = float(input('Insert square meters: '))

print('{0} square meters are equals {1} acres.'.format(smeters, (smeters * 0.000247)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""