from tkinter import Frame, Canvas, NW, NE
from PIL import Image, ImageTk
import fitz
from Util import PhSize
from enum import Enum, auto

class PageSide(Enum):
    LEFT = auto()
    RIGHT = auto()

class PdfFrame:
    def __init__(self, masterFrame: Frame, pageSide: PageSide):
        self.masterFrame = masterFrame
        self.pdfCanvas = Canvas(self.masterFrame, width=1, height=1)
        self.pdfCanvas.grid(column=0, row=0)
        self.pdfPage = None
        self.canvasPdfId = None
        self.pageSide = pageSide

    def DrawPage(self, pdfPage: fitz.Page):
        self.pdfPage = pdfPage
        if(self.canvasPdfId is not None):
            self.pdfCanvas.delete(self.canvasPdfId)
        shrinkFactor = min(
            int(self.pdfCanvas["height"]) / pdfPage.rect.height,
            int(self.pdfCanvas["width"]) / pdfPage.rect.width)
        mat = fitz.Matrix(shrinkFactor, shrinkFactor)
        pix = pdfPage.getPixmap(matrix=mat)

        mode = "RGBA" if pix.alpha else "RGB"
        self.pdfCanvas.rawImage = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        self.pdfCanvas.image = ImageTk.PhotoImage(self.pdfCanvas.rawImage)
        if self.pageSide is PageSide.RIGHT:
            self.canvasPdfId = self.pdfCanvas.create_image(0, 0, anchor=NW, image=self.pdfCanvas.image)
        else:
            self.canvasPdfId = self.pdfCanvas.create_image(self.pdfCanvas["width"], 0, anchor=NE, image=self.pdfCanvas.image)

    def Empty(self):
        self.pdfCanvas.delete(self.canvasPdfId)
        self.canvasPdfId = None
        self.pdfPage = None
    
    def resize(self, newSize: PhSize):
        self.pdfCanvas["width"] = newSize.width
        self.pdfCanvas["height"] = newSize.height
        if(self.pdfPage is not None):
            self.DrawPage(self.pdfPage)