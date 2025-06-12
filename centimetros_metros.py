# Criação da variável centimetros que receberá o valor em centimetros a ser convertido para metros.
centimetros = float(input("Digite o valor da distância em centímetros: "))

# Convertendo a distâcia de centímetros em metros.
metros = centimetros / 100

# Apresentando ao usuário o resultado da conversão de centímetros para metros.
print(f"{centimetros}cm é equivalente a {metros}m")