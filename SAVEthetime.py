from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import time, pytesseract, pyautogui, keyboard, cv2, os, tkinter

from pyscreeze import Box

screenwid, screenlen = pyautogui.size()

inGUI = False  # variable which denotes if we're using the GUI or not
sinners = [0] * 6  # the sinners we want to use
sinselected = False
money = 0


# TO BE IMPLEMENTED, finds window and adjusts values and images to confrom to window resolution
def adjustres():
    return


# Macro function to click skip button
def clickonskip():
    for i in range(3):
        pyautogui.click(903, 465)
        time.sleep(.3)
    return


# stops user from closing a window
def disable_event():
    pass


# def to open a popup for the GUI, exits on button press
def openapopup(poptext):
    popup = tkinter.Toplevel()
    popup.wm_title("WARNING")
    var = tkinter.IntVar()
    popup.geometry("250x250")
    popup.protocol("WM_DELETE_WINDOW", disable_event)
    Label = tkinter.Label(popup, text=poptext)
    exitbutton = tkinter.Button(popup, text="OK", command=lambda: var.set(1))
    Label.pack()
    exitbutton.pack()
    popup.resizable(False, False)
    popup.wait_variable(var)
    print("past wait")
    popup.destroy()


def selectsinners():  # this bot sets the sinners via the console
    global sinners
    initx = 434  # x value where sinner cards start
    inity = 341  # y value where sinner cards start
    while 1:
        if not inGUI:  # use the console to prompt for user input if just in script
            print("Are unwanted sinners already selected? y/n")
            select = input()
            if select == "y":
                return
            elif select == "n":
                break
            print("bad input, please only type either y or n")
        else:  # use tkinter to pop up if we're using a gui
            openapopup("Please make sure all sinners are unselected")
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


def startbot():  # this starts the main bot, allows user to select sinner, or not
    global sinners, sinselected
    sincount = [0] * 13
    print("STARTING SAVE THE TIME. INPUT SINNER NUMBERS (type 0 to leave unused) \n")
    print("make sure to be in the first hex in dungeon\n")
    x = 0
    while 1:
        selsin = input("are sinners already selected? y/n")
        if selsin == "y":
            sinselected = True
            return
        if selsin == "n":
            break
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


def infightcheck() -> bool:  # makes sure we're within a fight via 2 unique elements
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


# future autoshop function
def shop():
    if (inGUI):
        openapopup("Autoshop is disabled, press OK when finishsed")
    else:
        print("this still needs to be done, figure it out soon dipshit")
        input("press enter to continue")
    # get money from screen
    # read and select ego gifts with compatable skill apps until out of money
    return


# hit p, then hit enter
def pthenenter():
    pyautogui.press("p", 1, .1)
    pyautogui.press("enter", 1, .1)
    time.sleep(5)
    return


# this def is the def that handles simple fights with enemies.
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
                time.sleep(8)
                pyautogui.click(944, 454)  # extra stuff for ego gift
                pyautogui.sleep(.5)
                pyautogui.click(1696, 850)
                return
        print("STILL FIGHTING")

    # select win rate, then hit go


def isvictory() -> bool:
    # return if we're done
    return False


# click whereever res is
def clickhere(res):
    selwid, sellen = pyautogui.center(res)
    pyautogui.click(selwid, sellen)
    return


# gets the event type, 1 for success, 2 for select sinenrs in GUI, 3 for shop in GUI
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
                    match (deteventstage(0)):
                        case 0:  # we definitely left the event
                            break
                        case 1:  # in text/choices section
                            time.sleep(3)
                            dotext()
                        case 2:  # in sinner probabilities
                            sinprob()
                        case 3:  # the red button was present
                            pass

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
    if eventend():
        print("we should exit now")
        ret = 3
    elif istext():
        print("DO TEXT")
        ret = 1
    elif isprob():
        ret = 2
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
        pyautogui.screenshot("screen.png", region=(1038, 259 + addy, 700, 160))
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
                print("we are here!")
                pyautogui.moveTo(1038, 279)
                pyautogui.click(1038, 279)  # select first option
                time.sleep(3)
                break
            else:
                addy = addy + 200  # read the next block
    print("Returning")
    return 0


def isprob() -> bool:
    try:
        pyautogui.locateOnScreen("advantage.png", confidence=.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def sinprob():  # this def handles the part of events where you decide which sinner should perform a task
    breakout = False
    probs = ["ery H", "igh", "ormal", "Low"]
    for prob in probs:
        initre = 112
        for i in range(12):
            if keyboard.is_pressed('q'):
                exit(0)
            pyautogui.click(initre, 939)
            time.sleep(.5)
            pyautogui.screenshot("screen.png", region=(1147, 716, 600, 60))
            img = cv2.imread("screen.png")
            img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
            text = pytesseract.image_to_string(img)
            print(prob + " " + text)
            time.sleep(1)
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
    clickonskip()
    return 0  # hopefully we're done with the event probability


def eventend() -> bool:
    if pyautogui.pixelMatchesColor(1692, 885, (160, 50, 35), tolerance=20):
        print("Done?")
        pyautogui.click(1793, 914)  # it turns out we're done
        return True
    return False


def grabEGO() -> bool:
    try:
        res = pyautogui.locateOnScreen("EGOconfirm.png", confidence=.8)
        clickhere(res)
    except pyautogui.ImageNotFoundException:
        try:  # this is really bad form. this does theme packs
            res = pyautogui.locateOnScreen("starlightgain.png", confidence=.8)
            pyautogui.moveTo(res[0], res[1])
            pyautogui.drag(0, 300, 1, button='left')
        except pyautogui.ImageNotFoundException:
            return False
    pyautogui.moveTo(950, 540)
    return True


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
            time.sleep(.8)
            res = pyautogui.locateOnScreen("enter.png", confidence=.8)  # if valid enter will be found
            print("entering")
            clickhere(res)
            break
        except:
            sellen = sellen + 275
    time.sleep(.9)
    return 0


def adjustzoom() -> bool:
    for look in range(3):
        pyautogui.moveTo(590 + (400 * look), 540)
        for i in range(6):
            pyautogui.scroll(1000)
            time.sleep(.2)

        for i in range(6):
            if findclockface(.9):
                return False
            pyautogui.scroll(-1)
            time.sleep(.2)
        print("zooming out " + str(i))
        time.sleep(.3)
    return True


def mainbot():
    startbot()
    time.sleep(5)
    grabEGO()
    fail = True
    while not keyboard.is_pressed('q'):
        move()
        print("EXITED MOVE")
        eventck = getevent()
        print("EXITED EVENT")
        fightck = infightcheck()
        egochk = grabEGO()
        if not fightck:
            if not eventck or not egochk:
                if not isvictory():

                    print("looking around and adjusting zoom")
                    fail = adjustzoom()
                    if fail or not egochk:
                        print("Could not find icon, exiting")
                        exit(0)

                else:
                    exit(0)  # We won!
            else:
                print("getting zoom right after event")
                pyautogui.scroll(-1)
                pyautogui.scroll(1)
        else:  # we're in a fight
            mainfight()


def dolux():
    time.sleep(3)
    while 1:
        if infightcheck():
            mainfight()
            time.sleep(3)
        else:
            return


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
if __name__ == "__main__":
    while 1:
        do = input("type 1 to just fight, 2 to start the bot")
        if do == "1":
            openapopup("testtest test")
            print("we're here now!")
            exit(0)
        elif do == "2":
            mainbot()
            exit(0)
