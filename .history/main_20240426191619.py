import pygetwindow as gw
import keyboard as kb
import pyautogui as ag


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
        return(gameWindow)
    except Exception as e: print(e)

def startscript():
    kb.wait(';')
    checkforgreen()


def checkforgreen():
    barcolour = (83, 250, 83)
    s = ag.screenshot()
    if s.getpixel((i, j)) == barcolour:
        print("hello world")




def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()
