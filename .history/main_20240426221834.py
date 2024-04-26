import pygetwindow as gw
import keyboard as kb
import pyautogui as ag
import time
# Screen areas for checking:

# Box for bubbles:

# top left (300, 150)
# bottom left (300, 750)
# top right (1620, 150)
# bottom right (1620, 750)

# Box for green:

# top left (750, 775)
# bottom left (750, 880)
# top right (1150, 775)
# bottom right (1150, 880)

# Click indicator:
# position check: (825, 823)



def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
        return(gameWindow)
    except Exception as e: print(e)

def checkforbubbles():
    bubblecolour = (68, 252, 234)
    while True:
        s = ag.screenshot()
        bubble_found = False
        
        for i in range(300, 1620):
            for j in range(150, 750):
                if s.getpixel((i, j)) == bubblecolour:
                    print("Bubble found")
                    ag.click(button='left')
                    automatedfishing()
                    bubble_found = True
                    time.sleep(3)  # Give some time before checking for more bubbles
                    break
            if bubble_found:
                break

        if kb.is_pressed(','):
            print("Stopping bubble checks...")
            break

def automatedfishing():
    positioncolour = (255, 255, 255)
    check_area = range(870, 880)  # Check a small horizontal range for the white bar

    while True:
        found = False
        for x in check_area:
            s = ag.screenshot()
            if s.getpixel((x, 823)) == positioncolour:
                print("Pointer detected at:", x)
                ag.click(button='left')
                found = True
                time.sleep(0.1)  # Slight delay to prevent overly rapid clicks
                break  # Break after the first click to avoid multiple clicks per detection

        if not found:
            print("Bar no longer detected, stopping clicks...")
            break

        time.sleep(0.5) 
def startscript():
    kb.wait(';')
    checkforbubbles()

def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()