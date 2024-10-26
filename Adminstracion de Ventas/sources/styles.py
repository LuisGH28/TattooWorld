"""
__author__ = "Luis Gonzalez"
__version__ = "1.0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import tkinter as tk

import conexion

def show_styles(frame):
    tk.Label(frame, text="Formulario de Estilos", font=("Helvetica", 16)).pack(pady=10)

    tk.Label(frame, text="idStyle:").pack(anchor="w", padx=10)
    entry_id = tk.Entry(frame)
    entry_id.pack(fill="x", padx=10, pady=5)

    tk.Label(frame, text="Nombre:").pack(anchor="w", padx=10)
    entry_name = tk.Entry(frame)
    entry_name.pack(fill="x", padx=10, pady=5)

    
    tk.Label(frame, text="Descripción:").pack(anchor="w", padx=10)
    entry_description = tk.Entry(frame)
    entry_description.pack(fill="x", padx=10, pady=5)

    
    frame_button = tk.Frame(frame)
    frame_button.pack(pady=20)

    save_button = tk.Button(frame_button, text="Guardar", command=lambda: save_style(entry_id, entry_name, entry_description))
    delete_button = tk.Button(frame_button, text="Eliminar", command=delete_style)
    new_button = tk.Button(frame_button, text="Nuevo", command=new_style)

    save_button.grid(row=0, column=0, padx=5)
    delete_button.grid(row=0, column=1, padx=5)
    new_button.grid(row=0, column=2, padx=5)

def save_style(entry_id, entry_name, entry_description):
    id_style = entry_id.get()
    nombre = entry_name.get()
    descripcion = entry_description.get()
    print(f"Guardado: idStyle={id_style}, Nombre={nombre}, Descripción={descripcion}")

def delete_style():
    print("Estilo eliminado")

def new_style():
    print("Formulario para nuevo estilo")