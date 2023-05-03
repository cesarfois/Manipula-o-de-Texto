# Python Automação - Monitoramento + Criação de Pastas AUTOMÁTICOS
# https://github.com/devaprender/download_folder_cleaner/blob/master/download_cleaner.py
# https://www.youtube.com/watch?v=Nnj6-NtJXUc&t=92s


import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('arquivo creado')
        

    @staticmethod
    def on_modified(event):
        # if os.path.isdir(event.src_path):
        #     return
        print('arquivo modificado ')
        time.sleep(1)
        # if is_code_file(event) == True:
        #     path_to_folder = make_folder('code')
        #     move_to_new_corresponding_folder(event, path_to_folder)
        #     return
        # elif is_text_file(event) == True:
        #     path_to_folder = make_folder('text')
        #     move_to_new_corresponding_folder(event, path_to_folder)
        #     return
      

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
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()