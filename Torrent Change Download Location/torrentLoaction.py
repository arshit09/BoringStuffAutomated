import pyautogui
import time

countDM = 15
count = 0
time.sleep(0)
while (count < countDM):
    pyautogui.click(529, 115)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(643, 120)
    time.sleep(0.5)
    pyautogui.click(733, 615)
    time.sleep(0.5)
    count = count + 1
    