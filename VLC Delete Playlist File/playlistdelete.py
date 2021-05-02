from pynput.keyboard import Key, Listener
import pyautogui
import time


def on_press(key):
    if key == Key.esc:
        # print("hey")
        pyautogui.click(386, 42)
        time.sleep(0.1)
        pyautogui.click(546, 350)


# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys
