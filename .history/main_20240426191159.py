import pygetwindow as gw
import keyboard as kb
import pyautogui as ag


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
    except Exception as e: print(e)
selectwindow()

def startscript():
    keyboard.wait(';')
    checkforgreen()


def checkforgreen():
    barcolour = (83, 250, 83)
    s = pyautogui.screenshot()
    for i in range(s.width):
        for j in range(s.height):
            if s.getpixel((i, j)) == barcolour:
                pyautogui.click(x, y)




def main():
    gamewindow = selectwindow()
    if not window is None:
        startscript()
    else:
        print("Failed to find the Roblox window. Please ensure the game is running.")

if __name__ == "__main__":
    main()
