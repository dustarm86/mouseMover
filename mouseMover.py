"""
dependencies:
pip3 install pyobj c -core

pip3 install pyobjc

pip3 install pyautogui
"""
import pyautogui
import time

userTime = int(input('How many hour(s) will the prog run?: '))
print('mouseMover prog will run for', userTime, 'hour(s)')
startTime = time.time() # remember when we started

while (time.time() - startTime) < (userTime * 60) * 60:
    pyautogui.PAUSE = 10
    pyautogui.moveRel(0, 10)
    pyautogui.click()
    pyautogui.PAUSE = 15
    pyautogui.moveRel(0, -10)
    pyautogui.click()
    pyautogui.PAUSE = 15

print('mouseMover prog has finished running for', userTime, 'hour(s)')
