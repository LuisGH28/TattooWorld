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

        


