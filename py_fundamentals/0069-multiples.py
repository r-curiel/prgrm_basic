"""
Enunciado: Faça um programa para verificar se um determinado número inteiro e divisívelpor 3 ou 5, mas não simultaneamente pelos dois.

Resolução: 
"""

num = int(input('Insert a number: '))

if num % 3 == 0:
   if num % 5 == 0:
       print('The number is divisible by 3 and 5!')
   else:
       print('The number is divisible only by 3 and not 5!')
elif num % 5 == 0:
   print('The number is divisible only by 5 and not 3!')
else:
   print("The number isn't divisible by 3 or 5")


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""