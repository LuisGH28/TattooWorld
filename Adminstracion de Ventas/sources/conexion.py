""" 
__author__ = "Luis Gonzalez"
__version__ = "1.0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import sqlite3


def connect_db():
    try:
        conexion = sqlite3.connect('DB/tattoo_world.sqlite')  
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Función para crear la tabla si no existe
def create_table():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS estilos (
                            idStyle INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            descripcion TEXT NOT NULL
                        )''')
        conexion.commit()
        conexion.close()

# Función para insertar un nuevo estilo
def insert_styles(nombre, descripcion):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO estilos (nombre, descripcion) VALUES (?, ?)", (nombre, descripcion))
        conexion.commit()
        conexion.close()
        print("Estilo insertado correctamente.")

# Función para eliminar un estilo por su ID
def delete_styles(id_style):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estilos WHERE idStyle = ?", (id_style,))
        conexion.commit()
        conexion.close()
        print(f"Estilo con ID {id_style} eliminado correctamente.")

# Función para obtener todos los estilos
def show_styles():
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estilos")
        estilos = cursor.fetchall()
        conexion.close()
        return estilos
    return []

# Función para actualizar un estilo
def update_styles(id_style, nombre, descripcion):
    conexion = connect_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE estilos SET nombre = ?, descripcion = ? WHERE idStyle = ?", (nombre, descripcion, id_style))
        conexion.commit()
        conexion.close()
        print(f"Estilo con ID {id_style} actualizado correctamente.")

