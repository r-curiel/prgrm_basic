"""
Enunciado: Leia uma velocidade em km/h (quilómetros por hora) e apresente-a 
convertida em m/s (metros por segundo). A fórmula de conversão ê: Aí = AT/3.6, 
sendo K a velocidade em km/h e M em m/s.

Resolução: 
"""

kmh = int(input('Insert the speed in kilometers: '))

print(f'From {kmh} km to {round((kmh/3.6),2)} m/s.')

"""
Comentário: Atribuição simples de variável, retornando o input no print, 
diretamente com a operação solicitada.
"""
