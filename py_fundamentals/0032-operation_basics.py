"""
Enunciado: Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
 escolhida. Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).

Resolução: 
"""

print('1 - Sum of two numbers')
print('2 - Subtraction between two numbers (higher by lower)')
print('3 - Product between two numbers')
print('4 - Division between two numbers (denominator must be different from 0)\n')

option = int(input('Insert an option: '))

if 0 < option < 5:
   num = [int(input(f'Insert the {x + 1} of 2 numbers: ')) for x in range(2)]
   if option == 1:
       print(num[0] + num[1])
   elif option == 2:
       if num[0] > num[1]:
           print(num[0] - num[1])
       else:
           print(num[1] - num[0])
   elif option == 3:
       print(num[0] * num[1])
   elif option == 4:
       if num[1] != 0:
           print(num[0] / num[1])
       else:
           print('Operation closed because the denominator are 0!')
else:
   print('Invalid entry.')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do
 resultado das operações.
 """