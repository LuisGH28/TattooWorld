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

def insert_tatuador(nombre, apellido_p, apellido_m, estilo, area):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Tatuadores (Nombre, Apellido_P, Apellido_M, Estilo, Area) VALUES (?, ?, ?, ?, ?)",
                       (nombre, apellido_p, apellido_m, estilo, area))
        conexion.commit()
        conexion.close()
        print("Tatuador insertado correctamente.")

def delete_tatuador(id_tatuador):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Tatuadores WHERE idTatuador = ?", (id_tatuador,))
        conexion.commit()
        conexion.close()
        print(f"Tatuador con ID {id_tatuador} eliminado correctamente.")

def update_tatuador(id_tatuador, nombre, apellido_p, apellido_m, estilo, area):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Tatuadores SET Nombre = ?, Apellido_P = ?, Apellido_M = ?, Estilo = ?, Area = ? WHERE idTatuador = ?",
                       (nombre, apellido_p, apellido_m, estilo, area, id_tatuador))
        conexion.commit()
        conexion.close()
        print(f"Tatuador con ID {id_tatuador} actualizado correctamente.")

def show_tatuadores():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Tatuadores")
        tatuadores = cursor.fetchall()
        conexion.close()
        return tatuadores
    return []

def show_tattooists_interface(parent_frame):
    def refresh_tatuadores_list():
        for widget in tatuadores_list_frame.winfo_children():
            widget.destroy()
        tatuadores = show_tatuadores()
        for tatuador in tatuadores:
            tk.Label(tatuadores_list_frame, text=f"{tatuador[0]} - {tatuador[1]} {tatuador[2]} {tatuador[3]}, Estilo ID: {tatuador[4]}, Área ID: {tatuador[5]}").pack(anchor="w")

    def add_tatuador():
        nombre = nombre_entry.get()
        apellido_p = apellido_p_entry.get()
        apellido_m = apellido_m_entry.get()
        estilo = estilo_entry.get()
        area = area_entry.get()
        if nombre and apellido_p and estilo and area:
            insert_tatuador(nombre, apellido_p, apellido_m, estilo, area)
            refresh_tatuadores_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_tatuador():
        selected_id = id_entry.get()
        if selected_id:
            delete_tatuador(int(selected_id))
            refresh_tatuadores_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del tatuador a eliminar")

    def update_selected_tatuador():
        selected_id = id_entry.get()
        nombre = nombre_entry.get()
        apellido_p = apellido_p_entry.get()
        apellido_m = apellido_m_entry.get()
        estilo = estilo_entry.get()
        area = area_entry.get()
        if selected_id and nombre and apellido_p and estilo and area:
            update_tatuador(int(selected_id), nombre, apellido_p, apellido_m, estilo, area)
            refresh_tatuadores_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    tk.Label(parent_frame, text="ID").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Nombre").pack()
    nombre_entry = tk.Entry(parent_frame)
    nombre_entry.pack()

    tk.Label(parent_frame, text="Apellido Paterno").pack()
    apellido_p_entry = tk.Entry(parent_frame)
    apellido_p_entry.pack()

    tk.Label(parent_frame, text="Apellido Materno").pack()
    apellido_m_entry = tk.Entry(parent_frame)
    apellido_m_entry.pack()

    tk.Label(parent_frame, text="Estilo ID").pack()
    estilo_entry = tk.Entry(parent_frame)
    estilo_entry.pack()

    tk.Label(parent_frame, text="Área ID").pack()
    area_entry = tk.Entry(parent_frame)
    area_entry.pack()

    tk.Button(parent_frame, text="Agregar Tatuador", command=add_tatuador).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Tatuador", command=update_selected_tatuador).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Tatuador", command=delete_selected_tatuador).pack(fill="x", pady=5)

    tatuadores_list_frame = tk.Frame(parent_frame)
    tatuadores_list_frame.pack(fill="both", expand=True)
    refresh_tatuadores_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        apellido_p_entry.delete(0, tk.END)
        apellido_m_entry.delete(0, tk.END)
        estilo_entry.delete(0, tk.END)
        area_entry.delete(0, tk.END)
