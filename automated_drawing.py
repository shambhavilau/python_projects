# Automated Drawing

# Open up your paint or any other drwaing application 
# Run the program and switch to your paint app
# Wait for the response


# Import modules
import time
import pyautogui

# Draw spiral using pyautogui
time.sleep(4)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button='left') # draw horizontal line for 300 long and for 1 sec
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button='left')
    time.sleep(2)


