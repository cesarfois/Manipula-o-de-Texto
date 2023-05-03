arquivo = open('doc.txt', 'r', encoding='utf-8' )


# Le uma linha
#print(arquivo.readline())


# Le todas as linhas linhas, Transformando numa lista.
print(arquivo.readlines())


arquivo.close()