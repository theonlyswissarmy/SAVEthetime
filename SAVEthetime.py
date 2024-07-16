from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import time, pytesseract, pyautogui, keyboard, cv2, os

from pyscreeze import Box

screenwid, screenlen = pyautogui.size()

sinners = [0] * 6
sinselected = False
money = 0


# TO BE IMPLEMENTED, finds window and adjusts values and images to confrom to window resolution
def resadjust():
    return


# Macro function to click skip button
def clickonskip():
    for i in range(3):
        pyautogui.click(903, 465)
        time.sleep(.3)
    return


def selectsinners():
    global sinners
    initx = 434
    inity = 341
    while 1:
        print("Are sinners already selected? y/n")
        select = input()
        if select == "y":
            return
        elif select == "n":
            break
        print("bad input, please only type either y or n")
    # pyautogui.click(initx, inity)
    for sinner in sinners:
        addy, addx = 0, 0
        if (sinner % 6) < sinner:
            addy = 310
            sinner = sinner % 6
        addx = 200 * sinner
        print("sinnum is " + str(sinner) + " addx is " + str(addx) + " addy is " + str(addy))
        pyautogui.moveTo(initx + addx, inity + addy)
        pyautogui.click(initx + addx, inity + addy)
        time.sleep(1)


def startbot():
    sincount = [0] * 13
    print("STARTING SAVE THE TIME. INPUT SINNER NUMBERS (type 0 to leave unused) \n")
    print("make sure to be in the first hex in dungeon\n")
    x = 0
    while x < 6:
        while 1:
            selsin = input("input sinner " + str(x + 1) + " number \n")
            if selsin.isdigit() and 0 <= int(selsin) < 13:
                break
        sinnum = int(selsin)
        sincount[sinnum] = sincount[sinnum] + 1
        sinners[x] = sinnum - 1
        if sinnum != 0 and sincount[sinnum] > 1:
            print("Select distinct sinners only \n")
            while 1:  # maybe something was misunderstood
                select = input("exit? y/n")
                if select == "y" or select == "Y":
                    exit(0)
                elif select == "n" or select == "N":
                    for i in range(13):
                        sincount[i] = 0
                    for i in range(6):
                        sinners[i] = 0
                    x = -1  # set to negative 1, so we restart at 0
                    break
        x += 1
    if sincount[0] == 6:
        print("no sinners selected, exiting")
        exit(0)
    print("starting bot in 10 seconds, switch to main game in full screen")
    return


def upgrade():
    # not sure what to put here
    return


def findclockface(acc) -> Box | None:
    try:
        return pyautogui.locateOnScreen("clockface3.png", confidence=acc)
    except pyautogui.ImageNotFoundException:
        return None


def infightcheck() -> bool:
    try:
        pyautogui.locateOnScreen("fork.png", confidence=.8)
        print("located fork")
        return True
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.locateOnScreen("pause.png", confidence=.8)
            print("located pause")
            return True
        except pyautogui.ImageNotFoundException:
            return False


def shop():
    # get money from screen
    # read and select ego gifts with compatable skill apps until out of money
    return


def pthenenter():
    pyautogui.press("p", 1, .1)
    pyautogui.press("enter", 1, .1)
    time.sleep(5)
    return


def mainfight():
    pyautogui.moveTo(1789, 121)
    time.sleep(1)
    pixp = pyautogui.pixel(1789, 121)  # pause color
    pixf = (131, 91, 39)  # fork color

    while 1:
        if keyboard.is_pressed("q"):
            exit(0)
        pthenenter()
        pix = pyautogui.pixel(1789, 121)
        if not pix == pixp and not pix == pixf:  # compare curcolor to others to see if still fight
            print("FIRST PASS")
            time.sleep(1)  # edge case
            pyautogui.moveTo(1789, 121)
            if not infightcheck():
                print("DONE FIGHTING")
                time.sleep(6)
                pyautogui.click(944, 454)  # extra stuff for ego gift
                pyautogui.sleep(.5)
                pyautogui.click(1696, 850)
                return
        print("STILL FIGHTING")

    # select win rate, then hit go


def isvictory() -> bool:
    # return if we're done
    return False


def clickhere(res):
    selwid, sellen = pyautogui.center(res)
    pyautogui.click(selwid, sellen)
    return


def getevent() -> bool:
    global sinselected
    time.sleep(.5)
    print("GET EVENT")
    pix = pyautogui.pixel(1685, 499)
    print("pix 0 = " + str(pix[0]) + " " + str(pix[1]) + " " + str(pix[2]))
    try:
        # NOTE MAKE SURE SINNERS ARE SELECTED VIA SINSELECTED

        pyautogui.locateOnScreen("TOBATTLE.png", confidence=.8)
        if not sinselected:  # we havent slected sinners yet!
            selectsinners()
            sinselected = not sinselected
        pyautogui.click(1705, 869)
        time.sleep(10)
        print("we're fighting?")
        mainfight()
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.locateOnScreen("eventskip.png", confidence=.8)
            clickonskip()
            if pyautogui.pixelMatchesColor(1674, 183, (253, 96, 0)):
                print("SHOP")
                shop()
            else:
                print("EVENT")
                while 1:
                    time.sleep(5)
                    match (deteventstage(0)):
                        case 0:  # we definitely left the event
                            break
                        case 1: # in text/choices section
                            time.sleep(3)
                            dotext()
                        case 2: # in sinner probabilities
                            sinprob()
                        case 3:  # the red button was present
                            pass # TO DO LATER

        except pyautogui.ImageNotFoundException:
            print("FAIL")
            return False
    return True


