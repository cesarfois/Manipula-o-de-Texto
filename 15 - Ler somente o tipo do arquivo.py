import os

nome_arquivo = "exemplo.txt"

tipo_arquivo = os.path.splitext(nome_arquivo)[1]

print("O tipo do arquivo é:", tipo_arquivo)
