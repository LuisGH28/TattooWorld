import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Sistema de Citas")

    # Crear un label con el mensaje
    etiqueta = tk.Label(ventana, text="¡Aquí puedes hacer citas en Python con Tkinter!", font=("Helvetica", 16))
    etiqueta.pack(pady=20)

    ventana.mainloop()

crear_ventana()