"""
Enunciado: Faça um programa que leia um número inteiro positivo de três dígitos 
(de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido.

Resolução: 
"""

number = str(input("Insert a number: "))


print("Read number: %s" % (number))

number = number[::-1]

print("Generated number: %s" % (number))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno 
do resultado das operações.
"""