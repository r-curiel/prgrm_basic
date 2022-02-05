"""
Enunciado: Escreva um programa que, dada a idade de um nadador, classifique-o em uma 
categoria.

Resolução: 


age = int(input('Insert the age: '))

if 4 < age < 8:
   print('Kids A')
if 7 < age < 11:
   print('Kids B')
if 10 < age < 14:
   print('Teens A')
if 13 < age < 18:
   print('Teens B')
if age >= 18:
   print('Senior')

Comentário: A resolução do código consistiu na coleta das informações e retorno do resultado das operações.


Resolução alternativa: 
"""

dados = {'Kids A': range(4, 8), 'Kids B': range(8, 11),
        'Teens A': range(11, 14), 'Teens B': range(14, 18),
        'Senior': range(18, 200)}

age = int(input('Insert the age: '))

for cat, ages in dados.items():
   if age in ages:
       print(cat)


"""
Comentário: A resolução alternativa aplica uma verificação no range das idades. O loop
 for retorna a categoria correspondente ao conjunto de idades.
"""