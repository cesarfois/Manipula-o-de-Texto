# import os
# import shutil
# os.rename("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# os.replace("caminhoa/arquivo.txt", "caminhob/arquivo.txt")
# shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

#https://www.geeksforgeeks.org/how-to-move-all-files-from-one-directory-to-another-using-python/ 


import os
import shutil

source = "C:/Users/DDR4/Desktop/pasta_a"
destination = "C:/Users/DDR4/Desktop/pasta_b/"

# listar todos os arquivos

allfiles = os.listdir(source)

# iterate todos os arquivos e mover para o destino 

for f in allfiles:
    src_path = os.path.join(source, f)
    print("source =", src_path)
    dst_path = os.path.join(destination, f)
    print("Destination =", dst_path)
    shutil.move(src_path, dst_path)

