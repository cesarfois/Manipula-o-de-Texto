arquivo = open('doc.txt', 'r', encoding='utf-8' )


for i in arquivo:
    
    print(i, end="")


arquivo.close()