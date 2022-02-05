"""
Enunciado: Leia um número fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o 
número é inválido.

Resolução: 
"""

number = int(input("Insert a number: "))

print(round((number ** 0.5), 2) if number > 0 else "Invalid entry!")

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""