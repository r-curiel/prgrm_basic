"""
Enunciado: A importância de R$ 780.000,00 será dividida entre très ganhadores de um 
concurso.

Sendo que da quantia total:

•O primeiro ganhador receberá 46%;

•O segundo receberá 32%;

•O terceiro receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores:

Resolução: 
"""

total = 780_000

print("First winner: $ %.2f" % (total * 0.46))

print("Second winner: $ %.2f" % (total * 0.32))

print("Third winner: $ %.2f" % (total * (1 - 0.32 - 0.46)))


print(((total * 0.46) + (total * 0.32) + (total * (1 - 0.32 - 0.46))))

"""
Comentário: A resolução do código dividiu o total do prêmio proporcionalmente entre 
os ganhadores.
"""