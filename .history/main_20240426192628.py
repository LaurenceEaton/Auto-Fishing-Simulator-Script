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
    fishing = False
    barcolour = (83, 250, 83)
    s = ag.screenshot()
    for i in range(s.width):
        for j in range(s.height):
            if s.getpixel((i, j)) == barcolour:
                fishing = True
        




def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()
