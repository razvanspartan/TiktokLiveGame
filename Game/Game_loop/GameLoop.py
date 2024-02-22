'''import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.last_position = 0

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.filename):
            with open(event.src_path, 'r') as file:
                # Move to the last known position in the file
                file.seek(self.last_position)
                # Read the new content added to the file
                new_content = file.read()
                # Update the last known position
                self.last_position = file.tell()
                # Print the new content
                print(f"New modifications in '{self.filename}':")
                print(new_content)

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Specify the filename to monitor
    filename = 'events1.txt'

    # Create an event handler
    event_handler = MyHandler(filename)

    # Create an observer
    observer = Observer()
    observer.schedule(event_handler, current_directory, recursive=True)

    # Start the observer
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

Handler=MyHandler("events1.txt")
Myhandler.on_modified("events1.txt")'''
