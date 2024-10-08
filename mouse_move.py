import pyautogui
import time
import random

while True:
    try:
        # move the mouse cursor one pixel right
        pyautogui.move(1, 0)

        # wait for 0.5 seconds to give time for the cursor to move
        time.sleep(0.5)

        # move the mouse cursor one pixel left
        pyautogui.move(-1, 0)

        # wait for a random time between 250 to 350 seconds before repeating
        time.sleep(random.randint(250, 350))
    
    except pyautogui.FailSafeException:
        print("Fail-safe triggered. Resetting mouse position.")
        pyautogui.moveTo(pyautogui.size().width // 2, pyautogui.size().height // 2)  # move to center of the screen