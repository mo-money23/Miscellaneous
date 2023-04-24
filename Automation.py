from ast import Try
import pyautogui
import time

pyautogui.FAILSAFE = False

while True:
    try:
        time.sleep(15)

        for i in range(0, 100):
            pyautogui.moveTo(0, i * 2)

        for i in range(0, 3):
            pyautogui.click()

    except KeyboardInterrupt:
        break
