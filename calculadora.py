# -*- coding: utf-8 -*-
""" máquina de cálculos matemáticos
"""
print("----- MÁQUINA DE CÁLCULOS -----")

fechar = False

while fechar == False:

	num1 = input("Digite o primeiro algarismo: ")
	num1 = float(num1)
	operador = input("Digite o operador(+, -, /, *, **): ")
	num2 = input (" Digite o segundo algarismo: ")
	num2 = float(num2)

	# + soma
	if operador == "+":
		operacao = num1 + num2

	# - subtração
	if operador == "-":
		operacao = num1 - num2

	# / divisão
	if operador == "/":
		operacao = num1 / num2

	# * multiplicação
	if operador == "*":
		operacao = num1 * num2

	# ** potenciação
	if operador == "**":
		operacao = num1 ** num2


	print("Resultado: ")
	print(operacao)

	sair = input("Deseja sair? (n/s): ")
	if sair == "s":
		fechar = True

