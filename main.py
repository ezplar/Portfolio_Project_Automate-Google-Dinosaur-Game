import pyautogui
from PIL import ImageGrab, ImageOps
import numpy as np
import time

#Replay button via pixel coordinates
replay_btn = (482, 442)

#Dino pixel coordinates
dino = (70,330)

#Click replay button
pyautogui.click(replay_btn)

def restart_game():
    # pyautogui.click(replay_btn)

    pyautogui.keyDown('down')

def space_jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)

    print('jump')

    # time.sleep(0.0001)
    pyautogui.keyUp('space')

    pyautogui.keyDown('down')

def grab_image():
    box = (dino[0]+35, dino[1]+153, dino[0]+130, dino[1]+175)

    image = ImageGrab.grab(box)

    gray_img = ImageOps.grayscale(image)

    n_arr = np.array(gray_img.getcolors())

    print(n_arr.sum())
    return n_arr.sum()

restart_game()
while True:
    if (grab_image() != 2345):
        space_jump()

        time.sleep(0.001)




