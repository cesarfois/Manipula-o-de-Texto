
#En vez de usar isto...
#arquivo = open('doc.txt', 'r', encoding='utf-8' )
#arquivo.close()

# Utilizamos with

with open('doc.txt', 'r+', encoding='utf-8') as arquivo:   
    
    
    # iterando as linhas
    for i in arquivo:
        print(i, end='')
