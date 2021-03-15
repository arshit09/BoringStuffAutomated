import pyautogui
import time
import pyperclip
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

time.sleep(2)


countDM = 1
count = 0
time.sleep(1)
pyautogui.click(827, 1007, duration=1)
pyautogui.click(891, 90, duration=1)
time.sleep(1)

typethis = "theminimalist_india"
lengthofTS = len(typethis)
countTS = 0
limit = lengthofTS
while(countTS < lengthofTS):
    pyautogui.hotkey(typethis[countTS])
    countTS = countTS + 1

pyautogui.click(820, 178, duration=1)
time.sleep(2)
pyautogui.click(991, 169, duration=1)
time.sleep(1)

while (count < countDM):
    # follower list > first user
    pyautogui.click(800, 243, duration=1)
    time.sleep(1.5)
    # click on RIGHT TOP optins
    pyautogui.click(1187, 91, duration=1)
    time.sleep(1)
    image = pyautogui.screenshot(region=(666, 931, 207, 35))
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    cv2.imwrite("D:\InstadetectMessage.png", image)
    stringFromSS = pytesseract.image_to_string(
        r'D:\InstadetectMessage.png', lang='eng')
    if(stringFromSS.find('Message') != -1):
        print("Found")
        # click on "SEND MESSAGE" option
        pyautogui.click(784, 949, duration=1)
        time.sleep(1)
        # click on TEXT BOX
        pyautogui.click(890, 994, duration=1)
        typethis = "It seems you like minimalism. Checkout @be.kriative for creativity with minimalism."
        lengthofTS = len(typethis)
        countTS = 0
        limit = lengthofTS
        while(countTS < lengthofTS):
            pyautogui.hotkey(typethis[countTS])
            countTS = countTS + 1
        pyautogui.click(1176, 671, duration=1)
    pyautogui.click(680, 88, duration=1)
    pyautogui.click(680, 88, duration=1)
    pyautogui.moveTo(800, 243, duration=1)
    pyautogui.dragRel(0, -72, duration=1)
    count = count+1
