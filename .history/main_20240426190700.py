import pygetwindow as gw
import keyboard as kb
import pyautogui as ag


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
    except Exception as e: print(e)
selectwindow()

def checkforgreen():
    barcolour = (83, 250, 83)