import pyautogui
import time
pyautogui.PAUSE = 0.6

def abre_chrome():
    pyautogui.press("win")
    pyautogui.write('chrome')
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("F5")
    time.sleep(1)
    pyautogui.press("home")
    time.sleep(0.4)
abre_chrome()
