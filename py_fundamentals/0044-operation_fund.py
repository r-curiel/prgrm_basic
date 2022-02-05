"""
Enunciado: Receba a altura do degrau de uma escada e a altura que o usuário deseja 
alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para 
atingir seu objetivo.

Resolução: 
"""

staircase = int(input("Step height (cm): "))

height = int(input("Height that you want (m): "))

print("You will need to climb %.0f steps." % (height * 100 / staircase))

"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações.
"""