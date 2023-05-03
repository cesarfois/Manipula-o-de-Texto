# PComo Usar Watchdog
#https://www.youtube.com/watch?v=jyE-MJRwsqo&t=1s


import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

def on_created(event):
    print("creado")

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

    path = r'C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2'
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