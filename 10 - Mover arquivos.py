# import os
# import shutil
# os.rename("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# os.replace("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

import os
import shutil


if os.path.isdir(r'C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2'):      
    shutil.move(r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\cesar.txt", r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2\doc2.txt")
else:
    os.mkdir('pasta2') 
    shutil.move(r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\doc.txt", r"C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2\doc2.txt")