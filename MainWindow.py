from tkinter import *
from tkinter import filedialog
from Util import *
from PdfFrame import PdfFrame
from PdfManager import PdfManager

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Title Takeover!")
        self.master.geometry("500x500")
        self.height = self.master["height"]
        self.width = self.master["width"] 

        self.pdfPane = Frame(master)
        self.pdfPane.grid(row=0, column=0)
        
        # Set up Pdf Management
        filePath = self.loadPdfFile()
        self.pdfManager = PdfManager(self.pdfPane, filePath)

        self.bottomNav = Frame(master)
        self.bottomNav.grid(row=1, column=0)
        self.bottomNav["bg"] = "black"
        self.bottomNav["height"] = 40

        # Set up master window events
        self.master.bind("<Configure>", func=self.resizeEvent)
    
    def resizeEvent(self, event):
        if(event.widget is self.master and (self.height != event.height or self.width != event.width)):
            self.height = event.height
            self.width = event.width
            self.pdfPane["height"] = self.height - 40
            self.pdfPane["width"] = self.width

            self.bottomNav["width"] = self.width

            print("Window", "Width:", self.width, "Height:", self.height)
    
    def loadPdfFile(self):
        fpath = filedialog.askopenfilename(title="Select your PDF...", filetypes=[("PDFs", "*.pdf")])
        if fpath:
            return fpath
        else:
            raise Exception("Couldn't find given file.")