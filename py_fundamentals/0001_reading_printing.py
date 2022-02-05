"""Enunciado: Faça um programa que leia um número inteiro e o imprima.



Resolução: 
"""
while True:

   try:

       print(number := int(input('Insert value: ')))

       if number == 0:

           break

   except:

       print('The number must be an integer!')

       continue



"""Comentário: Criei um loop infinito que se encerra apenas com uma entrada válida. Utilizei o operador walrus (':=') para retornar e atribuir uma variável ao mesmo tempo. Se a entrada não for válida, o programa indica uma mensagem de alerta e solicita novamente uma entrada válida."""
