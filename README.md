# operadores-aritmeticos

Operadores Aritméticos são os símbolos utilizados para realização de operações matemáticas.

Os operadores usados em Python divergem dos operadores padrões da matemáticas, mas são similares aos operadores utilizados em outras linguagens de programação.

Breve explicação dos Operadores e suas funcionalidades:

* Adição............ +
* Subtração......... -
* Multiplicação..... *
* Divisão Inteira... //
* Divisão Decimal... /
* Exponenciação..... **
* Resto Divisão..... %

Dos operadores apresentados acima, os únicos que divergem do padrão matemático são o "/" , "//" e o "%".  
"/" - é utilizado para retornar o resultado da divisão em número decimal ou float. ex 5 / 2 = 2.5.  
"//" - é utilizado para retornar o resultado da divisão em número inteiro, arredondando caso o resultado seja decimal. ex 5 // 2 = 2.  
"%" é utilizado para retornar o resultado do resto de uma divisão. ex 5 % 2 = 1

## 01.soma_inteiros.py

"Este exercício consiste na criação de duas variáveis, de nomes "a" e "b", cujos valores serão digitados pelo usuário. Como os valores digitados para a linguagem Python são, inicialmente, armazenados em forma de texto (string), e textos não podem ser somados, precisaremos convertê-los em números inteiros para atribuí-los às respectivas variáveis.
Em seguida, é criada a variável "soma", que deverá receber a soma das variáveis "a" e "b".
Por fim, utiliza-se o comando print para apresentar ao usuário o resultado da operação armazenada na variável "soma"."

## 02.reais_dolares.py

O exercício pede que o usuário insira um valor em reais e a taxa de câmbio para a conversão em dólares. É importante notar que, em Python, os valores decimais devem ser inseridos com um ponto (.) e não uma vírgula (,).
Em seguida, uma operação de divisão realiza a conversão.
Por fim, o resultado é exibido ao usuário. O caractere f no print formata o texto de saída, enquanto a expressão :.2f limita o resultado a apenas duas casas decimais, como no exemplo $ 4.10.

## 03.dolares_reais.py

O exercício segue o mesmo padrão do exercício anterior de coversão de moeda "02.reais_dolares.py".
Para compreensão verifique explicação do exercício anterior.

## 04.metros_centimetros.py

Exercício simples que recebe o valor em metros digitado pelo usuário, realiza a conversão e armazena na variável centimetros.  
Apresenta ao usuário o resultado da conversão em centímetros.

## 05.centimetros_metros.py

O exercício segue o mesmo padrão do exercício anterior de coversão de medidas "metros_centimetros.py".  
Para compreensão verifique explicação do exercício anterior.

## 06.foto_qualidade.py

Este exercício solicita ao usuário o tamanho em Gigabytes e atribui o valor à variável pen_drive.
Em seguida, converte o tamanho do Pen Drive de GB para MB e armazena na variável pen_drive_mb. Lembre-se de que a conversão de unidades de medida é realizada através da multiplicação do valor por 1024.
Ele realiza o cálculo da capacidade de armazenamento do Pen Drive e armazena em qtd_fotos, apresentando, por fim, ao usuário a quantidade aproximada de fotos que podem ser armazenadas.
O :.0f garante que não sejam exibidos números decimais, pois não é possível armazenar partes de uma imagem.

## 07.tempo_download.py

Este exercício solicita ao usuário o tamanho do arquivo a ser baixado e o armazena na variável tamanho_arquivo.
Em seguida, converte o tamanho do arquivo de MB para KB e o armazena na variável tamanho_arquivo_kb.
Ele realiza o cálculo do tempo necessário para baixar o arquivo, levando em conta que são baixados 256 KB/s.
Por fim, apresenta ao usuário o tempo aproximado necessário para o download do arquivo, em segundos.

## 08.volume_concreto.py

