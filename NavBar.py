from tkinter import Frame, Button, E, W, BOTH, NSEW
from Util import PhSize
from typing import List, Callable
from math import floor

class NavBar:
    def __init__(self, masterFrame: Frame) -> None:
        self.nextClickFuncs: List[Callable] = []
        self.previousClickFuncs: List[Callable] = []

        self.masterFrame = masterFrame
        self.masterFrame["bg"] = "black"

        self.nextButtonFrame = Frame(self.masterFrame)
        self.nextButtonFrame.pack_propagate(0)
        self.nextButtonFrame.grid(row=0, column=1, sticky=NSEW, padx=0, pady=0)

        self.nextButton = Button(self.nextButtonFrame, text="Next", command=self.nextClicked)
        self.nextButton.pack(fill=BOTH, expand=1)
        # self.nextButton.grid(row=0, column=1, sticky=NSEW)

        self.previousButtonFrame = Frame(self.masterFrame)
        self.previousButtonFrame.pack_propagate(0)
        self.previousButtonFrame.grid(row=0, column=0, sticky=NSEW, padx=0, pady=0)

        self.previousButton = Button(self.previousButtonFrame, text="Previous", command=self.previousClicked)
        self.previousButton.pack(fill=BOTH, expand=1)
        # self.previousButton.grid(row=0, column=0, sticky=NSEW)


    def resize(self, newSize: PhSize) -> None:
        self.masterFrame["width"] = newSize.width
        self.masterFrame["height"] = newSize.height

        self.nextButtonFrame["width"] = floor(newSize.width / 2)
        self.previousButtonFrame["width"] = floor(newSize.width / 2)
        
        self.nextButtonFrame["height"] = newSize.height
        self.previousButtonFrame["height"] = newSize.height
        print("NavBar", "Width:", newSize.width, "Height:", newSize.height)

    def nextClicked(self) -> None:
        for func in self.nextClickFuncs:
            func()

    def previousClicked(self) -> None:
        for func in self.previousClickFuncs:
            func()

    def Remove(self) -> None:
        self.masterFrame.destroy()