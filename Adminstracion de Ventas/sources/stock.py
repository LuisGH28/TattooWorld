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

# Funciones CRUD para la tabla Stock
def insert_stock(item, cantidad, precio):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Stock (Item, Cantidad, Precio) VALUES (?, ?, ?)",
                       (item, cantidad, precio))
        conexion.commit()
        conexion.close()
        print("Artículo de stock insertado correctamente.")

def delete_stock(id_stock):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Stock WHERE idStock = ?", (id_stock,))
        conexion.commit()
        conexion.close()
        print(f"Artículo de stock con ID {id_stock} eliminado correctamente.")

def update_stock(id_stock, item, cantidad, precio):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE Stock SET Item = ?, Cantidad = ?, Precio = ? WHERE idStock = ?",
                       (item, cantidad, precio, id_stock))
        conexion.commit()
        conexion.close()
        print(f"Artículo de stock con ID {id_stock} actualizado correctamente.")

def show_stock():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Stock")
        stock_items = cursor.fetchall()
        conexion.close()
        return stock_items
    return []

# Interfaz de Stock
def show_stock_interface(parent_frame):
    def refresh_stock_list():
        for widget in stock_list_frame.winfo_children():
            widget.destroy()
        stock_items = show_stock()
        for item in stock_items:
            tk.Label(stock_list_frame, text=f"{item[0]} - {item[1]}, Cantidad: {item[2]}, Precio: {item[3]}").pack(anchor="w")

    def add_stock_item():
        item = item_entry.get()
        cantidad = cantidad_entry.get()
        precio = precio_entry.get()
        if item and cantidad and precio:
            insert_stock(item, cantidad, precio)
            refresh_stock_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_selected_stock_item():
        selected_id = id_entry.get()
        if selected_id:
            delete_stock(int(selected_id))
            refresh_stock_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del artículo a eliminar")

    def update_selected_stock_item():
        selected_id = id_entry.get()
        item = item_entry.get()
        cantidad = cantidad_entry.get()
        precio = precio_entry.get()
        if selected_id and item and cantidad and precio:
            update_stock(int(selected_id), item, cantidad, precio)
            refresh_stock_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios para actualizar")

    # UI Elements
    tk.Label(parent_frame, text="ID Stock").pack()
    id_entry = tk.Entry(parent_frame)
    id_entry.pack()

    tk.Label(parent_frame, text="Artículo").pack()
    item_entry = tk.Entry(parent_frame)
    item_entry.pack()

    tk.Label(parent_frame, text="Cantidad").pack()
    cantidad_entry = tk.Entry(parent_frame)
    cantidad_entry.pack()

    tk.Label(parent_frame, text="Precio").pack()
    precio_entry = tk.Entry(parent_frame)
    precio_entry.pack()

    tk.Button(parent_frame, text="Agregar Artículo", command=add_stock_item).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Actualizar Artículo", command=update_selected_stock_item).pack(fill="x", pady=5)
    tk.Button(parent_frame, text="Eliminar Artículo", command=delete_selected_stock_item).pack(fill="x", pady=5)

    stock_list_frame = tk.Frame(parent_frame)
    stock_list_frame.pack(fill="both", expand=True)
    refresh_stock_list()

    def clear_entries():
        id_entry.delete(0, tk.END)
        item_entry.delete(0, tk.END)
        cantidad_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
