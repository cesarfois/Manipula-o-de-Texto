# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

with open('doc.txt', 'r+', encoding='utf-8') as arquivo:
    temp_Arquivo = arquivo.read()

with open('cesar.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(temp_Arquivo)

with open('doc.txt', 'r+', encoding='utf-8') as a:
    print(a.read())




    
   
    
    
    # # iterando as linhas
    # for i in arquivo:
    #     # string.replace(oldvalue, newvalue, count)
    #     i = i.replace('linha', 'novo', 1)
    #     print(i, end='')


