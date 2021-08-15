from pynput.keyboard import Key, Listener
import pyautogui
import time

def on_press(key):
    if key == Key.insert:
        pyautogui.click(539, 979)
        time.sleep(0.75)
        pyautogui.click(630, 692)
        pyautogui.click(1461, 776)

# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()
