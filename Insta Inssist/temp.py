from pynput.keyboard import Key, Listener
import pyperclip
import pyautogui
import time

def on_press(key):
    if key == Key.esc:
        pyautogui.scroll(-65)
        
# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()
