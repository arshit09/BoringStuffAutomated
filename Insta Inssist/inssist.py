""""
Chrome extension: INSSIST 
Display resolution: 1920*1080
Scale: 125%
"""

from time import time
import pyautogui
import time
import pyperclip
import easygui

account = "theminimalist_india"
NumberofDM = 20

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

# waiti until Followers counter appears
Followers = pyautogui.locateOnScreen('Images/Followers.png', confidence=0.8)
while Followers == None:
    Followers = pyautogui.locateOnScreen('Images/Followers.png')
    
# click on Followers count
pyautogui.click(pyautogui.center(Followers), duration=0.5)

screenCheck = 0
count = 0
while count < NumberofDM:
    if(screenCheck == 0):
        # click on first follower(center screen)
        pyautogui.click(894, 277, duration = 2)
    else:
        # click on first(after scrolling) follower(right screen)
        pyautogui.click(1355, 283, duration = 1)
        
    # waiti until DM icon appears
    DMIcon = pyautogui.locateOnScreen('Images/DMIcon.png', confidence=0.8)
    while DMIcon == None:
        DMIcon = pyautogui.locateOnScreen('Images/DMIcon.png')

    # click on DM icon
    pyautogui.click(pyautogui.center(DMIcon), duration=0.5)

    time.sleep(4)

    Message = open('Message.txt', 'r').read()
    pyperclip.copy(Message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    # waiti until Follow button appears
    Follow = pyautogui.locateOnScreen('Images/Follow.png', confidence=0.8)
    while Follow == None:
        Follow = pyautogui.locateOnScreen('Images/Follow.png')
        
    # click on Follow
    pyautogui.click(pyautogui.center(Follow), duration=0.5)

    # click on back
    pyautogui.click(1307,229, duration = 1.5)

    time.sleep(2)

    pyautogui.scroll(-65)

    time.sleep(1)
    
    screenCheck = 1
    count += 1

title = "Insta Messenger"
msg = str(NumberofDM) + ' messages sent to the followers of "' + account +'"'
easygui.msgbox(msg, title)