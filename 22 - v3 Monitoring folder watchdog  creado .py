
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('arquivo creado')
        
      

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir(r'C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    print("Monitorando a pasta seleccionada")
    while True:        
        time.sleep(1)
except KeyboardInterrupt:
    print('Monitoramento cancelado')
    observer.stop()
observer.join()