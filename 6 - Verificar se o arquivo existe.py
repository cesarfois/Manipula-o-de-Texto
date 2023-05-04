import os

caminho_arquivo = 'caminho/do/arquivo.txt'


if os.path.exists(caminho_arquivo):
    # o arquivo existe, então podemos acessá-lo
    with open(caminho_arquivo, 'r') as arquivo:
         print('dfdasdf')
        # faça alguma coisa com o arquivo
else:
     print('O arquivo não existe')

    # o arquivo não existe, então não podemos acessá-lo
   
