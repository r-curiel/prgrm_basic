"""
Enunciado: Leia uma temperatura em graus Fahrenheit e apresente-a convertida 
em graus Celsius. A fórmula de conversão ê: C = 5.0* (F - 32.0)/9.0, sendo C a 
temperatura em Celsius e F a temperatura em Fahrenheit.

Resolução: 
"""

fahrenhiet = float(input('Insert fahrenhiet temperature: '))

print(f'From {fahrenhiet} to {(5.0 * (fahrenhiet - 32)/9.0)} celsius.')

"""
Comentário: Atribuição simples de variável, retornando o input no print, 
diretamente com a operação solicitada.
"""