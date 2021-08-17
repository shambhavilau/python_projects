# Automated Text Messaging

# Text file: message.txt
# Open up you messaging app or notepad
# Run the program
# switch to the notepad and wait for response


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
