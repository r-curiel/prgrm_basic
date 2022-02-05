"""
Enunciado: Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado 
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça 
um programa em que o usuário entre com o valor e o estado destino do produto e o programa
 retorne o preço final do produto acrescido do imposto do estado em que ele será vendido.
  Se o estado digitado não for válido, mostrar uma mensagem de erro.

Resolução: 
"""


location = input('Enter the State (MG / SP / RJ / MS): ').lower()
price = float(input('Enter the value: '))

indexes = {'mg': 1.07, 'sp': 1.12, 'rj': 1.15, 'ms': 1.08}

if location.lower() in indexes:
   print(f'Final price: {round(indexes.get(location) * price, 2)}')
else:
   raise ValueError("The state is not valid.")


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações. Como diferencial, de acordo com o pedido do enunciado, a função 
raise permite mostrar uma mensagem de erro personalizada caso o Estado não seja válido.
"""