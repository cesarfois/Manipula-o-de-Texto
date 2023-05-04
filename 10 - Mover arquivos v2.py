# import os
# import shutil
# os.rename("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# os.replace("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

import os
import shutil


source = "C:/Users/DDR4/Desktop/pasta_a/"
destination = "C:/Users/DDR4/Desktop/pasta_b/"

arquivo = 'Novo Documento de Texto.txt'

print(f"{destination}notfound/{arquivo}")

shutil.move(f"{source}{arquivo}", f"{source}notfound/{arquivo}")

# if os.path.isdir(r'C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2'):      
#     shutil.move(r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\cesar.txt", r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2\doc2.txt")
# else:
#     os.mkdir('pasta2') 
#     shutil.move(r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\doc.txt", r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2\doc2.txt")