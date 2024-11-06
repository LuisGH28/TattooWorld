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

def insert_ticket(monto, cliente_id, cita_id):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Tickets (Monto, ClienteID, CitaID) VALUES (?, ?, ?)", 
                       (monto, cliente_id, cita_id))
        conexion.commit()
        conexion.close()
        print("Ticket insertado correctamente.")

def delete_ticket(id_ticket):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Tickets WHERE idTicket = ?", (id_ticket,))
        conexion.commit()
        conexion.close()
        print(f"Ticket con ID {id_ticket} eliminado correctamente.")

def update_ticket(id_ticket, monto, cliente_id, cita_id):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Tickets SET Monto = ?, ClienteID = ?, CitaID = ? WHERE idTicket = ?", 
                       (monto, cliente_id, cita_id, id_ticket))
        conexion.commit()
        conexion.close()
        print(f"Ticket con ID {id_ticket} actualizado correctamente.")

def show_tickets():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Tickets")
        tickets = cursor.fetchall()
        conexion.close()
        return tickets
    return []

# Interfaz de Tickets
def show_tickets_interface(parent_frame):
    def refresh_tickets_list():
        for widget in tickets_list_frame.winfo_children():
            widget.destroy()
        tickets = show_tickets()
        for ticket in tickets:
            tk.Label(tickets_list_frame, text=f"{ticket[0]} - Monto: {ticket[1]}, Cliente ID: {ticket[2]}, Cita ID: {ticket[3]}").pack(anchor="w")

    def add_ticket():
        monto = monto_entry.get()
        cliente_id = cliente_id_entry.get()
        cita_id = cita_id_entry.get()
        if monto and cliente_id and cita_id:
            insert_ticket(monto, cliente_id, cita_id)
            refresh_tickets_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_ticket():
        selected_id = id_entry.get()
        if selected_id:
            delete_ticket(int(selected_id))
            refresh_tickets_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del ticket a eliminar")

    def update_selected_ticket():
        selected_id = id_entry.get()
        monto = monto_entry.get()
        cliente_id = cliente_id_entry.get()
        cita_id = cita_id_entry.get()
        if selected_id and monto and cliente_id and cita_id:
            update_ticket(int(selected_id), monto, cliente_id, cita_id)
            refresh_tickets_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    # UI Elements
    tk.Label(parent_frame, text="ID Ticket").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Monto").pack()
    monto_entry = tk.Entry(parent_frame)
    monto_entry.pack()

    tk.Label(parent_frame, text="Cliente ID").pack()
    cliente_id_entry = tk.Entry(parent_frame)
    cliente_id_entry.pack()

    tk.Label(parent_frame, text="Cita ID").pack()
    cita_id_entry = tk.Entry(parent_frame)
    cita_id_entry.pack()

    tk.Button(parent_frame, text="Agregar Ticket", command=add_ticket).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Ticket", command=update_selected_ticket).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Ticket", command=delete_selected_ticket).pack(fill="x", pady=5)

    tickets_list_frame = tk.Frame(parent_frame)
    tickets_list_frame.pack(fill="both", expand=True)
    refresh_tickets_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        monto_entry.delete(0, tk.END)
        cliente_id_entry.delete(0, tk.END)
        cita_id_entry.delete(0, tk.END)
