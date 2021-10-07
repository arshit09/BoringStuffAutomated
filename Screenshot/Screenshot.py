from pynput.keyboard import Key, Listener
import pyautogui
import cv2
import numpy as np

xy = []

def on_press(key):
    if hasattr(key,'char'):
        if key.char == "1":
            x1, y1 = pyautogui.position()
            xy.append(x1)
            xy.append(y1)
            
        elif key.char == "2":
            x2, y2 = pyautogui.position()
            xy.append(x2)
            xy.append(y2)
            print(xy)
            exit()

with Listener(on_press=on_press) as listener:
    listener.join()
    
topL = []
topR = []
botL = []
botR = []

def position(x1, y1, x2, y2):
    if(y1 > y2):
        if(x1 > x2):
            botR.append(x1)
            botR.append(y1)
        else:
            botL.append(x1)
            botL.append(y1)
    else:
        if(x1 > x2):
            topR.append(x1)
            topR.append(y1)
        else:
            topL.append(x1)
            topL.append(y1)

position(xy[0],xy[1],xy[2],xy[3])
position(xy[2],xy[3],xy[0],xy[1])

if ((not topL) and (not botR)):
    topL.append(botL[0])
    topL.append(topR[1])
    botR.append(topR[0])
    botR.append(botL[1])

# print("-"*30)
# print("|",topL,"            ", topR,"\n|\n|\n|\n|", botL,"          ", botR)

image = pyautogui.screenshot(region=(topL[0], topL[1], botR[0]-topL[0], botR[1]-topL[1]))
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("Screenshot.png", image)