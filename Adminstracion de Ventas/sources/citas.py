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

# Funciones CRUD para la tabla Citas
def insert_appointment(fecha, hora, cliente_id, tatuador_id):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Citas (Fecha, Hora, ClienteID, TatuadorID) VALUES (?, ?, ?, ?)", 
                       (fecha, hora, cliente_id, tatuador_id))
        conexion.commit()
        conexion.close()
        print("Cita insertada correctamente.")

def delete_appointment(id_cita):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Citas WHERE idCita = ?", (id_cita,))
        conexion.commit()
        conexion.close()
        print(f"Cita con ID {id_cita} eliminada correctamente.")

def update_appointment(id_cita, fecha, hora, cliente_id, tatuador_id):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Citas SET Fecha = ?, Hora = ?, ClienteID = ?, TatuadorID = ? WHERE idCita = ?", 
                       (fecha, hora, cliente_id, tatuador_id, id_cita))
        conexion.commit()
        conexion.close()
        print(f"Cita con ID {id_cita} actualizada correctamente.")

def show_appointments():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Citas")
        citas = cursor.fetchall()
        conexion.close()
        return citas
    return []

# Interfaz de Citas
def show_appointments_interface(parent_frame):
    def refresh_appointments_list():
        for widget in appointments_list_frame.winfo_children():
            widget.destroy()
        citas = show_appointments()
        for cita in citas:
            tk.Label(appointments_list_frame, text=f"{cita[0]} - Fecha: {cita[1]}, Hora: {cita[2]}, Cliente ID: {cita[3]}, Tatuador ID: {cita[4]}").pack(anchor="w")

    def add_appointment():
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        cliente_id = cliente_id_entry.get()
        tatuador_id = tatuador_id_entry.get()
        if fecha and hora and cliente_id and tatuador_id:
            insert_appointment(fecha, hora, cliente_id, tatuador_id)
            refresh_appointments_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_appointment():
        selected_id = id_entry.get()
        if selected_id:
            delete_appointment(int(selected_id))
            refresh_appointments_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID de la cita a eliminar")

    def update_selected_appointment():
        selected_id = id_entry.get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        cliente_id = cliente_id_entry.get()
        tatuador_id = tatuador_id_entry.get()
        if selected_id and fecha and hora and cliente_id and tatuador_id:
            update_appointment(int(selected_id), fecha, hora, cliente_id, tatuador_id)
            refresh_appointments_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    # UI Elements
    tk.Label(parent_frame, text="ID Cita").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Fecha").pack()
    fecha_entry = tk.Entry(parent_frame)
    fecha_entry.pack()

    tk.Label(parent_frame, text="Hora").pack()
    hora_entry = tk.Entry(parent_frame)
    hora_entry.pack()

    tk.Label(parent_frame, text="Cliente ID").pack()
    cliente_id_entry = tk.Entry(parent_frame)
    cliente_id_entry.pack()

    tk.Label(parent_frame, text="Tatuador ID").pack()
    tatuador_id_entry = tk.Entry(parent_frame)
    tatuador_id_entry.pack()

    tk.Button(parent_frame, text="Agregar Cita", command=add_appointment).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Cita", command=update_selected_appointment).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Cita", command=delete_selected_appointment).pack(fill="x", pady=5)

    appointments_list_frame = tk.Frame(parent_frame)
    appointments_list_frame.pack(fill="both", expand=True)
    refresh_appointments_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        fecha_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)
        cliente_id_entry.delete(0, tk.END)
        tatuador_id_entry.delete(0, tk.END)
