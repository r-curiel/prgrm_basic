"""
Enunciado: Faça um programa que leia três números inteiros positivos e efetue o cálculo 
de uma das seguintes médias de acordo com um valor numérico digitado peto usuário.

Resolução: 
"""

option = int(input('1) Geometrical\n2) Weighted\n3) Harmonic\n4) Arithmetic \nEnter the method: '))

x, y, z = [int(input(f"Insert the {n+1} of 3 values: ")) for n in range(3)]

if option == 1:
   print(f'Geometrical result: {(x * y * z) ** (1 / 3)}.')
elif option == 2:
   print(f'Weighted result: {(x + 2 * y + 3 * z) / 6}.')
elif option == 3:
   print(f'Harmonic result: {1 / ((1/x) + (1/y) + (1/z))}.')
elif option == 4:
   print(f'Arithmetic result: {(x + y + z) / 3}.')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do
 resultado das operações. Como destaque, há o procedimento de entrada de valores 
 com a atribuição automática a cada uma das variáveis x, y e z.
 """