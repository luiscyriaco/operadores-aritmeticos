# 6. Uma foto de boa qualidade tem, em média, 10MB. Faça um programa que solicite a 
# capacidade de um pen-drive em GB e determine a quantidade de fotos que pode ser 
# armazenada nele.

# Criação da variável pen_drive e solicitação da capacidade do Pen Drive ao usuário.
pen_drive = float(input("Insira a capacidade do Pen Drive em GB: "))

# Convertendo unidade de medida do Pen Drive de GB para MB.
pen_drive_mb = pen_drive * 1024

# Calculando a capacidade de armazenamento do Pen Drive para fotos de 10MB.
qtd_fotos = pen_drive_mb / 10

# Apresentado ao usuário a capacidade de armazenamento de fotos de 10MB para o Pen Drive.
print(f"O Pen drive de {pen_drive:.0f}GB, é capaz de armazenar aproximadamente {qtd_fotos:.0f} fotos")
