__author__ = "Luis Gonzalez"
__version__ = "1.0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"

import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def exec_content(fun):
    for widget in right_frame.winfo_children():
        widget.destroy()
        
    fun() # this fuction change the frame's content
    
# Ventana principal
master = Tk() 
master.title("TattooWorld")
master.geometry("200x200") 

# Función para abrir ventana de Tatuadores
def openNewWindow(): 
    root = Toplevel(master)
    root.wm_title("Tatuadores")
    app = Ventana(root)
    app.mainloop()

# Función para abrir ventana de Estilos
def openStyle(): 
    root = Toplevel(master)
    root.wm_title("Estilos")
    app = Estilo(root)
    app.mainloop()

# Función para abrir ventana de Áreas
def openArea(): 
    root = Toplevel(master)
    root.wm_title("Áreas")
    app = Area(root)
    app.mainloop()

# Función para abrir ventana de Recepcionistas
def openRecp(): 
    root = Toplevel(master)
    root.wm_title("Recepcionistas")
    app = Recepcionista(root)
    app.mainloop()

# Botones para abrir diferentes ventanas
btn = Button(master, text="Tatuadores", command=openNewWindow)
btn.pack(pady=10)

btn = Button(master, text="Estilos", command=openStyle)
btn.pack(pady=10)

btn = Button(master, text="Áreas", command=openArea)
btn.pack(pady=10)

btn = Button(master, text="Recepcionistas", command=openRecp)
btn.pack(pady=10)

mainloop()
