# PComo Usar Watchdog
#https://www.youtube.com/watch?v=jyE-MJRwsqo&t=1s


import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def on_created(event):
    print("creado")
    source = "C:/Users/DDR4/Desktop/pasta_a/"
    destination = "C:/Users/DDR4/Desktop/pasta_b/"
    allfiles = os.listdir(source)

    #Le o arquivo de dados
    
   
    #Le o nome do documento
    with open("C:/Users/DDR4/Desktop/pasta_a/doc.txt", 'r', encoding='utf-8') as arquivo:
        tipo_arquivo = os.path.splitext(arquivo.name)[1]
        print(tipo_arquivo.lstrip("."))
        name = os.path.basename(arquivo.name)
        name = os.path.splitext(name)[0]

    with open('indexadores.csv', 'r', encoding='utf-8') as indexador:
        indexador = indexador.readlines()
        print(indexador)
        for i in indexador:
            if name == indexador[i]:
                print(indexador[i])
                pass

    # Cria o arquivo dwcontrol
    with open(f'C:/Users/DDR4/Desktop/pasta_b/{name}.dwcontrol', 'w', encoding='utf-8') as arquivo:
        
        #name = name.replace(source, '').lstrip()
        print(name)
        
    #OBRIGATORIO <ControlStatements xmlns="http://dev.docuware.com/Jobs/Control" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        arquivo.write("<ControlStatements xmlns=\"http://dev.docuware.com/Jobs/Control\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\n\n")
        arquivo.write("<Page>\n\n")

        arquivo.write(f"<Field dbName=\"EMPRESA\" type=\"Text\" value=\"{name}\"/>\n")
    

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
    print("Monitorando a pasta seleccionada")
    while True:        
        time.sleep(1)
except KeyboardInterrupt:
    print('Monitoramento cancelado')
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