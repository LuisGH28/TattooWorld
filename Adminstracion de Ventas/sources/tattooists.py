import tkinter as tk
from ast import Lambda
from faulthandler import disable
from importlib.metadata import entry_points
from ipaddress import collapse_addresses
from lib2to3.pygram import pattern_symbols
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from tkinter import ttk
from conexion import *

window=Tk() 
window.title("Tatuadores")
window.geometry("600x500")




Db=DataBase()
modify = False
Nombre=StringVar()
AP=StringVar()
AM=StringVar()
Estilo=StringVar()
Area=StringVar()

def tattoClick(event):
    idTatuador=tvTattooists.selection()[0]
    if int(idTatuador)>0:
        Nombre.set(tvTattooists.item(idTatuador, "values")[1])
        AP.set(tvTattooists.item(idTatuador, "values")[2])
        AM.set(tvTattooists.item(idTatuador, "values")[3])
        Estilo.set(tvTattooists.item(idTatuador, "values")[4])
        Area.set(tvTattooists.item(idTatuador, "values")[5])


frame=LabelFrame(window, text="Ingreso de Tatuadores")
frame.place(x=50, y=50, width=500, height=400)

#Labels and Entrys
lblNombre = Label(frame, text="Nombre:").grid(column=0, row=0, padx=5, pady=5)
txtNombre = Entry(frame, textvariable=Nombre)
txtNombre.grid(column=1, row=0)

lblAp=Label(frame, text="Apellido Paterno").grid(column=0,row=1, padx=5, pady=5)
txtAp=Entry(frame, textvariable=AP)
txtAp.grid(column=1, row=1)

lblAm=Label(frame, text="Apellido Materno").grid(column=0, row=2, padx=5, pady=5)
txtAm=Entry(frame, textvariable=AM)
txtAm.grid(column=1, row=2)

lblEstilo=Label(frame, text="Estilo").grid(column=2, row=0, padx=5, pady=5)
txtEstilo=Entry(frame, textvariable=Estilo)
txtEstilo.grid(column=3, row=0)

lblArea=Label(frame, text="Area").grid(column=2, row=1, padx=5, pady=5)
txtArea=Entry(frame, textvariable=Area)
txtArea.grid(column=3, row=1)

lblMessage=Label (frame, text="Aqui van los mensajes", fg="gray")
lblMessage.grid(column=0, row=3, columnspan=4)

#Tables of Workers

tvTattooists=ttk.Treeview(frame, selectmode=NONE)

tvTattooists["columns"]=("ID","Nombre", "Apellido Paterno", "Apellido Materno", "Estilo", "Area")
tvTattooists.column("#0", width=0, stretch=NO)
tvTattooists.column("ID", width=50, anchor=CENTER)
tvTattooists.column("Nombre", width=50, anchor=CENTER)
tvTattooists.column("Apellido Paterno", width=50, anchor=CENTER)
tvTattooists.column("Apellido Materno", width=50, anchor=CENTER)
tvTattooists.column("Estilo", width=50, anchor=CENTER)
tvTattooists.column("Area", width=50, anchor=CENTER)
tvTattooists.heading("#0", text="")
tvTattooists.heading("ID", text="ID", anchor=CENTER)
tvTattooists.heading("Nombre", text="Nombre", anchor=CENTER)
tvTattooists.heading("Apellido Paterno", text="Apellido Paterno", anchor=CENTER)
tvTattooists.heading("Apellido Materno", text="Apellido Materno", anchor=CENTER)
tvTattooists.heading("Estilo", text="Estilo", anchor=CENTER)
tvTattooists.heading("Area", text="Area", anchor=CENTER)

tvTattooists.grid(column=0, row=5, columnspan=4, padx=20)
tvTattooists.bind("<<TreeviewSelect>>", tattoClick)

#Action Bottom

btnDelete=Button(frame, text="Eliminar", command= lambda:delete())
btnDelete.grid(column=1, row=7)


btnAdd=Button(frame, text="Agregar", command=lambda:add())
btnAdd.grid(column=2, row=7)


btnUpdate=Button(frame, text="Seleecionar", command=lambda:update())
btnUpdate.grid(column=3, row=7)

#Fuction of CRUD

def modifyFalse():
    global modify
    modify = False
    tvTattooists.config(selectmode=NONE)
    btnAdd.config(text="Guardar")
    btnUpdate.config(text="Seleccionar")
    btnDelete.config(state=DISABLED)

def modifyTrue():
    global modify
    modify = True
    tvTattooists.config(selectmode=BROWSE)
    btnAdd.config(text="Agregar")
    btnUpdate.config(text="Actualizar")
    btnDelete.config(state=NORMAL)

def validate():
    return len(Nombre.get()) and len(AP.get()) and len(AM.get()) and len(Estilo.get()) and len(Area.get())

def clear():
    Nombre.set("")
    AP.set("")
    AM.set("")
    Estilo.set("")
    Area.set("")

def emptyTable():
    filas = tvTattooists.get_children()
    for fila in filas:
        tvTattooists.delete(fila)


def fillTable():
    emptyTable()
    sql="select * from Tatuadores"
    Db.cursor.execute(sql)
    filas=Db.cursor.fetchall()
    for fila in filas:
        id=fila[0]
        tvTattooists.insert("", END, id, text= id, values= fila )

def delete():
    idTatuadores=tvTattooists.selection()[0]
    if int(idTatuadores)>0:
        sql="delete from Tatuadores where idTatuador="+idTatuadores
        Db.cursor.execute(sql)
        Db.connection.commit()
        tvTattooists.delete(idTatuadores)
        lblMessage.config(text="Se ha eliminado el registro correctamente")
        clear()
    else:
        lblMessage.config(text="No se pudo eliminar el registro, verifique que se haya seleccionado un registro")

def add():
    if modify == False:
        if validate():
            val=(Nombre.get(),AP.get(),AM.get(),Estilo.get(),Area.get())
            sql="insert into Tatuadores (Nombre, Apellido_P, Apellido_M, Estilo, Area) values(%s, %s, %s, %s, %s)"
            Db.cursor.execute(sql, val)
            Db.connection.commit()
            lblMessage.config(text="El registro se guardo correctamente", fg="green")
            fillTable()
            clear()
        else:
            lblMessage.config(text="Los campos no deben de estar vacios >:V", fg="red")
    else:
        modifyFalse()

def update():
    if modify == True:
        if validate():
            id=tvTattooists.selection()[0]
            val=(Nombre.get(),AP.get(),AM.get(),Estilo.get(),Area.get())
            sql="update Tatuadores set Nombre=%s, Apellido_P=%s, Apellido_M=%s, Estilo=%s, Area=%s where idTatuador=" +id
            Db.cursor.execute(sql, val)
            Db.connection.commit()
            lblMessage.config(text="El registro se actualizo correctamente", fg="green")
            fillTable()
            clear()
        else:
            lblMessage.config(text="Los campos no deben de estar vacios >:V", fg="red")
    else:
        modifyTrue()


fillTable()
window.mainloop()