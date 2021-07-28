import time
from pyautogui import *
import pyautogui as pg
import keyboard
import random
import win32api, win32con

#Position1: X: 362, Y: 360, RGB: (153, 158, 230)    This position is the point we wanna click
#Position2: X: 426, Y: 360, RGB: (172, 176, 233)    on game. you can change or setting to new position.    
#Position3: X: 478, Y: 360, RGB: (  0,   0,   0)    
#Position4: X: 534, Y: 360, RGB: (162, 167, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    ## If your computer too slow and it's don't click on the game, 
    ## you should increase time.sleep such as 0.05, 0.08, 0.1 or whatever
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pg.pixel(362,360)[0] == 0:
        click(362,360)

    if pg.pixel(426,360)[0] == 0:
        click(426,360)

    if pg.pixel(478,360)[0] == 0:
        click(478,360)

    if pg.pixel(534,360)[0] == 0:
        click(534,360)
