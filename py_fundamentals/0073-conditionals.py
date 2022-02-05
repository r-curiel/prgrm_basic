"""
Enunciado: Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou 
não se aposentar. As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

Resolução: 
"""

age = int(input('Age: '))
workyr = int(input('Years of work: '))

if age >= 65 or workyr >= 30:
   print('Allowed to retire')
elif age >= 60 and workyr >= 25:
   print('Allowed to retire')
else:
   print('Not allowed to retire')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""