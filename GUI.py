import tkinter

import numpy as np, SAVEthetime as s, tkinter as tk, Communicae

Comms = Communicae.Communicae()
window = tk.Tk()


# displays a help menu
def helpstt():
    GUIpopup("USAGE INFORMATION: SAVEthetime is a Limbus Company Bot made to complete Easy Mirror Dungeons "
             "and luxifications\n"
             "REQUIREMENTS: Main Screen Resolution must be in 1920 x 1080, Screen Resolution must be on Full Screen,"
             "Windowed \n"
             "REQUIREMENTS: Tessoract-OCR must be installed for this program to work, Language must be set to"
             " English\n"
             "In the main window, there are multiple entry boxes placed next to the names of each sinner. "
             "Within each entrybox "
             "place the selection order, 1 for first selection, 2 for second, ect.\n"
             "Once the sinners are selected, hit the button to start the bot and select the game to make it "
             "active\n"
             "For just luxification, Make sure to start the luxification, and then hit the button, no sinners need"
             " to be selected\n"
             "IMPORTANT NOTE: On the first battle of the dungeon, unless the sinner checkbox is marked, you"
             "will be prompted to make sure unwanted sinners reamin unselected\n"
             "IMPORTANT NOTE: Currently there is no Autoshop feature, all actioned related to shopping or upgrading"
             " will need to be done manually.", "Help")


# this def collects sinners from the entires and loads them into SAVEthetime, throws an altert if bad values
def loadsinners(entries) -> bool:
    global Comms
    end = False
    sinners = [0] * 6  # these are the inital six sinners we want to use
    bacsin = [-1] * 6  # these are back up sinners that we use if the initial six expire.
    for cnt in range(6):
        for i in range(12):
            val = entries[i].get()
            print("cal is " + str(cnt))
            print("val is " + str(val))
            if val != "" and int(val) - 1 == cnt:
                sinners[cnt] = i
                break
            elif i == 11:  # no solo missions if you wanna use the GUI
                GUIpopup("Please make sure enough sinners are selected\n"
                         "at least 6 boxes must have a number from 1 - 6.\n"
                         "7-12 can be selected for backup if desired", "Bad Input")
                return False
    # sinner backups, to do later
    # for cnt in range(6): # back up sinners load in, less important, no fail
    #     for i in range(12):
    #         val = entries[i].get()
    #         print("cal is " + str(cnt))
    #         print("val is " + str(val))
    #         if int(val) - 1 == cnt + 6:
    #             bacsin[cnt] = i
    #             break
    #         elif i == 11: # no solo missions if you wanna use the GUI
    #             end = True
    #     if end:
    #         break
    s.sinnerintake(sinners)
    return True


# handles general popup protocol for the GUI
def GUIpopup(text: str, Title: str):
    if Comms.isopen(Title):
        pop = Comms.getwin(Title)
        pop.attributes("-topmost", True)  # forces the popup to the top where it can't be missed
        pop.attributes("-topmost", False)  # we don't care what happens as long as the user sees the popup
    else:
        s.openapopup(text, False, title=Title)  # creates a new window since one doesn't already exist


# main behavior for starting the bot
def START(sel: int, entries=None, var=None, othervar=None):
    #GUIpopup("STARTING THE BOT IN 5 SECONDS\n"
             #"MAKE SURE THE GAME IS FULLSCREEN WINDOWED, ACTIVE, AND ON THE MAIN MONITOR\n", "STARTING")
    match sel:
        case 1:
            s.setinGUI(True)  # done once
            if not var.get():  # sinners not already selected
                print("Check unmarked")
                s.sinselected = False
                if not loadsinners(entries):
                    return
            else:
                print("sinselected set to true")
                s.sinselected = True
            if finvar:
                s.finalWAIT = True
            else:
                s.finalWAIT = False

            s.mainbot()
        case 2:
            s.dolux()


# this is a value verificiation def, throws false if not good, test is input type, text is current value
def valent(text, test):
    global window, Comms

    print("text is " + text + " test is " + test)
    if int(test) == 1 or int(test) == 0:  # if inserting into text
        print("Past insert")
        if str(text).isdigit() and -1 < int(text) < 13 or text == "":
            print("here")
            return True
        GUIpopup("Invalid input, numbers from 1-12 only", "Invalid Input")
        return False
    return True


sinnames = ["1. Yi Sang:", "2. Faust:", "3. Don Quixote:",
            "4. Ryoshu:", "5. Meursault:", "6. Hong Lu:", "7.Heathcliffe:",
            "8. Ishmael:", "9. Rodion:", "10. Sinclair:", "11. Outis:", "12. Gregor:"]
s.setCommunicae(Comms)  # links the comms between STT and GUI
finvar = tk.BooleanVar() # var for waiting at final floor EGO gift
var = tk.BooleanVar()
window.title("SAVEthetime")
window.resizable(False, False)
Instruction = tk.Label(text="Input numbers in order of sinner selection (1 to select first, ect.)")
checkme = tk.Checkbutton(window, text="Sinners already selected?", variable=var)
checkmetoo = tk.Checkbutton(window, text="Manually select final floor EGO gift?", variable=finvar)
button = [0 for i in range(3)]
Instruction.grid(row=0, column=0, columnspan=10, padx=100)
entries = [0 for i in range(12)]
labels = [0 for i in range(12)]
valid = (window.register(valent), '%P', '%d')
for i in range(12):  # label and entry setup
    labels[i] = tk.Label(window, text=sinnames[i])

    entries[i] = tk.Entry(window, width=5, validate='all', validatecommand=valid)
sin = 0
for i in range(4):
    for j in range(3):
        labels[sin].grid(row=j + 2, column=(i * 2))
        entries[sin].grid(row=j + 2, column=(i * 2) + 1)
        sin = sin + 1
button[0] = tk.Button(window, text="Help", command=lambda: helpstt())
button[1] = tk.Button(window, text="Start Bot", command=lambda: START(1, entries, var, finvar))
button[2] = tk.Button(window, text="Do Lux", command=lambda: START(2))
checkme.grid(row=5, column=0, columnspan=3)
checkmetoo.grid(row=5, column=3, columnspan=4)
button[0].grid(row=6, column=2)
button[1].grid(row=6, column=3)
button[2].grid(row=6, column=4)
window.mainloop()
