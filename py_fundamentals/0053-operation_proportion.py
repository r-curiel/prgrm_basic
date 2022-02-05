"""
Enunciado: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser 
repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça 
um programa que leia quanto cada apostador investiu, o valor do prémio, e imprima 
quanto cada um ganharia do prêmio com base no valor investido.

Resolução: 
"""

vector1 = [float(input("Insert the {0}/3 player: ".format(n+1))) for n in range(3)]

for n in range(0, 3):

   print("The {0}/3 player will receive: {1:.4}% of the reward.".format((n+1), ((vector1[n] / sum(vector1)) * 100)))


"""
Comentário: A resolução do código consistiu na coleta dos valores das apostas. O 
retorno demonstra o percentual de participação no recebimento do prêmio.
"""