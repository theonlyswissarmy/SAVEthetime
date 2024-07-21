import numpy as np, SAVEthetime as s, tkinter as tk, pyautogui as pya

def helpstt():
    s.openapopup("whadda hell")
    print("do me soon")





def doguibot(): # this is nearly a one to one copy of the main bot in SAVEthetime, but now its able to handle certain events
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
                    if fail or not egochk:
                        print("Could not find icon, exiting")
                        exit(0)
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
sinnames = ["1. Yi Sang:", "2. Faust:", "3. Don Quixote:",
            "4. Ryoshu:", "5. Meursault:", "6. Hong Lu:", "7.Heathcliffe:",
            "8. Ishmael:","9. Rodion:","10. Sinclair:","11. Outis:","12. Gregor:"]
window = tk.Tk()
window.title("SAVEthetime")
window.resizable(False, False)
Instruction = tk.Label(text="Input numbers in order of sinner selection (1 to select first, ect.)")
checkme = tk.Checkbutton(window, text="sinners already selected")
button = [0 for i in range(3)]
Instruction.grid(row=0, column=0,columnspan=10, padx=100)
entries =[0 for i in range(12)]
labels =[0 for i in range(12)]
for i in range(12): # label and entry setup
    labels[i] = tk.Label(window, text=sinnames[i])
    entries[i] = tk.Entry(window, width=5)
sin = 0
for i in range(4):
    for j in range(3):
        labels[sin].grid(row=j+2, column= (i*2))
        entries[sin].grid(row=j+2, column= (i*2)+1)
        sin = sin+1

button[0] = tk.Button(window, text="Help", command=lambda: helpstt())
button[1] = tk.Button(window, text="Start Bot", command=lambda: doguibot())
button[2] = tk.Button(window, text="Do Lux", command=lambda: doluxnow())
checkme.grid(row=5, column=2,columnspan=3)
button[0].grid(row=6, column=2)
button[1].grid(row=6, column=3)
button[2].grid(row=6, column=4)
window.mainloop()
