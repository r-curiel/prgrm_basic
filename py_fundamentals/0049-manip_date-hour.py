"""
Enunciado: Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a
 duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo 
 horário (hora, minuto e segundo) do termino da mesma.

Resolução: 
"""

import datetime


print(f'Start time:')
inicio = f"{input('Date (dd/mm/aa): ')} {input('Hour (hh:mm): ')}"

print(f'\nEnd time:')
duration = [int(t) for t in input('Duration (hh:mm): ').split(":")]


datetime_inicio = datetime.datetime.strptime(inicio, '%d/%m/%y %H:%M')
delta = datetime.timedelta(hours=duration[0], minutes=duration[1])

delta_duracao = datetime_inicio + delta

print(f'End time: {delta_duracao}')

"""
Comentário: Manipulações de data e hora são um problema a parte. Diferente das 
manipulações convencionais, operar com data e hora demanda mais técnica e atenção. Foi 
utilizada a biblioteca datetime, recebendo os dados e já concatenando em um formato para 
cálculo do delta. Na sequência, houve a conversão dos dados recebidos em formato de data 
e tempo, conversão esta que possibilita a operação final que retorna a diferença de dias 
e horas.
"""