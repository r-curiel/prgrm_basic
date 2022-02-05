"""Enunciado: Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 
“Número inválido”. Se o número for positivo, calcular o logaritmo deste numero.

Resolução: 
"""

import math


num = int(input('Insert a number: '))

print(f"It's log is {round(math.log10(num), 3)}" if num > 0 else "Invalid entry.")


"""
Comentário: Calculado logaritmo na base 10 através da função log10() da biblioteca math.
"""