"""
Enunciado: Faça um programa que leia 2 notas de um aluno, verifique se as notas são 
válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, 
um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve 
ser informado ao usuário e o programa termina.

Resolução: 
"""

from numpy import mean


nbrs = [float(input(f"Insert the {n + 1}/2 number: ")) for n in range(2)]

print(f'The average is {mean(nbrs)}' if all([10 >= x >= 0 for x in nbrs]) else "Invalid Entry.")


"""
Comentário: Foi utilizada a função mean (média) da biblioteca numpy. A entrada dos dados
 foi feita através de uma list comprehension. O retorno consistiu na média dos valores 
 das notas após uma verificação com 'all' se todos elementos da lista atendiam à 
 restrição levantada.
"""