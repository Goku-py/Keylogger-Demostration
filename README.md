# Keystroke Logging Demonstration

A Python-based educational keylogger with a GUI interface, built using `pynput` and `tkinter`.  
Designed for **demonstration and learning purposes** in a controlled environment.

---

## Features

- **Graphical Interface** — Clean tkinter GUI with Start and Stop & Exit buttons
- **Three Keystroke Events** — Captures `pressed`, `held`, and `released` states for every key
- **Dual Logging** — Writes to two log files simultaneously on every keystroke:
  - `logs.json` — Structured event log with event labels and key names
  - `logs.txt` — Plain character stream (readable text output)
- **Session Reset** — Log files are wiped at the start of each new session so old data never carries over
- **Non-blocking Architecture** — File I/O is offloaded to a background writer thread via a queue, keeping the GUI fully responsive
- **Space Detection** — Space keystrokes are marked as word separators in the structured log
- **Graceful Exit** — Listener is safely stopped on window close or Ctrl+C

---
[![alt text](image.png)](https://github.com/Goku-py/Keylogger-Demostration)

## Log Format

### `logs.json`
One event per entry, written continuously:
```
pressed('h'), held('h'), released('h'),pressed('e'), held('e'), released('e'), space , pressed('y'), ...
```

### `logs.txt`
Plain characters only — no event labels:
```
hey
```

---

## Setup

### Requirements

- Python 3.x
- `pynput` library

### Install Dependencies

```bash
pip install pynput
```

### Run

```bash
python Keylogger.py
```

> **Note:** On Windows, run from a terminal with appropriate permissions if keystrokes are not being captured.

### Usage

1. Run the script — the GUI window will open
2. Click **Start Keylogger** to begin capturing keystrokes
3. Type anywhere on your system — all keys are logged in real time
4. Click **Stop & Exit** to stop the listener and close the app
5. Open `logs.json` or `logs.txt` from the same folder to view captured data

---

## File Structure

```
Keystroke Logging Demonstration/
│
├── Keylogger.py      # Main application
├── logs.json         # Structured event log (created on first run)
├── logs.txt          # Plain text keystroke log (created on first run)
└── README.md         # This file
```

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Disclaimer

> This tool is intended **strictly for educational and demonstration purposes**.  
> Do not use this software to monitor or record keystrokes on any system without **explicit consent** from the owner.  
> Unauthorized use may violate privacy laws and regulations.
