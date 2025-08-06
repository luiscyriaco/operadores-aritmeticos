""" 04. Conversão de medidas: faça um programa que solicite uma distância em metros, 
 calcule e exiba a distância em centímetros.
"""

# Criação da variável metros que receberá o valor em metros a ser convertido para centímetros.
metros = float(input("Digite o valor da distância em metros: "))

# Convertendo a distâcia de metros em centímetros
centimetros = metros * 100

# Apresentando ao usuário o resultado da conversão de metros para centímetros
print(f"{metros}m é equivalente a {centimetros}cm")
