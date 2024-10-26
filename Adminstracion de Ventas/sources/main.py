"""
__author__ = "Luis Gonzalez"
__version__ = "1.0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import tkinter as tk
from PIL import Image, ImageTk

import conexion
import styles

def exec_content(fun):
    for widget in right_frame.winfo_children():
        widget.destroy()
        
    fun(right_frame) # this fuction change the frame's content

def change_background(new_image):
    for widget in right_frame.winfo_children():
        widget.destroy()
        
    wallpaper = Image.open(new_image)
    wallpaper = wallpaper.resize((label_imagen.winfo.width(),
                                  label_imagen.winfo_height()))
    imagen_tk = ImageTk.PhotoImage(wallpaper)
    label_imagen.config(image=imagen_tk)
    label_imagen.pack(fill="both", expand=True)
    
def create_interface():
    global right_frame, label_imagen
    
    window = tk.Tk()
    window.title("Tattoo World")
    
    left_frame = tk.Frame(window)
    right_frame = tk.Frame(window)
    left_frame.pack(side="left", fill="both", expand=True)
    right_frame.pack(side="right", fill="both", expand=True)
    
    wallpaper = Image.open("images/tattooWorld.png")
    imagen_tk = ImageTk.PhotoImage(wallpaper)
    
    # label to the image
    label_imagen = tk.Label(right_frame, image=imagen_tk)
    label_imagen.pack(fill='both', expand=True)
    
    # Buttons
    appointments = tk.Button(left_frame, text="Citas", command=lambda:
        exec_content(citas.form))
    appointments.pack(fill='x', pady=5)
    styles_button = tk.Button(left_frame, text="Estilos", command=lambda:
        exec_content(styles.show_styles))
    styles_button.pack(fill="x", pady=5)
    
    window.mainloop()

create_interface()