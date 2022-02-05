"""
Enunciado: Leia um valor de volume em litros e apresente-o convertido em metros cúbicos 
m3. A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em 
metros cúbicos.

Resolução: 
"""

liters = float(input('Insert liters: '))

print('{0} liters are equals {1} cubic meters.'.format(liters, (liters / 1000)))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""