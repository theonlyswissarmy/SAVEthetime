import tkinter as tk
class Communicae:  # this is a class that handles communication between the GUI and SAVEthetime
    windict  = {} # list of all open non mainGUI labels

    def isopen(self, name: str):  # checks if a given window title is currently open
        return name in self.windict

    def addwin(self, name: str, win: tk.Toplevel):  # adds a name to winnames
        self.windict[name] = win

    def delwin(self, name: str):  # Removes a name from winnames, extra window was closed
        del self.windict[name]

    def getwin(self, name: str): return (
        self.windict)[name]

