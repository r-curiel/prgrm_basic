"""
Enunciado: Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

Resolução: 
"""

value_hour = float(input("Insert the hour's value: "))

work_hour = int(input("Insert the time of the work: "))

print(f"$ %.2f" % ((value_hour * work_hour) * 1.1))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""