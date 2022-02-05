"""
Enunciado: Leia uma distância em quilómetros e apresente-a convertida em milhas. A fórmula de conversão é: M = K/1.61 sendo K a distância em quilómetros e M em milhas.

Resolução: 
"""

km = int(input('Insert kilometers distance: '))

print(f'From {km} km to {round((km / 1.61), 4)} miles.')

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""