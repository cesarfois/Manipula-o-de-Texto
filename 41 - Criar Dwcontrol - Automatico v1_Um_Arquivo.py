# PComo Usar Watchdog
#https://www.youtube.com/watch?v=jyE-MJRwsqo&t=1s


import os
import time
import csv
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def on_created(event):
    source = "C:/Users/DDR4/Desktop/pasta_a/"
    print("\033[1;33m" + "Novo Documento Creado identificado no seguinte endereço: " + "\033[1;39m" + source  )
    destination = "C:/Users/DDR4/Desktop/pasta_b/"
    allfiles = os.listdir(source)
    print(allfiles)

    #Le o arquivo de dados
    
   
    #Le o nome do documento
    with open("C:/Users/DDR4/Desktop/pasta_a/doc.txt", 'r', encoding='utf-8') as arquivo:
        #tipo_arquivo = os.path.splitext(arquivo.name)[1]
        #print(tipo_arquivo.lstrip("."))
        namefull = os.path.basename(arquivo.name)
        print(namefull)
        name = os.path.splitext(namefull)[0]


    
     
    # Abre o arquivo de indexação, procura a correspondencia e salva na lista
    lista = []
    with open('indexadores.csv', mode='r') as file:
        data_csv = csv.reader(file, delimiter=';')
        for i, linha in enumerate(data_csv):
            print(i, linha)
            if linha[0] == namefull:  
                print('achei')
                for j in linha:
                    lista.append(j)

    # Cria o arquivo dwcontrol
    with open(f'C:/Users/DDR4/Desktop/pasta_b/{name}.dwcontrol', 'w', encoding='utf-8') as arquivo:


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
    # iterate todos os arquivos e mover para o destino 

    # for f in allfiles:
    #     src_path = os.path.join(source, f)
    #     dst_path = os.path.join(destination, f)
    #     shutil.move(src_path, dst_path)

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

    path = r'C:\Users\DDR4\Desktop\pasta_a'
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

try:
    print("\033[0;32m" + "Monitorando a pasta seleccionada")
    while True:        
        time.sleep(1)
except KeyboardInterrupt:
    print("\033[1;31m" + 'Monitoramento cancelado' + "\033[1;39m")
    observer.stop()
observer.join()












# <ControlStatements xmlns="http://dev.docuware.com/Jobs/Control" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

# <Page>
# <Field dbName="EMPRESA" type="Text" value="Peters Engineering"/>
# <Field dbName="RESPONSAVEL" type="Text" value="Construction"/>
# <Field dbName="REVISOR" type="Text" value="Area determination"/>
# <Field dbName="TIPO_DE_DOCUMENTO" type="Text" value="invoice"/>

# </Page>
# </ControlStatements>