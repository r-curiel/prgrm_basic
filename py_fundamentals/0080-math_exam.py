"""
Enunciado: Faça uma prova de matemática para crianças que estão aprendendo a somar 
números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre 
na tela a pergunta: qual é a soma de a + b, onde n e b são os números aleatórios. Peça a 
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas 
corretas, além de quantas vezes o aluno acertou.

Resolução: 
"""

import random

correct = 0
question = 1

while True:
   status = input('Press ENTER to start - or 0 to exit')
   try:
       if int(status) == 0:
           break
   except:
       ard, brd = [random.randint(1, 100) for _ in range(2)]

       answer = int(input('Question {0}:\n{1} + {2} = ??'.format(question, ard, brd)))
      
       print('Wow! Correct!' if answer == (ard + brd) else 'No no no :/')

       if answer == (ard + brd):
           correct += 1

       question += 1


print('\nResults:')
print('Total questions: {0}'.format(question))
print('Correct answers: %.d - %.2f%%' % (correct, (correct / question * 100)))
print('Incorrect answers: %.d - %.2f%%' % ((question - correct), (100 - (correct / question * 100))))


"""
Comentário: Para gerar os números das operações foi utilizada a biblioteca random. 
Verificação do tipo de procedimento adotado (iniciar a prova ou sair) através do 
tratamento de erros no caso de se tentar transformar em int o comando \n (enter). Após 
realizadas as operações, há a demonstração dos resultados com número de questões, acertos
 e erros, ambos em quantidade e percentual.
 """