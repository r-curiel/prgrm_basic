"""
Enunciado: Leia uma temperatura em graus Celsius e apresente-a 
convertida em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0, 
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

Resolução: 
"""

celsius = float(input('Insert celsius temperature: '))

print(f'From {celsius} to {(celsius * (9.0/5.0)+32)} fahrenhiet.')


"""
Comentário: Atribuição simples de variável, retornando o input no print, 
diretamente com a operação solicitada.
"""