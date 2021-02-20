import pyautogui
import time
from mss import mss
import cv2
from PIL import Image
import numpy as np

# START THE GAME
# -----------------------------------
def start_mario_double_dash():
    # look for dolphin emulator icon
    while 1:
        dolphinIcon = pyautogui.locateOnScreen('dolphinIcon.png')
        print(dolphinIcon)

        if dolphinIcon != None:
            pyautogui.click(dolphinIcon)
            break

    # look for dolphin window
    while 1:
        dolphinWindow = pyautogui.locateOnScreen('dolphinStart.png')
        print(dolphinWindow)

        if dolphinWindow != None:
            pyautogui.click(dolphinWindow)
            break

    # look for mario kart dash and double click it
    while 1:
        marioDoubleDash = pyautogui.locateOnScreen('marioDoubleDash.png')
        print(marioDoubleDash)

        if marioDoubleDash != None:
            pyautogui.click(marioDoubleDash)
            pyautogui.click(marioDoubleDash)
            break


    # wait for game to start and select window
    while 1:
        marioKartWindow = pyautogui.locateOnScreen('nintendo.png')
        print(marioKartWindow)

        if marioKartWindow != None:
            pyautogui.click(marioKartWindow)
            break
    return 1

# press key
def press_key(key, n_times = 1):
    for _ in range(n_times):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)

# wait for start menu and press enter then a
# wait for game to start and select window
def wait_for_start_menu():
    while 1:
        marioKartStartWindow = pyautogui.locateOnScreen('MarioKartStartMenu.png')
        print(marioKartStartWindow)

        if marioKartStartWindow != None:
            select_scenario()
            break
# locate and exit marioDoubleDash
def locate_and_exit_marioDoubleDash():
    # exit mario dash
    while 1:
        exitMarioDash = pyautogui.locateOnScreen('exit.png')
        if exitMarioDash != None:
            pyautogui.click(exitMarioDash)
            break
    while 1:
        yes = pyautogui.locateOnScreen('yes.png')
        if yes != None:
            pyautogui.click(yes)
            break
    # exit dolphin
    while 1:
        exitDolphin = pyautogui.locateOnScreen('dolphinStart.png')
        if exitDolphin != None:
            pyautogui.click(x=980, y=155)
            break

# select 1 player mode, grand prix and 50 cc
def select_scenario():
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')

# select characters
# from start
# mario = a
# luigi = down -> a
# princess = right -> a
# brown princess = right -> down -> a

def select_character(first, second):
    # for now just select first two appearing
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')
    time.sleep(1)
    press_key('a')

# continously catch game screen
def catch_screen():
    mon = {'top': 20, 'left': 70, 'width': 640, 'height':520}
    moved = 0
    x = 0
    y = 0
    sct = mss()

    while 1:
        sct_img = sct.grab(mon)
        img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
        cv2.imshow('test', np.array(img))

        if moved == 0:
            nintendo = pyautogui.locateOnScreen('nintendo.png')
            if nintendo != None and moved == 0:
                x = nintendo[0] + nintendo[2]
                y = nintendo[1]

        if moved == 0 and x != 0:
            testWindow = pyautogui.locateOnScreen('screenCaptureWindow.png')
            if testWindow != None:
                pyautogui.click(testWindow)
                pyautogui.dragTo(x, y, button='left')
                moved = 1

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
