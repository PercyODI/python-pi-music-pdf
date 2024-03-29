from tkinter import Tk, Frame, NSEW, Menu, S
from tkinter import filedialog
from Util import *
from PdfFrame import PdfFrame
from PdfManager import PdfManager
from NavBar import NavBar
from PyMus import PyMusData
import json
from typing import Optional

class MainWindow:
    def __init__(self, master) -> None:
        self.master: Tk = master
        self.master.title("Title Takeover!")
        self.master.geometry("500x500")
        self.height = 500
        self.width = 500

        # Set up defaults
        self.pdfManager: Optional[PdfManager] = None
        self.bottomNavBar: Optional[NavBar] = None

        # Set up menu
        self.menubar = Menu(self.master)
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.newFromPdf)
        self.fileMenu.add_command(label="Open", command=self.openPyMusFile)

        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.menubar)

    def resizeAll(self, width: int, height: int) -> None:
        self.height = height
        self.width = width
        if self.pdfManager is not None:
            self.pdfManager.resize(PhSize(self.width, self.height - 40))
        if self.bottomNavBar is not None:
            self.bottomNavBar.resize(PhSize(self.width, 40))
        print("Window", "Width:", self.width, "Height:", self.height)

    
    def resizeEvent(self, event) -> None:
        if(event.widget is self.master and (self.height != event.height or self.width != event.width)):
            self.resizeAll(event.width, event.height)
    
    def openPyMusFile(self) -> None:
        fpath = filedialog.askopenfilename(title="Select your PyMus File...", filetypes=[("PyMus files", "*.pymus")])
        if not fpath:
            raise Exception("Could not find specified file.")
        def callback() -> None:
            with open(fpath, "r") as pdfFile:
                pdfFileStr = pdfFile.read()
                self.pyMusData = PyMusData.from_json(pdfFileStr)
                
                pdfPane = Frame(self.master)
                pdfPane.grid(row=0, column=0)
                self.master.grid_rowconfigure(0, weight=1)
                # Set up Pdf Management
                self.pdfManager = PdfManager(pdfPane, self.pyMusData)

                bottomNavPane = Frame(self.master) 
                bottomNavPane.grid(row=1, column=0, sticky=NSEW)
                self.bottomNavBar = NavBar(bottomNavPane)

                # Set up master window events
                self.master.bind("<Configure>", func=self.resizeEvent)

                # Hook up children functions
                self.bottomNavBar.nextClickFuncs.append(self.pdfManager.NextPage)
                self.bottomNavBar.previousClickFuncs.append(self.pdfManager.PreviousPage)

                # Force Initial sizing
                self.resizeAll(self.width, self.height)

        self.master.after_idle(callback)
                

    def newFromPdf(self) -> None:
        if(self.pdfManager is not None):
            self.pdfManager.Remove()
            self.pdfManager = None
        if(self.bottomNavBar is not None):
            self.bottomNavBar.Remove()
            self.bottomNavBar = None

        fpath = filedialog.askopenfilename(title="Select your PDF...", filetypes=[("PDFs", "*.pdf")])

        def callback() -> None:
            if fpath:
                pdfPane = Frame(self.master)
                pdfPane.grid(row=0, column=0)
                # Set up Pdf Management
                self.pdfManager = PdfManager(pdfPane, fpath)

                bottomNavPane = Frame(self.master) 
                bottomNavPane.grid(row=1, column=0, sticky=NSEW)
                self.bottomNavBar = NavBar(bottomNavPane)

                # Set up master window events
                self.master.bind("<Configure>", func=self.resizeEvent)

                # Hook up children functions
                # self.bottomNavBar.nextClickFuncs.append(self.pdfManager.NextPage)
                # self.bottomNavBar.previousClickFuncs.append(self.pdfManager.PreviousPage)

                # Force Initial sizing
                self.resizeAll(self.width, self.height)
                return fpath
            else:
                raise Exception("Couldn't find given file.")
        self.master.after_idle(callback)