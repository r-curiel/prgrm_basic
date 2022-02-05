"""
Enunciado: Faça um programa que receba a altura e o sexo de uma pessoa e calcule e 
mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):

• Homens: (72.7 * h) - 58
• Mulheres: (62,1* h) - 44,7

Resolução: 
"""

gender = input("Insert your sex (m/f): ")

gender = gender[0].lower()


height = float(input("Insert your height: "))


if gender == 'm':
   print("Your ideal weight is: {0:.4}kg".format((72.7 * height) - 58))
elif gender == 'f':
   print("Your ideal weight is: {0:.4}kg".format((62.1 * height) - 44.7))
else:
   print("Invalid entry.")


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações. Como diferencial, observa-se o tratamento da entrada de gênero, 
podendo receber qualquer caractere (tornado em minúsculo e aplicado a correspondência).
 Operações diferentes para male ou female e apresentação de entrada inválida para 
 entradas que não satisfazem nenhum critério.
 """