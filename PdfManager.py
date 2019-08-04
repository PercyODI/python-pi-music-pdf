import fitz
from tkinter import *
from PdfFrame import PdfFrame
from Util import PhSize

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

    def NextPage(self):
        pass

    def resize(self, newSize: PhSize):
        self.leftPane["width"] = newSize.width / 2
        self.leftPane["height"] = newSize.height

        self.rightPane["width"] = newSize.width / 2
        self.rightPane["height"] = newSize.height

        print("PdfManager", "Width:", newSize.width, "Height:", newSize.height)