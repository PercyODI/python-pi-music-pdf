import fitz
from tkinter import Frame
from PdfFrame import PdfFrame, PageSide
from Util import PhSize
from PyMus import PyMusData, PyMusPage, PyMusPdf
from uuid import UUID
from typing import Dict, List


class PdfManager:
    def __init__(self, master: Frame, pyMusData: PyMusData) -> None:
        self.masterFrame = master
        self.pdfFrames: List[PdfFrame] = []
        self.pyMusData = pyMusData
        self.loadedPdfs: Dict[UUID, fitz.Document] = {}

        pyMusPdf: PyMusPdf
        for pyMusPdf in pyMusData.pdfs:
            self.loadedPdfs[pyMusPdf.id] = fitz.Document("pdf", pyMusPdf.bytes)
        self.currentView = 0
        self.BuildFrames()

    def Remove(self) -> None:
        self.masterFrame.destroy()

    def BuildFrames(self) -> None:
        currCol = 0
        for pdfFrame in self.pdfFrames:
            pdfFrame.Remove()
        self.pdfFrames = []

        page: PyMusPage
        for page in self.pyMusData.views[self.currentView].pages:
            pageFrame = Frame(self.masterFrame)
            pageFrame.grid(row=0, column=currCol)
            self.pdfFrames.append(
                PdfFrame(pageFrame, self.loadedPdfs[page.pdfId][page.pageNum], PageSide.LEFT if currCol == 0 else PageSide.RIGHT))
            currCol += 1
        self.resize(
            PhSize(self.masterFrame["width"], self.masterFrame["height"]))

    def NextPage(self) -> None:
        if self.currentView + 1 < len(self.pyMusData.views):
            self.currentView += 1
            self.BuildFrames()

    def PreviousPage(self) -> None:
        if self.currentView > 0:
            self.currentView -= 1
            self.BuildFrames()

    def resize(self, newSize: PhSize) -> None:
        self.masterFrame["width"] = newSize.width
        self.masterFrame["height"] = newSize.height
        for pdfFrame in self.pdfFrames:
            pdfFrame.resize(
                PhSize(newSize.width / len(self.pdfFrames), newSize.height))

        print("PdfManager", "Width:", newSize.width, "Height:", newSize.height)
