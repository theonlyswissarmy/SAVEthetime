from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import time, pytesseract, pyautogui, keyboard, cv2, os

screenwid, screenlen = pyautogui.size()

sinners = [0] * 6
sinselected = False
money = 0


def setsinselect():
    global sinselected
    sinselected = not sinselected


def getsinselect():
    global sinselected
    return sinselected


def selectsinners():
    global sinners
    initx = 434
    inity = 341

    while 1:
        print("Are sinners already selected? y/n")
        if input() == "y":
            return
        elif input() == "n":
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
    pixp = (252, 154, 0)  # pause color
    pixf = (131, 91, 39)  # fork color

    while 1:
        if keyboard.is_pressed("q"):
            exit(0)
        pthenenter()
        pix = pyautogui.pixel(1789, 121)
        if not pix == pixp and not pix == pixf:  # compare curcolor to others to see if still fight
            print("FIRST PASS")
            time.sleep(2)  # edge case
            pyautogui.moveTo(1789, 121)
            pix = pyautogui.pixel(1789, 121)
            try:
                pyautogui.locateOnScreen("fork.png", confidence=.8)
                print("located fork")
            except:
                try:
                    pyautogui.locateOnScreen("pause.png", confidence=.8)
                    print("located pause")
                except:
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
            setsinselect()
        pyautogui.click(1705, 869)
        time.sleep(10)
        print("we're fighting?")
        mainfight()
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.locateOnScreen("eventskip.png", confidence=.8)
            for i in range(3):
                pyautogui.click(903, 465)
                time.sleep(.3)
            if pyautogui.pixelMatchesColor(1674, 183, (253, 96, 0)):
                shop()
            else:
                event()
        except pyautogui.ImageNotFoundException:
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


def grabEGO():
    try:
        res = pyautogui.locateOnScreen("EGOconfirm.png", confidence=.8)
        clickhere(res)
        return
    except pyautogui.ImageNotFoundException:
        return


def event() -> int:
    while 1:
        initre = 1038
        probs = ["ery", "igh", "ormal", "Low"]
        breakout = False
        time.sleep(1)
        im = pyautogui.screenshot(region=(initre, 259, 700, 160))
        text = pytesseract.image_to_string(im)
        print(text)
        if "E.G." in text:
            pyautogui.click(initre + 100, 359)
            time.sleep(2.5)
            for i in range(2):
                pyautogui.click(1705, 931)
            time.sleep(2.5)
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
                    if prob in text:
                        breakout = True
                        break
                    initre = initre + 120
                if breakout:
                    os.remove("screen.png")
                    break
            for i in range(2):
                pyautogui.click(1705, 931)
            time.sleep(5)
            for i in range(4):
                pyautogui.click(903, 465)
                time.sleep(.5)
            time.sleep(.5)
            pyautogui.click(1705, 931)
            time.sleep(2)
            for i in range(4):
                pyautogui.click(1705, 931)
            time.sleep(5)
            return 0
        else:
            print("No ego gift found?")
            if pyautogui.pixelMatchesColor(1793, 914, (150, 50, 35)):
                clickhere((1793, 914))  # it turns out we were done
                return 1
            if keyboard.is_pressed("q"):
                exit(0)
            pyautogui.click(1038, 975)  # select first option
        return 0


def infightcheck() -> bool:
    try:
        if pyautogui.locateOnScreen("pause.png", confidence=.8):
            mainfight()
            return True
    except pyautogui.ImageNotFoundException:
        try:
            if pyautogui.locateOnScreen("fork.png", confidence=.8):
                mainfight()
                return True
        except pyautogui.ImageNotFoundException:
            return False


def move():
    print("MOVE")
    try:
        res = pyautogui.locateOnScreen("clockface3.png", confidence=.6)
        selwid, sellen = pyautogui.center(res)
        print("We found the image")
        pyautogui.moveTo(selwid, sellen)
        selwid = selwid + 400
        sellen = sellen - 220
        for i in range(3):
            try:
                pyautogui.click(selwid, sellen)  # we click on the icon
                time.sleep(1)
                res = pyautogui.locateOnScreen("enter.png", confidence=.6)  # if valid enter will be found
                print("entering")
                clickhere(res)
                break
            except:
                sellen = sellen + 275
    except pyautogui.ImageNotFoundException:
        print("we didnt find the image")
        return 1
    time.sleep(.9)
    return 0


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
startbot()
time.sleep(5)
while not keyboard.is_pressed('q'):
    moveck = move()
    print("EXITED MOVE")
    eventck = getevent()
    print("EXITED EVENT")
    fightck = infightcheck()
    grabEGO()
    if not eventck:
        if not fightck:
            if not isvictory():
                print("adjusting zoom")
    else:
        print("getting zoom right after event")
        pyautogui.scroll(-1)
        pyautogui.scroll(1)
