
import os
import time
import csv
import shutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# PATH MONITORING
source = "C:/Users/DDR4/Desktop/folder_In/"

# DESTINATION
destination = "C:/Users/DDR4/Desktop/folder_Out/" 

# INDEX_FILE
index_File = "C:/Users/DDR4/Desktop/Python Manipulação de Texto/indexadores.csv"


# Contadores
Count_Total = 0
Count_Index = 0
Count_Not_Found = 0



def on_created(event):
    
    print("\033[1;33m" + "New Document Created, path: " + "\033[1;39m" + source  ) 
    global Count_Total
    Count_Total += 1   
    namefull = os.path.basename(event.src_path)
    name = os.path.splitext(namefull)[0]
    
 

    # check if folder already exists # if folder doesn't exist then create it
    if not os.path.exists(f"{source}Not_Found"):        
        os.makedirs(f"{source}Not_Found")


         
    # Opens the index file, searches for the match and saves it to the list
    lista = []
    found_In_Base = False
    with open( f'{index_File}', mode='r') as file:
        data_csv = csv.reader(file, delimiter=';')
        for i, linha in enumerate(data_csv):
           # print(i,linha)
            if linha[0] == namefull:
                global Count_Index
                Count_Index += 1
                #print('found')
                found_In_Base = True
                for j in linha:
                    lista.append(j)
            
    if found_In_Base:
        # Move file to destination
        shutil.move(f"{source}{namefull}", f"{destination}{namefull}") 

        # Create file dwcontrol

        # ==================================================================================================
        # ***************************      START CREATION DWCONTROL   *************************************#
        #===================================================================================================

        with open(f'{destination}{name}.dwcontrol', 'w', encoding='utf-8') as arquivo:


        #OBRIGATORIO <ControlStatements xmlns="http://dev.docuware.com/Jobs/Control" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            arquivo.write("<ControlStatements xmlns=\"http://dev.docuware.com/Jobs/Control\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\n\n")
            arquivo.write("<Page>\n\n")

            
            arquivo.write(f"<Field dbName=\"NOME_ARQUIVO\" type=\"Text\" value=\"{lista[0]}\"/>\n")
            arquivo.write(f"<Field dbName=\"EMPRESA\" type=\"Text\" value=\"{lista[1]}\"/>\n")
            arquivo.write(f"<Field dbName=\"NO_DE_CONTRATO\" type=\"Text\" value=\"{lista[2]}\"/>\n")
            arquivo.write(f"<Field dbName=\"STATUS\" type=\"Text\" value=\"{lista[3]}\"/>\n")
            arquivo.write(f"<Field dbName=\"RESPONSAVEL\" type=\"Text\" value=\"{lista[4]}\"/>\n")
            arquivo.write(f"<Field dbName=\"REVISOR\" type=\"Text\" value=\"{lista[5]}\"/>\n")
            arquivo.write(f"<Field dbName=\"TIPO_DE_DOCUMENTO\" type=\"Text\" value=\"{lista[6]}\"/>\n")
        

            # Obrigatorio  
            arquivo.write("\n</Page>")
            arquivo.write("\n</ControlStatements>")

        # ==================================================================================================
        # ***************************      END CREATION DWCONTROL   ************************************** #
        #===================================================================================================
                 

    # If not found no file base, move to folder "Not_Found"

    if not found_In_Base and namefull != "Not_Found": # ignore Folder 
        global Count_Not_Found
        Count_Not_Found += 1      
        data_hora_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")        
        if os.path.exists(f"{source}{namefull}"):
            shutil.move(f"{source}{namefull}", f"{source}Not_Found/{data_hora_atual}{namefull}") 
            print(f'Not found file: , {namefull}')

    
def on_deleted(event):
    print("Deletado")

def on_modified(event):
    print('modificado')

def on_moved(event):
    print('movido')


if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    # Calling functions
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    # Path monitoring
    path = "C:/Users/DDR4/Desktop/folder_In/"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
try:
    print("\033[0;32m" + "Monitorando a pasta seleccionada")
    while True:        
        time.sleep(1)
except KeyboardInterrupt:    

    # 
    data_hora_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")  
    with open(f'log.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write('\n'+'='*70 + ' '*15 +'\n      Date end execution: ' + data_hora_atual + '\n' + '='*70)
        arquivo.write(f'\nTotal documents imported: {Count_Total}\n')
        arquivo.write(f'Indexed documents: {Count_Index}\n')
        arquivo.write(f'Documents not found, not indexed: {Count_Not_Found}\n')
    print("\033[1;31m" + 'Monitoramento cancelado' + "\033[1;39m")
    observer.stop()
observer.join()
