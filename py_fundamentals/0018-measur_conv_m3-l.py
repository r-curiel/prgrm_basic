"""
Enunciado: Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em 
litros. A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume 
em metros cúbicos.

Resolução: 
"""

cubcs = int(input('Insert cubic meters: '))

print('{0} cubic meters are equals {1} liters'.format(cubcs, (cubcs * 1000)))


"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""