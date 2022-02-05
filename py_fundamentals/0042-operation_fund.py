"""Enunciado: Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendose que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.

Resolução: 
"""

salary = float(input("Insert your salary: "))

print("%.2f" % (salary * 1.05 * 0.93))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""