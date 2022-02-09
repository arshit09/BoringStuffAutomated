""""
Software: Bluestacks 5 Beta 
Display resolution: 1920*1080
Scale: 125%
"""

import pyautogui
import time
import pyperclip
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

time.sleep(2)

countDM = 10
count = 0
flag = 0
time.sleep(1)
pyautogui.click(827, 1007, duration=1)
pyautogui.click(891, 90, duration=1)
time.sleep(1)

typethis = "brandkhichdi"
lengthofTS = len(typethis)
countTS = 0
# limit = lengthofTS
while(countTS < lengthofTS):
    pyautogui.hotkey(typethis[countTS])
    countTS += 1

pyautogui.click(820, 178, duration=1)
time.sleep(1)
pyautogui.click(991, 169, duration=1)
time.sleep(1)

while (count < countDM):
    # follower list -> first user
    pyautogui.click(800, 243, duration=1)
    time.sleep(1)
    # click on RIGHT TOP options
    pyautogui.click(1187, 91, duration=1)
    time.sleep(0.5)
    image = pyautogui.screenshot(region=(666, 931, 207, 45))
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    cv2.imwrite("D:\InstadetectMessage.png", image)
    stringFromSS = pytesseract.image_to_string(
        r'D:\InstadetectMessage.png', lang='eng')
    if(stringFromSS.find('message') != -1):
        flag = 1
        # print("Found")
        count = count+1
        # click on "SEND MESSAGE" option
        pyautogui.click(784, 949, duration=0.5)
        time.sleep(0.5)
        # click on TEXT BOX
        # pyautogui.click(890, 994, duration=1)
        pyperclip.copy(
            'It seems you like minimalism. Checkout @be.kriative for creativity with minimalism.')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(1175, 992, duration=0.5)
    pyautogui.click(680, 88, duration=0.5)
    pyautogui.click(680, 88, duration=0.5)
    if (flag == 1):
        pyautogui.click(1145, 243, duration=0.5)
    pyautogui.moveTo(800, 243, duration=0.5)
    # -6 drag added
    pyautogui.dragRel(0, -80, duration=0.5)
    flag = 0
