import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # mover o arquivo para outra pasta
            src_path = event.src_path
            dst_path = r'C:\Users\DDR4\Desktop\Python Manipulação de Texto' + os.path.basename(src_path)
            os.rename(src_path, dst_path)
            print(f"Movido: {src_path} -> {dst_path}")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=r'C:\Users\DDR4\Desktop\Python Manipulação de Texto\pasta2', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
