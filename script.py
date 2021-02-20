import os
# give access to pyautogui
os.system("xhost +")
import pyautogui
import time
from pynput.keyboard import Key, Controller
import subprocess
from helpers import helpers

# **************
# TO DO
# 1. Start game and try to navigate using screen capture
# **************
'''
helpers.start_mario_double_dash()
# wait for start cinematic to show
time.sleep(10)
# -----------------------------------
# for cinematic press a
helpers.press_key('a')
# wait for start menu and go into character selection
helpers.wait_for_start_menu()
helpers.select_character('luigi', 'mario')
'''
helpers.catch_screen()



#helpers.locate_and_exit_marioDoubleDash()

# end
# disable access for pyautogui
os.system("xhost -")

# asyncio
'''
import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
    cmd,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run("echo 'PRESS A' >> ~/.dolphin-emu/Pipes/pipe"))
asyncio.run(run("echo 'RELEASE A' >> ~/.dolphin-emu/Pipes/pipe"))
'''

# Capture screen continously and fast
'''
mon = {'top': 20, 'left': 70, 'width': 900, 'height':800}

sct = mss()

while 1:
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    cv2.imshow('test', np.array(img))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
'''




'''
# grab fullscreen
# force backend to mss and remove childprocess = fast screnshots
#im = ImageGrab.grab(backend="mss", childprocess=False, bbox=(10, 10, 510, 510)) # X1, Y1, X2, Y2

# save file
#im.save("box.png")


for i in range(100):
    #im = ImageGrab.grab()
    # force backend to mss and remove childprocess = fast screnshots
    im = ImageGrab.grab(backend="mss", childprocess=False)
    im.save("fullscreen.png")
    im.show()

'''




# Capture windows WINDOWS MAC ONLY
'''
from PIL import ImageGrab
import win32gui

hwnd = win32gui.FindWindow(None, r'Window_Title')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)

image = ImageGrab.grab(dimensions)
image.show()
'''

# code for displaying number of monitors
'''
import mss
import mss.tools
from PIL import Image

with mss.mss() as sct:
# Get information of monitor 2
monitor_number = 2
mon = sct.monitors[monitor_number]

print(mon)
'''

# code for capturing a part of the screen
'''
import mss
import mss.tools
from PIL import Image

with mss.mss() as sct:
    # capture part of screen
    monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    #filename = sct.shot(mon=-2, output='terminal.png')

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

'''
