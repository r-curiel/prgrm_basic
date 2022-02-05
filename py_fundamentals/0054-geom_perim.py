"""
Enunciado: Faça um programa para ler as dimensões de um terreno (comprimento C e 
largura L), bem como o preço do metro de tela. Imprima o custo para cercar este 
terreno com a tela.

Resolução: 
"""

width = float(input('Insert the width: ')) * 2

height = float(input('Insert the height: ')) * 2

price = float(input('Price per meter of the fence: '))


print('Total to pay: ${0}'.format((width + height) * price))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno 
do resultado das operações.
"""