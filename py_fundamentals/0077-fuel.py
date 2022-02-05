"""
Enunciado: Leia a distância em Km e a quantidade de litros de gasolina consumida por um 
carro em um percurso. Calcule o consumo em Km/.

Resolução: 
"""

kilometer = float(input('Insert how many kilometers you have traveled: '))
liters = float(input('Insert how many liters was consumed: '))

kmltrs = kilometer / liters

if kmltrs < 8:
   print('Sell the car!')
elif 8 <= kmltrs <= 12:
   print('Economic!')
else:
   print('Super economic!')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do
resultado das operações.
"""