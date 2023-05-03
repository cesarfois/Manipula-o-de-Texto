# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

with open('doc.txt', 'r+', encoding='utf-8') as arquivo:
    print(arquivo.name)
    temp_Arquivo = arquivo.read()
    name = arquivo.name + ';'

with open('cesar.txt', 'a', encoding='utf-8') as arquivo:

    arquivo.write(name)
    arquivo.write(temp_Arquivo)    
    

with open('cesar.txt', 'r+', encoding='utf-8') as a:
    print(a.read())




    
   
    
    
    # # iterando as linhas
    # for i in arquivo:
    #     # string.replace(oldvalue, newvalue, count)
    #     i = i.replace('linha', 'novo', 1)
    #     print(i, end='')


