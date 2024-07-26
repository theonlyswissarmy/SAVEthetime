import numpy as np, SAVEthetime as s, tkinter as tk


def helpstt():
    s.openapopup("whadda hell")
    print("do me soon")


def loadsinners(entries):
    sinners = [-1] * 6
    for cnt in range(6):
        for i in range(12):
            val = entries[i].get()
            print("cal is " + str(cnt))
            print("val is " + str(val))
            if int(val) - 1 == cnt:
                sinners[cnt] = i
                break


def doguibot():  # this is nearly a one to one copy of the main bot in SAVEthetime, but now its able to handle certain
    # events
    s.setinGUI(True)
    s.loadinSinners(entries)
    s.time.sleep(5)
    s.grabEGO()
    fail = True
    while not s.keyboard.is_pressed('q'):
        s.move()
        print("EXITED MOVE")
        eventck = s.getevent()
        print("EXITED EVENT")
        fightck = s.infightcheck()
        egochk = s.grabEGO()
        if not fightck:
            if not eventck or not egochk:
                if not s.isvictory():
                    print("looking around and adjusting zoom")
                    fail = s.adjustzoom()
                    if fail and not s.grabEGO():
                        print("Could not find icon, stopping bot")
                        return
                else:
                    exit(0)  # We won!
            else:
                print("getting zoom right after event")
                s.pyautogui.scroll(-1)
                s.pyautogui.scroll(1)
        else:  # we're in a fight
            s.mainfight()


def doluxnow():
    s.dolux()


def valent(text, test):
    print("text is " + text + " test is " + test)
    if int(test) != -1:
        print("Past insert")
        if str(text).isdigit() and 0 < int(text) < 13:
            print("here")
            return True
        #s.openapopup("Invalid input, numbers from 1-12 only")
        return False
    return True


sinnames = ["1. Yi Sang:", "2. Faust:", "3. Don Quixote:",
            "4. Ryoshu:", "5. Meursault:", "6. Hong Lu:", "7.Heathcliffe:",
            "8. Ishmael:", "9. Rodion:", "10. Sinclair:", "11. Outis:", "12. Gregor:"]
window = tk.Tk()
window.title("SAVEthetime")
window.resizable(False, False)
Instruction = tk.Label(text="Input numbers in order of sinner selection (1 to select first, ect.)")
checkme = tk.Checkbutton(window, text="sinners already selected")
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

button[0] = tk.Button(window, text="Help", command=lambda: loadsinners(entries))
button[1] = tk.Button(window, text="Start Bot", command=lambda: doguibot())
button[2] = tk.Button(window, text="Do Lux", command=lambda: doluxnow())
checkme.grid(row=5, column=2, columnspan=3)
button[0].grid(row=6, column=2)
button[1].grid(row=6, column=3)
button[2].grid(row=6, column=4)
window.mainloop()
