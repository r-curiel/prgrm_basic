"""Enunciado: Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

Resolução: 
"""

def convert(seconds):
   seconds = seconds % (24 * 3600)
   hour = seconds // 3600
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60

   return "%02d:%02d:%02d" % (hour, minutes, seconds)


n = int(input("Seconds: "))

print(convert(n))

"""
Comentário: Como destaque, há a criação de uma função que trabalha horas. Nela, há o 
nivelamento para que a entrada seja restrita ao limite de 24 horas, na sequência, a 
geração de horas, minutos e segundos, seguido da impressão do resultado. Como fator 
adicional, há o procedimento de atualização dos segundos a medida que as horas e minutos 
são gerados.
"""