from pynput.keyboard import Key, Listener
import pyautogui
import cv2
import numpy as np

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def takeSS():
    global x1,y1,x2,y2
    image = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("Screenshot.png", image)
    print("Screenshot Area :", x1, y1,x2-x1, y2-y1)
    exit()    

def on_press(key):
    global x1,y1,x2,y2
    if hasattr(key,'char'):
        if key.char == "1":
            x1, y1 = pyautogui.position()
            
        elif key.char == "2":
            x2, y2 = pyautogui.position()
            takeSS()

with Listener(on_press=on_press) as listener:
    listener.join()