"""
Enunciado: Calcule as raízes da equação de 2° grau.

Resolução: 
"""

eq = {'a': 0, 'b': 0, 'c': 0}

for x in eq:
   eq[x] = int(input(f"Enter the '{x}' element: "))

if eq.get('a') != 0:
   print('Your equation is: {0}x² + {1}x + {2} = 0'.format(*eq.values()))
   delta = eq.get('b') ** 2 - 4 * eq.get('a') * eq.get('c')
   if delta < 0:
       print('There is no root!')
   elif delta == 0:
       print('There is only one root: %.2f' % (-eq.get('b') / (2 * eq.get('a'))))
   else:
       x1 = ((-eq.get('b') + (delta ** 0.5)) / (2 * eq.get('a')))
       x2 = ((-eq.get('b') - (delta ** 0.5)) / (2 * eq.get('a')))
       print('x1 = %.2f and x2 = %.2f' % (x1, x2))
else:
   print('That is not a second degree equation!')

"""
Comentário: A resolução do código consistiu na criação de um dicionário para comportar 
os elementos da equação. Foram realizados vários testes para verificar os parâmetros de
 demonstração do resultado, isto é, se os valores compõem uma equação de segundo grau, 
 se o delta equivale a zero para retornar apenas uma raiz ou então como devem ser 
 demonstradas as duas raízes distintas.
 """