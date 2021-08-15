import pyautogui
import time

# print(pyautogui.position())
time.sleep(3)
countDM = 200
count = 0
while (count < countDM):
    pyautogui.click(675, 206)
    count = count + 1
    