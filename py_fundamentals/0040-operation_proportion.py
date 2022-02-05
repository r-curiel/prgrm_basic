"""
Enunciado: Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que 
solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que 
deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

Resolução: 
"""

days = int(input("How many days did he work? "))

print("Salary: $ %.2f" % ((days * 30) * 0.92))

"""
Comentário: A resolução do código dividiu o total do prêmio proporcionalmente entre 
os ganhadores."""
