"""
Enunciado: Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A 
primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média 
do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser 
igual ou superior a 6 pontos.

Resolução: 
"""


from numpy import mean


peso = [1, 1, 2]

media = mean([int(input("Insert a number: ")) * x for x in peso])

print(f"Your average is {round(media,2)} and ", "you are approved!" if media >= 6 else "you are approved!")


"""
Comentário: A resolução do código consistiu na coletada das notas individuais, seguida 
da atribuição da ponderação e armazenamento das mesmas em uma lista. O retorno traz a 
média arredondada em duas casas decimais e o teste se o aluno foi ou não aprovado.
"""