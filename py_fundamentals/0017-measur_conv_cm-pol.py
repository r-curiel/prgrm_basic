"""
Enunciado: Leia um valor de comprimento em centímetros e apresente-o convertido em 
polegadas. A fórmula de conversão é: P = C/2,54 sendo C o comprimento em centímetros e 
P o comprimento em polegadas.

Resolução: 
"""

centimeters = float(input('Insert centimeters: '))

print(f'{centimeters} centimeters are equals {round((centimeters / 2.54), 4)} inches.')

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""