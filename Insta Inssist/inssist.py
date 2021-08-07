from time import time
import pyautogui
import time

account = "theminimalist_india"

# search for search-icon
SearchIcon = pyautogui.locateOnScreen('Images/SearchIcon.png', confidence=0.8)
while SearchIcon == None:
    SearchIcon = pyautogui.locateOnScreen('Images/SearchIcon.png')
# click on search-icon
pyautogui.click(pyautogui.center(SearchIcon), duration=0.5)

# click to type
pyautogui.click(1016, 228, duration=1.5)

time.sleep(1)

# type accout name
pyautogui.write(account, interval=0.1)

# click on first search result's name
pyautogui.click(906, 297, duration = 1.5)

SendIcon = pyautogui.locateOnScreen('Images/SendIcon.png', confidence=0.8)
while SendIcon == None:
    SendIcon = pyautogui.locateOnScreen('Images/SendIcon.png')
