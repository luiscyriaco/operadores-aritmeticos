# 2. Conversão de reais em dólares: faça um programa que solicite a quantidade de reais e a
# taxa de conversão, calcule e exiba a quantidade de dólares. 

# Criando as variáveis que armazenarão o valor em reais a ser convertido, e a taxa de câmbio.
reais = float(input("Digite o valor em reais a ser convertido R$ "))
taxa = float(input("Digite a taxa de conversão para dólares (ex. 6.10 para R$ 1.00 = 6.10: "))

# Realização do cáculo de conversão de real para dólar.
dolares = reais / taxa

# Apresentando ao usuário o valor convertido para dólares.
print(f"R$ {reais:.2f} equivalem a $ {dolares:.2f} dólares.")