import pyautogui
import time
i = 2
for i in range(25):
    i = i + 1
    pyautogui.click(x=155, y=92)
    pyautogui.write('exe{}.py'.format(i))
    pyautogui.press('enter')