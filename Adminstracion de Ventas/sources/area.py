"""
    __author__ = "Luis Gonzalez"
    __version__ = "1.0.1"
    __maintainer__ = "Luis Gonzalez"
    __email__ = "luisgnzhdz@gmail.com"
    __status__ = "Production"
"""


import tkinter as tk
from tkinter import messagebox
from conexion import connect_db

def insert_area(nombre):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Area (Nombre_Area) VALUES (?)", (nombre,))
        conexion.commit()
        conexion.close()
        print("Área insertada correctamente.")

def delete_area(id_area):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Area WHERE idArea = ?", (id_area,))
        conexion.commit()
        conexion.close()
        print(f"Área con ID {id_area} eliminada correctamente.")

def update_area(id_area, nombre):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Area SET Nombre_Area = ? WHERE idArea = ?", (nombre, id_area))
        conexion.commit()
        conexion.close()
        print(f"Área con ID {id_area} actualizada correctamente.")

def show_areas():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Area")
        areas = cursor.fetchall()
        conexion.close()
        return areas
    return []

def show_areas_interface(parent_frame):
    def refresh_areas_list():
        for widget in areas_list_frame.winfo_children():
            widget.destroy()
        areas = show_areas()
        for area in areas:
            tk.Label(areas_list_frame, text=f"{area[0]} - {area[1]}").pack(anchor="w")

    def add_area():
        nombre = nombre_entry.get()
        if nombre:
            insert_area(nombre)
            refresh_areas_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "El campo de nombre es obligatorio")

    def delete_selected_area():
        selected_id = id_entry.get()
        if selected_id:
            delete_area(int(selected_id))
            refresh_areas_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del área a eliminar")

    def update_selected_area():
        selected_id = id_entry.get()
        nombre = nombre_entry.get()
        if selected_id and nombre:
            update_area(int(selected_id), nombre)
            refresh_areas_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    tk.Label(parent_frame, text="ID").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Nombre").pack()
    nombre_entry = tk.Entry(parent_frame)
    nombre_entry.pack()

    tk.Button(parent_frame, text="Agregar Área", command=add_area).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Área", command=update_selected_area).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Área", command=delete_selected_area).pack(fill="x", pady=5)

    areas_list_frame = tk.Frame(parent_frame)
    areas_list_frame.pack(fill="both", expand=True)
    refresh_areas_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
