"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

from tkinter import * 
from tkinter.ttk import *
from ast import Lambda
from faulthandler import disable
from importlib.metadata import entry_points
from ipaddress import collapse_addresses
from lib2to3.pygram import pattern_symbols
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from tkinter import ttk
from conexion import *
from tattooists import *
from styles import *
from area import *
from recepcionista import *


master = Tk() 
master.title("TattooWorld")
master.geometry("200x200") 


def openNewWindow(): 
    def main():
        root = Tk()
        root.wm_title("Tatuadores")
        app = Ventana(root)
        app.mainloop()

    if __name__ == "__main__":
        main()
    
def openStyle(): 
    def main():
        root = Tk()
        root.wm_title("Estilos")
        app = Estilo(root)
        app.mainloop()

    if __name__ == "__main__":
        main()

def openArea(): 
    def main():
        root = Tk()
        root.wm_title("Area")
        app = Area(root)
        app.mainloop()

    if __name__ == "__main__":
        main()

def openRecp(): 
    def main():
        root = Tk()
        root.wm_title("Recepcionistas")
        app = Recepcionista(root)
        app.mainloop()

    if __name__ == "__main__":
        main()

btn = Button(master, text ="Tatuadores", command = openNewWindow) 
btn.pack(pady = 10) 

btn = Button(master, text ="Estilos", command = openStyle) 
btn.pack(pady = 10) 

btn = Button(master, text ="Areas", command = openArea) 
btn.pack(pady = 10) 

btn = Button(master, text ="Recepcionistas", command = openRecp) 
btn.pack(pady = 10)

mainloop() 