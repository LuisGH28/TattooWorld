from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame
from conexion import *
import time 

class Window(Frame):
    def __init__(self, master, *args):
        super().__init__(master,*args)
        
        self.menu = True
        self.color = True

        self.nombre = StringVar
        self.apellido_m = StringVar
        self.apellido_p = StringVar
        self.idStyle = StringVar
        self.idArea = StringVar
        self.search = StringVar()
        self.searchUpdate = StringVar()
        self.idTatuadores = StringVar()


        self.data_base = Data_logging()

        self.frame_begin = Frame(self.master, bg='black', width=50, height=45)
        self.frame_begin.grid_propagate(0)
        self.frame_begin.grid(column=0, row=0, sticky='nsew')

        self.frame_menu = Frame(self.master, bg='black', width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')

        self.frame_top = Frame(self.master, bg='black', height=50)
        self.frame_top.grid(column=1, row=0, sticky='nsew')

        self.frame_main = Frame(self.master, bg='black')
        self.frame_main.grid(column=1, row=1, sticky='nsew')

        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)

        self.frame_main.columnconfigure(0, weight=1)
        self.frame_main.rowconfigure(0, weight=1)

        self.widgets()

    def homeScreen(self):
        self.pages.select([self.frameOne])
    
    def dataScreen(self):
        self.pages.select([self.frameTwo])
        self.frameTwo.columnconfigure(0, weight=1)
        self.frameTwo.columnconfigure(1, weight=1)
        self.frameTwo.columnconfigure(2, weight=1)
        self.frameTwo.columnconfigure(0, weight=1)
        self.frameTwo.columnconfigure(0, weight=1)
        
    def screenWrite(self):
        self.pages.select([self.frameThree])
        self.frameThree.columnconfigure(0, weight=1)
        self.frameThree.columnconfigure(1, weght=1)
        
    def refreshScreen(self, frameFour):
        self.pages.select([self.frameFour])
        self.frameFour.columnconfigure(0, weight=1)
        self.frameFour.columnconfigure(1, weight=1)
    
    def searchScreen(self, frameFive):
        self.pages.select([self.frameFive])
        self.frameFive.columnconfigure(0, weight=1)
        self.frameFive.columnconfigure(1, weight=1)
        self.frameFive.columnconfigure(2, weight=1)
        self.frameFive.rowconfigure(2, weight=1)
        self.frameTableTwo.columnconfigure(0, weight=1)
        self.frameTableTwo.rowconfigure(0, weight=1)

    def lateralMenu(self):
        if self.menu is True:
            for i in range(50,170,10):
                self.frame_menu.config(width= i)
                self.frame_begin.config(width= i)
                self.frame_menu.update()
                click_begin = self.bt_close.grid_forget()
                if click_begin is None:
                    self.bt_begin.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_begin.grid_propagate(0)
                    self.bt.begin.config(width= i)
                    self.homeScreen()
            self.menu = False
        else:
            for i in range(50,170,10):
                self.frame_menu.config(width= i)
                self.frame_begin.config(width= i)
                self.frame_menu.update()
                click_begin = self.bt_begin.grid_forget()
                if click_begin is None:
                    self.frame_menu.grid_propagate(0)
                    self.bt_close.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_close.grid_propagate(0)
                    self.bt.close.config(width= i)
                    self.homeScreen()
            self.menu = True
    
    def wodgets(self):
        self.imageBegin = PhotoImage(file='home.png')
        self.imageMenu = PhotoImage(file='menu.png')
        self.imageData = PhotoImage(file='datos.png')
        self.imagenRegister = PhotoImage(file='editar.png')
        self.imageUpdate = PhotoImage(file='actualizar.png')
        self.imageSearch = PhotoImage(file='buscar.png')
        
