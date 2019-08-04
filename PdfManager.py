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

        self.leftPane = Frame(master)
        self.leftPane.grid(row=0, column=0)
        self.leftPane["bg"] = "light blue"
        self.leftPdfFrame = PdfFrame(self.leftPane, PageSide.LEFT)
        self.leftPdfFrame.DrawPage(self.doc[self.currentLeftPageNum])

        if(self.doc.pageCount > 1):
            self.rightPane = Frame(master)
            self.rightPane.grid(row=0, column=1)
            self.rightPane["bg"] = "red"
            self.rightPdfFrame = PdfFrame(self.rightPane, PageSide.RIGHT)
            self.rightPdfFrame.DrawPage(self.doc[self.currentRightPageNum])
        else:
            self.rightPdfFrame = None


    def NextPage(self):
        if(self.currentLeftPageNum + 1 < self.doc.pageCount):
            self.currentLeftPageNum += 1
            self.leftPdfFrame.DrawPage(self.doc[self.currentLeftPageNum])
        
        if(self.currentRightPageNum + 1 < self.doc.pageCount):
            self.currentRightPageNum += 1
            self.rightPdfFrame.DrawPage(self.doc[self.currentRightPageNum])

    def resize(self, newSize: PhSize):
        self.leftPdfFrame.resize(PhSize(newSize.width / 2, newSize.height))
        if(self.rightPdfFrame is not None):
            self.rightPdfFrame.resize(PhSize(newSize.width / 2, newSize.height))

        print("PdfManager", "Width:", newSize.width, "Height:", newSize.height)