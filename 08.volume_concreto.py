# Uma prefeitura precisa concretar o piso de uma praça. Para isso, vai comprar o concreto
# de uma empresa que solicita os seguintes dados: o comprimento e a largura da praça e a 
# espessura das placas de concreto que serão feitas. Com esses dados, eles calculam o volume
# de concreto, em metros cúbicos, necessário para realizar a obra. Sabendo o volume total,
# eles precisam calcular quantos caminhões serão necessários para transportar esse concreto,
# sabendo que cada caminhão carrega 2,5 m³ de concreto.vFaça um programa que solicite o 
# comprimento, a largura da praça, a espessura que se deseja para as placas de concreto, 
# calcule o volume total e quantos caminhões serão necessários e exiba o volume total e
# a quantidade de caminhões.

# Solicita os dados necessários para o cálculo do volume de concreto e a quantidade de caminhões.
comprimento =   float(input("Digite o comprimento da praça, em metros: "))
largura = float(input("Digite a largura da praça, em metros: "))
espessura = float(input("Digite a espessura do concreto, em mestros: "))
# Calcula o volume de concreto necessário e a quantidade de caminhões.
volume = comprimento * largura * espessura
caminhoes = volume // 2.5
print(f"Serão necessários para execução do piso {volume:.2f} m³ de concreto.")
print(f"Que deverão ser transportados em {caminhoes:.0f} caminhões.")
