"""
__author__ = "Luis Gonzalez"
__version__ = "1.0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import tkinter as tk
from tkinter import messagebox
from conexion import insert_styles, delete_styles, show_styles, update_styles

def show_styles_interface(parent_frame):
    def refresh_styles_list():
        for widget in styles_list_frame.winfo_children():
            widget.destroy()
        estilos = show_styles()
        for estilo in estilos:
            tk.Label(styles_list_frame, text=f"{estilo[0]} - {estilo[1]}: {estilo[2]}").pack(anchor="w")

    def add_style():
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get()
        if nombre and descripcion:
            insert_styles(nombre, descripcion)
            refresh_styles_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_style():
        selected_id = id_entry.get()
        if selected_id:
            delete_styles(int(selected_id))
            refresh_styles_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del estilo a eliminar")

    def update_selected_style():
        selected_id = id_entry.get()
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get()
        if selected_id and nombre and descripcion:
            update_styles(int(selected_id), nombre, descripcion)
            refresh_styles_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    # Interfaz
    tk.Label(parent_frame, text="ID").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Nombre").pack()
    nombre_entry = tk.Entry(parent_frame)
    nombre_entry.pack()

    tk.Label(parent_frame, text="Descripción").pack()
    descripcion_entry = tk.Entry(parent_frame)
    descripcion_entry.pack()

    tk.Button(parent_frame, text="Agregar Estilo", command=add_style).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Estilo", command=update_selected_style).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Estilo", command=delete_selected_style).pack(fill="x", pady=5)

    styles_list_frame = tk.Frame(parent_frame)
    styles_list_frame.pack(fill="both", expand=True)
    refresh_styles_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
