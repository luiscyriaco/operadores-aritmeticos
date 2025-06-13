# 3.  Conversão de dólares: faça um programa que solicite a quantidade de sólares e a
#  taxa de conversão, calcule e exiba a quantidade em reais.

# Criando as variáveis que armazenarão o valor em dólares a ser convertido, e a taxa de câmbio.
dolares = float(input("Digite o valor em dólares a ser convertido $ "))
taxa = float(input("Digite a taxa de conversão para reais (ex. 6.10 para R$ 1.00 = 6.10: "))

# Realização do cáculo de conversão de dólar para real.
reais = dolares * taxa

# Apresentando ao usuário o valor convertido para dólares.
print(f"$ {dolares:.2f} dólares equivalem a R$ {reais:.2f}.")