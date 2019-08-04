from tkinter import Frame, Button, E, W, BOTH
from Util import PhSize
from math import floor

class NavBar:
    def __init__(self, masterFrame: Frame):
        self.masterFrame = masterFrame
        self.masterFrame["bg"] = "black"
        self.masterFrame["highlightbackground"] = "blue"
        self.masterFrame["highlightcolor"] = "blue"
        self.masterFrame["highlightthickness"] = 1

        self.nextButtonFrame = Frame(self.masterFrame)
        self.nextButtonFrame.pack_propagate(0)
        self.nextButtonFrame.grid(row=0, column=1, sticky=E, padx=0, pady=0)

        self.nextButton = Button(self.nextButtonFrame, text="Next")
        self.nextButton.pack(fill=BOTH, expand=1)
        # self.nextButton.grid(row=0, column=1, sticky=E)

        self.previousButtonFrame = Frame(self.masterFrame)
        self.previousButtonFrame.pack_propagate(0)
        self.previousButtonFrame.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        self.previousButton = Button(self.previousButtonFrame, text="Previous")
        self.previousButton.pack(fill=BOTH, expand=1)
        # self.previousButton.grid(row=0, column=0, sticky=W)

    def resize(self, newSize: PhSize):
        self.masterFrame["width"] = newSize.width
        self.masterFrame["height"] = newSize.height

        self.nextButtonFrame["width"] = floor(newSize.width / 2)
        self.previousButtonFrame["width"] = floor(newSize.width / 2)
        
        self.nextButtonFrame["height"] = newSize.height
        self.previousButtonFrame["height"] = newSize.height
        print("NavBar", "Width:", newSize.width, "Height:", newSize.height)