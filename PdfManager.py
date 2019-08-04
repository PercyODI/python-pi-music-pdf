import fitz
from tkinter import *
from PdfFrame import PdfFrame

class PdfManager:
    def __init__(self, master: Frame, pdfPath: str):
        self.doc = fitz.Document(pdfPath)
        self.currentLeftPageNum = 0
        self.currentRightPageNum = 1

        self.leftPane = Frame(master)
        self.leftPane.grid(row=0, column=0)
        self.leftPane["bg"] = "light blue"
        self.leftPdfFrame = PdfFrame(self.leftPane)

        self.rightPane = Frame(master)
        self.rightPane.grid(row=0, column=1)
        self.rightPane["bg"] = "red"
        self.rightPdfFrame = PdfFrame(self.rightPane)

        self.masterFrame = master
        self.masterFrame.bind("<Configure>", func=self.selfResize)

    def NextPage(self):
        pass

    def selfResize(self, event):
        if(event.widget == self.masterFrame):
            self.leftPane["width"] = event.width / 2
            self.leftPane["height"] = event.height
            print("PdfManager", "Width:", event.width, "Height:", event.height)