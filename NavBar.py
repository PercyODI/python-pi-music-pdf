from tkinter import *
from Util import PhSize

class NavBar:
    def __init__(self, masterFrame: Frame):
        self.masterFrame = masterFrame
        self.masterFrame["bg"] = "black"

    def resize(self, newSize: PhSize):
        self.masterFrame["width"] = newSize.width
        self.masterFrame["height"] = newSize.height
            
        print("NavBar", "Width:", newSize.width, "Height:", newSize.height)