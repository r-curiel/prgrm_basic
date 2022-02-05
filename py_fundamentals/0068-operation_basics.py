"""
Enunciado: Faça um programa que mostre ao usuário um menu com 4 opções de operações 
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa 
então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.

Resolução: 
"""

option = int(input('1 - Adition\n2 - Subtraction\n3 - Multiplication\n4 - Division\nChoose an operation: '))


if 0 < option < 5:
   num = [int(input(f'Insert the {x+1} of 2 numbers: ')) for x in range(2)]
   if option == 1:
       print(num[0] + num[1])
   elif option == 2:
       print(num[0] - num[1])
   elif option == 3:
       print(num[0] * num[1])
   elif option == 4:
       print(num[0] / num[1])
else:
   print('Invalid entry.')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""