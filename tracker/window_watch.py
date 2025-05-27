# tracker/window_watch.py
import time
import win32gui
import psutil

def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd)

if __name__ == "__main__":
    print("Starting window watcher—press Ctrl+C to stop.")
    while True:
        title = get_active_window_title()
        print(f"Active window: {title}")
        time.sleep(1)
