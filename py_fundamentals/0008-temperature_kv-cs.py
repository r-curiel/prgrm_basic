"""
Enunciado: Leia uma temperatura em graus Kelvin e apresente-a convertida 
em graus Celsius. A fórmula de conversão ê: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

Resolução: 
"""

kelvin = float(input('Insert kelvin temperature: '))

print(f'From {kelvin} kelvin to {(kelvin - 273.15)} celsius.')

"""
Comentário: Atribuição simples de variável, retornando o input no print, 
diretamente com a operação solicitada.
"""