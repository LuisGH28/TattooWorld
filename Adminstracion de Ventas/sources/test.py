import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def ejecutar_programa_contenido(funcion):
    # Limpiar el contenido del frame derecho
    for widget in frame_derecho.winfo_children():
        widget.destroy()
    
    # Llamar a la función que reemplazará el contenido del frame derecho
    funcion()

def mostrar_citas():
    # Crear un label con el mensaje de "Citas"
    etiqueta = tk.Label(frame_derecho, text="¡Aquí puedes hacer citas en Python con Tkinter!", font=("Helvetica", 16))
    etiqueta.pack(pady=20)

def cambiar_imagen(nueva_imagen):
    # Limpiar el contenido del frame derecho
    for widget in frame_derecho.winfo_children():
        widget.destroy()
    
    # Mostrar una nueva imagen en el frame derecho
    imagen_original = Image.open(nueva_imagen)
    imagen_original = imagen_original.resize((label_imagen.winfo_width(), label_imagen.winfo_height()))
    imagen_tk = ImageTk.PhotoImage(imagen_original)
    label_imagen.config(image=imagen_tk)
    label_imagen.pack(fill="both", expand=True)

def crear_interfaz():
    global frame_derecho, label_imagen

    ventana = tk.Tk()
    ventana.title("Interfaz con botones y ejecución de programas")

    # Crear frames
    frame_izquierdo = tk.Frame(ventana)
    frame_derecho = tk.Frame(ventana)
    frame_izquierdo.pack(side="left", fill="both", expand=True)
    frame_derecho.pack(side="right", fill="both", expand=True)

    # Cargar la imagen inicial
    imagen_original = Image.open("images/tattooWorld.png")
    imagen_tk = ImageTk.PhotoImage(imagen_original)

    # Crear label para la imagen
    label_imagen = tk.Label(frame_derecho, image=imagen_tk)
    label_imagen.pack(fill="both", expand=True)

    # Crear botones
    boton1 = tk.Button(frame_izquierdo, text="Citas", command=lambda: ejecutar_programa_contenido(mostrar_citas))
    boton2 = tk.Button(frame_izquierdo, text="Tatuadores", command=lambda: cambiar_imagen("tatuadores.webp"))
    # ... otros botones ...
    boton1.pack(fill="x", pady=5)
    boton2.pack(fill="x", pady=5)
    # ... otros pack() ...

    ventana.mainloop()

crear_interfaz()
