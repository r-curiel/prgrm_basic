"""
Enunciado: Leia uma velocidade em m/s (metros por segundo) e apresente-a 
convertida em km/h (quilómetros por hora). A fórmula de conversão é: K = M * 3.6, 
sendo K a velocidade em km/h e M em m/s.

Resolução: 
"""

ms = int(input('Insert meters per second: '))

print(f'From {ms} m/s to {(ms * 3.6)} km/h')

"""
Comentário: Atribuição simples de variável, retornando o input no print, 
diretamente com a operação solicitada.
"""