def SAVEthetime():
    # main timeripper func,
    # IS HE TALKING????, click until he stops
    # use win rate for first three rounds
    # determine how many skills time ripper has
    # decide which skill to use
    # choose which time ripper skill to clash with
    # select EGO if needed
    # if all skills unclashable just use last skill
    # mark off skill, move onto next sinner.
    return


def deteventstage(ret) -> int:
    if istext():
        print("DO TEXT")
        ret = 1
    if isprob():
        ret = 2
    if eventend():
        ret = 3
    print(str(ret))
    return ret


def istext() -> bool:
    try:
        pyautogui.locateOnScreen("choices.png", confidence=.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def dotext():
    addy = 0
    for i in range(3):
        time.sleep(1)
        im = pyautogui.screenshot("screen.png", region=(1038, 259 + addy, 700, 160))
        readthis = cv2.imread("screen.png", cv2.IMREAD_GRAYSCALE)
        text = pytesseract.image_to_string(readthis, config='--psm 6')
        print(text + " <- This is our text")
        time.sleep(4)
        if "E.G." in text:
            pyautogui.click(1138, 359 + addy)
            time.sleep(2.5)
            clickonskip()
            break
        else:
            print("No ego gift found?")
            if keyboard.is_pressed("q"):
                exit(0)
            if i == 2:
                pyautogui.click(1038, 975)  # select first option
                break
            else:
                addy = addy + 200 # read the next block
    print("Returning")
    return 0


def isprob()->bool:
    try:
        pyautogui.locateOnScreen("advantage.png", confidence=.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def sinprob():
    breakout = False
    probs = ["ery", "igh", "ormal", "Low"]
    for prob in probs:
        initre = 112
        for i in range(12):
            pyautogui.click(initre, 939)
            time.sleep(.5)
            pyautogui.screenshot("screen.png", region=(1147, 716, 600, 60))
            img = cv2.imread("screen.png")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(img)
            print(prob + " " + text)
            if prob in text:  # find a good probability
                breakout = True
                break
            initre = initre + 120
        if breakout:
            os.remove("screen.png")
            break
    for i in range(2):
        pyautogui.click(1705, 931)
    time.sleep(5)
    clickonskip()  # we try to skip the next few batches of text
    return 0  # hopefully we're done with the event probability


def eventend() -> bool:
    if pyautogui.pixelMatchesColor(1793, 914, (150, 50, 35)):
        print("Done?")
        clickhere((1793, 914))  # it turns out we're done
        return True
    return False


def grabEGO():
    try:
        res = pyautogui.locateOnScreen("EGOconfirm.png", confidence=.8)
        clickhere(res)
    except pyautogui.ImageNotFoundException:
        try: # this is really bad form. this does theme packs
            res = pyautogui.locateOnScreen("starlightgain.png", confidence=.8)
            pyautogui.moveTo(res[0], res[1])
            pyautogui.drag(0,300,1, button='left')
        except pyautogui.ImageNotFoundException:
            return
    pyautogui.moveTo(950,540)
    return


def move():
    print("MOVE")
    res = findclockface(.85)
    if res is None:
        print("we didnt find the image")
        return 1
    selwid, sellen = pyautogui.center(res)
    print("We found the image")
    pyautogui.moveTo(selwid, sellen)
    selwid = selwid + 400
    sellen = sellen - 220
    for i in range(3):
        try:
            pyautogui.click(selwid, sellen)  # we click on the icon
            time.sleep(1)
            res = pyautogui.locateOnScreen("enter.png", confidence=.8)  # if valid enter will be found
            print("entering")
            clickhere(res)
            break
        except:
            sellen = sellen + 275
    time.sleep(.9)
    return 0


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#startbot()
time.sleep(5)
grabEGO()
while not keyboard.is_pressed('q'):
    fail = True
    moveck = move()
    print("EXITED MOVE")
    eventck = getevent()
    print("EXITED EVENT")
    fightck = infightcheck()
    grabEGO()
    if not fightck:
        if not eventck:
            if not isvictory():
                print("adjusting zoom")
                for i in range(6):
                    pyautogui.scroll(1000)
                    time.sleep(.2)
                for i in range(20):
                    if findclockface(.9):
                        fail = False
                        break
                    pyautogui.scroll(-1)
                    print("zooming out " + str(i))
                    time.sleep(.3)
                if fail:
                    print("Could not find icon, exiting")
                    exit(0)
                else:
                    fail = True
            else:
                exit(0)  # We won!
        else:
            print("getting zoom right after event")
            pyautogui.scroll(-1)
            pyautogui.scroll(1)


    else: # we're in a fight
        mainfight()
