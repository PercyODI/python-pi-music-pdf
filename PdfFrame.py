from tkinter import Frame, Canvas, NW, NE, PhotoImage
from PIL import Image, ImageTk
import fitz
from Util import PhSize
from typing import Optional

class PhImageCanvas(Canvas):
    def __init__(self, master, **kw):
        self.rawImage: Optional[Image] = None
        self.image: Optional[PhotoImage] = None
        return super().__init__(master, **kw)

class PdfFrame:
    def __init__(self, masterFrame: Frame, pdfPage: fitz.Page) -> None:
        self.masterFrame = masterFrame
        self.pdfCanvas = PhImageCanvas(self.masterFrame, width=1, height=1)
        self.pdfCanvas.grid(column=0, row=0)
        self.pdfPage = pdfPage
        self.canvasPdfId = None
        self.givenSize: PhSize = PhSize(1, 1)
        self._drawPage()

    def _drawPage(self) -> None:
        if(self.canvasPdfId is not None):
            self.pdfCanvas.delete(self.canvasPdfId)
        shrinkFactor = min(
            float(self.givenSize.height / self.pdfPage.rect.height),
            float(self.givenSize.width / self.pdfPage.rect.width))
        mat = fitz.Matrix(shrinkFactor, shrinkFactor)
        pix = self.pdfPage.getPixmap(matrix=mat)

        mode = "RGBA" if pix.alpha else "RGB"
        self.pdfCanvas["width"] = pix.width
        self.pdfCanvas["height"] = pix.height
        self.pdfCanvas.rawImage = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        self.pdfCanvas.image = ImageTk.PhotoImage(self.pdfCanvas.rawImage)
        self.canvasPdfId = self.pdfCanvas.create_image(0, 0, anchor=NW, image=self.pdfCanvas.image)

    def Remove(self) -> None:
        self.masterFrame.destroy()
    
    def resize(self, newSize: PhSize) -> None:
        self.givenSize = PhSize(max(1, newSize.width), max(1, newSize.height))
        if(self.pdfPage is not None):
            self._drawPage()