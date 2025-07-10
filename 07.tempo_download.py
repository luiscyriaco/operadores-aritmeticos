# 7. Uma rede tem a velocidade de download de 256 KB/s. Faça um programa 
# que solicite o tamanho de um arquivo em MB, calcule e exiba quanto tempo
# será necessário para seu download.

# Solitando o tamanho do arquivo que será baixado em MB e armazenando na variável tamanho_arquivo
tamanho_arquivo = float(input(" Insira o tamanho do arquivo em MB: "))

# Converção do tamanho do arquivo de MB para KB.
tamanho_arquivo_kb = tamanho_arquivo * 1024

# Cálculo de tempo de download do arquivo.
tempo_download = tamanho_arquivo_kb / 256

# Apresentando o tempo de download do arquivo para o usuário.
print(f"Para o arquivo de {tamanho_arquivo:.0f}MB, o tempo de download será de {tempo_download:.0f} segundos.")
