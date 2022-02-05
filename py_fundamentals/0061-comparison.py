"""
Enunciado: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. 
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso 
contrário imprima: Empréstimo concedido.

Resolução: 
"""

num1 = int(input("Insert your salary: "))

num2 = int(input("Insert installment amount: "))

print("Loan not granted." if num2 > (num1 * 0.2) else "Loan granted.")


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""