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

# Funciones CRUD para la tabla Clientes
def insert_client(nombre, apellido_p, apellido_m, telefono, correo):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Clientes (Nombre, Apellido_P, Apellido_M, Telefono, Correo) VALUES (?, ?, ?, ?, ?)",
                       (nombre, apellido_p, apellido_m, telefono, correo))
        conexion.commit()
        conexion.close()
        print("Cliente insertado correctamente.")

def delete_client(id_cliente):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Clientes WHERE idCliente = ?", (id_cliente,))
        conexion.commit()
        conexion.close()
        print(f"Cliente con ID {id_cliente} eliminado correctamente.")

def update_client(id_cliente, nombre, apellido_p, apellido_m, telefono, correo):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Clientes SET Nombre = ?, Apellido_P = ?, Apellido_M = ?, Telefono = ?, Correo = ? WHERE idCliente = ?",
                       (nombre, apellido_p, apellido_m, telefono, correo, id_cliente))
        conexion.commit()
        conexion.close()
        print(f"Cliente con ID {id_cliente} actualizado correctamente.")

def show_clients():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Clientes")
        clientes = cursor.fetchall()
        conexion.close()
        return clientes
    return []

# Interfaz de Clientes
def show_clients_interface(parent_frame):
    def refresh_clients_list():
        for widget in clients_list_frame.winfo_children():
            widget.destroy()
        clientes = show_clients()
        for cliente in clientes:
            tk.Label(clients_list_frame, text=f"{cliente[0]} - {cliente[1]} {cliente[2]} {cliente[3]}, Tel: {cliente[4]}, Correo: {cliente[5]}").pack(anchor="w")

    def add_client():
        nombre = nombre_entry.get()
        apellido_p = apellido_p_entry.get()
        apellido_m = apellido_m_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        if nombre and apellido_p and telefono and correo:
            insert_client(nombre, apellido_p, apellido_m, telefono, correo)
            refresh_clients_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_client():
        selected_id = id_entry.get()
        if selected_id:
            delete_client(int(selected_id))
            refresh_clients_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del cliente a eliminar")

    def update_selected_client():
        selected_id = id_entry.get()
        nombre = nombre_entry.get()
        apellido_p = apellido_p_entry.get()
        apellido_m = apellido_m_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        if selected_id and nombre and apellido_p and telefono and correo:
            update_client(int(selected_id), nombre, apellido_p, apellido_m, telefono, correo)
            refresh_clients_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    # UI Elements
    tk.Label(parent_frame, text="ID Cliente").pack()
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

    tk.Label(parent_frame, text="Teléfono").pack()
    telefono_entry = tk.Entry(parent_frame)
    telefono_entry.pack()

    tk.Label(parent_frame, text="Correo").pack()
    correo_entry = tk.Entry(parent_frame)
    correo_entry.pack()

    tk.Button(parent_frame, text="Agregar Cliente", command=add_client).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Cliente", command=update_selected_client).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Cliente", command=delete_selected_client).pack(fill="x", pady=5)

    clients_list_frame = tk.Frame(parent_frame)
    clients_list_frame.pack(fill="both", expand=True)
    refresh_clients_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        apellido_p_entry.delete(0, tk.END)
        apellido_m_entry.delete(0, tk.END)
        telefono_entry.delete(0, tk.END)
        correo_entry.delete(0, tk.END)
