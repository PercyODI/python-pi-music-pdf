from tkinter import Frame, NSEW, Menu 
from tkinter import filedialog
from Util import *
from PdfFrame import PdfFrame
from PdfManager import PdfManager
from NavBar import NavBar

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Title Takeover!")
        self.master.geometry("500x500")
        self.height = 500
        self.width = 500

        # Set up defaults
        self.pdfManager = None
        self.bottomNavBar = None

        # Set up menu
        self.menubar = Menu(self.master)
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.loadPdfFile) 
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.menubar)

    def resizeAll(self, width: int, height: int):
        self.height = height
        self.width = width
        self.pdfManager.resize(PhSize(self.width, self.height - 40))
        self.bottomNavBar.resize(PhSize(self.width, 40))
        print("Window", "Width:", self.width, "Height:", self.height)

    
    def resizeEvent(self, event):
        if(event.widget is self.master and (self.height != event.height or self.width != event.width)):
            self.resizeAll(event.width, event.height)
    
    def loadPdfFile(self):
        if(self.pdfManager is not None):
            self.pdfManager.Remove()
            self.pdfManager = None
        if(self.bottomNavBar is not None):
            self.bottomNavBar.Remove()
            self.bottomNavBar = None

        fpath = filedialog.askopenfilename(title="Select your PDF...", filetypes=[("PDFs", "*.pdf")])

        def callback():
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
                self.bottomNavBar.nextClickFuncs.append(self.pdfManager.NextPage)
                self.bottomNavBar.previousClickFuncs.append(self.pdfManager.PreviousPage)

                # Force Initial sizing
                self.resizeAll(self.width, self.height)
                return fpath
            else:
                raise Exception("Couldn't find given file.")
        self.master.after_idle(callback)