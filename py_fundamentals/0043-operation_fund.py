"""
Enunciado: Escreva um programa de ajuda para vendedores. A partir de um valor total 
lido, mostre:

• o total a pagar com desconto de 10%;

• o valor de cada parcela, no parcelamento de 3x sem juros;

• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)

• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

Resolução: 
"""

value = float(input("Insert the sales' value: $"))

print("Total to receive with 10%% of discount: $ %.2f" % (value * 0.9))

print("Divided in 3x: $ %.2f" % (value / 3))

print("For the sale in cash, the seller will receive: $ %.2f" % (value * 0.05 * 0.9))

print("For the divided sale, the seller will receive: $ %.2f" % (value * 0.05))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do
 resultado das operações.
"""