
#En vez de usar isto...
#arquivo = open('doc.txt', 'r', encoding='utf-8' )
#arquivo.close()

# Utilizamos with

with open('doc.txt', 'r+', encoding='utf-8') as arquivo:   
    
    
    # iterando as linhas
    for i in arquivo:
        # string.replace(oldvalue, newvalue, count)
        i = i.replace('linha', 'novo', 1)
        print(i, end='')
