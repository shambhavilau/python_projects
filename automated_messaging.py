# Automated Text Messaging

# Import modules
import time
import pyautogui

def SendMessage():
    time.sleep(4)
    text = open('message.txt')
    for line in text:
        pyautogui.typewrite(line)
        pyautogui.press('enter')


SendMessage()