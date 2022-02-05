"""
Enunciado: Faça um programa que receba dois números e mostre o maior. Se por acaso, 
os dois números forem iguais, imprima a mensagem números iguais.

Resolução: 
"""

nbrs = [float(input(f"Insert the {n+1}/2 number: ")) for n in range(2)]

print(f'The higher is {max(nbrs)}' if nbrs[0] != nbrs[1] else f'Equal numbers' if nbrs[0] == nbrs[1] else None)


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno 
do resultado das operações.
"""