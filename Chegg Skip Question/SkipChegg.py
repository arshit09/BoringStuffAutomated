from pynput.keyboard import Listener
import pyautogui
import time


def on_press(key):
    pyautogui.click(539, 979)
    time.sleep(0.5)
    pyautogui.click(630, 692)
    pyautogui.click(1461, 776)


# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys
