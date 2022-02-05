"""Enunciado: Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto 
se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por 
exemplo: 1988, 1992, 1996...

Resolução: 
"""

year = int(input('Insert a year: '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
   print('Leap year')
else:
   print("It's not a leap year!")


"""
Comentário: A resolução do código consistiu em estabelecer duas condições para 
identificar se um ano é ou não bissexto: ser múltiplo de 400 ou então ser múltiplo de 4 
mas não de 100.
"""