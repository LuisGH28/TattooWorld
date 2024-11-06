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
import citas
import styles
import area 
import tattooists
import clients
import tickets
import stock


def exec_content(fun):
    for widget in right_frame.winfo_children():
        widget.destroy()
    fun(right_frame)  # Cambia el contenido del frame

def change_background(new_image):
    for widget in right_frame.winfo_children():
        widget.destroy()

    wallpaper = Image.open(new_image)
    wallpaper = wallpaper.resize((label_imagen.winfo_width(), label_imagen.winfo_height()))
    imagen_tk = ImageTk.PhotoImage(wallpaper)
    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk  # Actualiza la referencia de la imagen
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

    # Label para la imagen de fondo
    label_imagen = tk.Label(right_frame, image=imagen_tk)
    label_imagen.image = imagen_tk  # Mantiene la referencia de la imagen
    label_imagen.pack(fill='both', expand=True)

    # Botones en el marco izquierdo
    appointments_button = tk.Button(left_frame, text="Citas", command=lambda: exec_content(citas.show_appointments_interface))
    appointments_button.pack(fill='x', pady=5)

    styles_button = tk.Button(left_frame, text="Estilos", command=lambda: exec_content(styles.show_styles_interface))
    styles_button.pack(fill="x", pady=5)

    area_button = tk.Button(left_frame, text="Area", command=lambda: exec_content(area.show_areas_interface))
    area_button.pack(fill="x", pady=5)

    tattooists_button = tk.Button(left_frame, text="Tatuadores", command=lambda: exec_content(tattooists.show_tattooists_interface))
    tattooists_button.pack(fill="x", pady=5)
    
    clients_button = tk.Button(left_frame, text="Cleintes", command=lambda: exec_content(clients.show_clients_interface))
    clients_button.pack(fill="x", pady=5)
    
    tickets_button = tk.Button(left_frame, text="Tickets", command=lambda: exec_content(tickets.show_tickets_interface))
    tickets_button.pack(fill="x", pady=5)
    
    stock_button = tk.Button(left_frame, text="Stock", command=lambda: exec_content(stock.show_stock_interface))
    stock_button.pack(fill="x", pady=5)
    
    window.mainloop()
    
create_interface()
