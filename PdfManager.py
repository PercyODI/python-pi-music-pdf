import fitz
from tkinter import Frame
from PdfFrame import PdfFrame, PageSide
from Util import PhSize

class PdfManager:
    def __init__(self, master: Frame, pdfPath: str):
        self.masterFrame = master
        self.doc = fitz.Document(pdfPath)
        self.currentLeftPageNum = 0
        self.currentRightPageNum = 1
        self.leftPdfFrame = None
        self.rightPdfFrame = None
        self.BuildFrames()

    def Remove(self):
        self.masterFrame.destroy()

    def BuildFrames(self):
        if self.leftPdfFrame is not None:
            self.leftPdfFrame.Remove()
            self.leftPdfFrame = None
        if self.rightPdfFrame is not None:
            self.rightPdfFrame.Remove()
            self.rightPdfFrame = None
        leftPane = Frame(self.masterFrame)
        leftPane.grid(row=0, column=0)
        self.leftPdfFrame = PdfFrame(leftPane, PageSide.LEFT, self.doc[self.currentLeftPageNum])

        if(self.currentRightPageNum < self.doc.pageCount):
            rightPane = Frame(self.masterFrame)
            rightPane.grid(row=0, column=1)
            self.rightPdfFrame = PdfFrame(rightPane, PageSide.RIGHT, self.doc[self.currentRightPageNum])

        self.resize(PhSize(self.masterFrame["width"], self.masterFrame["height"]))

    def NextPage(self):
        if(self.currentLeftPageNum + 2 < self.doc.pageCount):
            self.currentLeftPageNum += 2
        
            if(self.currentRightPageNum + 2 < self.doc.pageCount):
                self.currentRightPageNum += 2
            else:
                self.currentRightPageNum += 2
            self.BuildFrames()
                

    def PreviousPage(self):
        if(self.currentLeftPageNum - 2 >= 0):
            self.currentLeftPageNum -= 2
        
            if(self.currentRightPageNum - 2 >= 0):
                self.currentRightPageNum -= 2
            self.BuildFrames()


    def resize(self, newSize: PhSize):
        self.masterFrame["width"] = newSize.width
        self.masterFrame["height"] = newSize.height
        if(self.leftPdfFrame is not None):
            self.leftPdfFrame.resize(PhSize(newSize.width / 2, newSize.height))
        if(self.rightPdfFrame is not None):
            self.rightPdfFrame.resize(PhSize(newSize.width / 2, newSize.height))

        print("PdfManager", "Width:", newSize.width, "Height:", newSize.height)