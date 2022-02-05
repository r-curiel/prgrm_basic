"""
Enunciado: Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela
 equação: hipotenusa² = a² + b² . Faça um programa que receba os valores de 'a' e 'b' e 
 calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

Resolução: 
"""

a = int(input("Insert the 'a' number: "))

b = int(input("Insert the 'b' number: "))

print("%.2f" % ((a ** 2 + b ** 2) ** 0.5))

"""
Comentário: Atribuição simples de variável, retornando o input no print, diretamente 
com a operação solicitada.
"""