import numpy as np
import cv2
import pyautogui
import time
import pyperclip
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

countDM = int(input("\nTotal DMs: "))
time.sleep(3)
# pyperclip.copy('scrcpy --max-fps 15 ')
# pyautogui.hotkey('win', 'r')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# pyautogui.hotkey('enter')
# time.sleep(5)
# pyautogui.hotkey('win', 'up')

FamousAccount = 'theminimalist_india'
# pyperclip.copy(FamousAccount)
count = 0

# print(pyautogui.position())
# click on Search icon
pyautogui.click(827, 1006, duration=1)
time.sleep(3)
# click on Search Bar
pyautogui.click(906, 89, duration=1)
time.sleep(3)
# search for minimalist account
# pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite(FamousAccount)
# pyautogui.typewrite(["9", "g", "a", "g"])
# pyautogui.typewrite(["t", "h", "e", "m", "i", "n", "i", "`m",
#                      "a", "l", "i", "s", "t", "_", "i", "n", "d", "i", "a"])
time.sleep(3)

# clicks on famous account we searched for
pyautogui.click(807, 181, duration=1)
time.sleep(3)

# clicks on followers
pyautogui.click(990, 159, duration=1)

# pyperclip.copy(
#     'It seems you like minimalism. Checkout @be.kriative for creativity with minimalism.')

while (count < countDM):
    # wait first time to load followers
    if (count == 0):
        time.sleep(3)
    # click on first user
    pyautogui.click(790, 243, duration=1)
    time.sleep(3)

    image = pyautogui.screenshot(region=(662, 40, 553, 530))
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    cv2.imwrite("D:\desktop\detectMessage.png", image)
    stringFromSS = pytesseract.image_to_string(
        r'D:\desktop\detectMessage.png', lang='eng')
    # if(stringFromSS.find('Message') != -1):
    #     # click back arrow
    #     pyautogui.click(764, 96, duration=1)

    # click on options for DM
    pyautogui.click(1187, 91, duration=1)

    # "send message" option
    pyautogui.click(730, 951, duration=1)
    time.sleep(3)

    # message box
    pyautogui.click(813, 995, duration=1)

    # MAIN MESSAGE
    # pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite(
        'It seems you like minimalism. Checkout @be.kriative for creativity with minimalism.')

    # click send
    time.sleep(1)
    pyautogui.click(1173, 678, duration=1)

    # click on Back arrow button on top left corner
    pyautogui.click(689, 89, duration=1)
    pyautogui.click(689, 89, duration=1)
    if countDM != 1 or count != countDM-1:
        pyautogui.moveTo(790, 243, duration=1)
        pyautogui.dragRel(0, -75, duration=1)
    count = count + 1