import webbrowser
import pyautogui
import time
from pyscreeze import locateOnScreen

web_link = 'Link'
webbrowser.open_new_tab(web_link)
time.sleep(5)

pyautogui.hotkey('ctrl','e')
pyautogui.hotkey('ctrl','d')
time.sleep(1)

position_file = pyautogui.locateOnScreen('Path')
pyautogui.moveTo(position_file)
pyautogui.click(position_file)