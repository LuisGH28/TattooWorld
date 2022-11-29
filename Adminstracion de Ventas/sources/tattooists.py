"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

from tkinter import *
from tkinter import ttk
from conexion import *
from tkinter import messagebox

class Ventana(Frame):

    tatuador = Conecction()

    def __init__(self, master=None):
        super().__init__(master, width=680, height=360)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
        self.id=-1      
            
    def habilitarCajas(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtAM.configure(state=estado)
        self.txtAP.configure(state=estado)
        self.txtEstilo.configure(state=estado)
        self.txtArea.configure(state=estado)

        
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtNombre.delete(0,END)
        self.txtAM.delete(0,END)
        self.txtAP.delete(0,END)
        self.txtEstilo.delete(0,END)
        self.txtArea.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenaDatos(self):
        datos= self.tatuador.consulta_datos()

        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4], row[5]))
                    
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )

    def fNuevo(self):
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtNombre.focus()

    def fModificar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()            
            self.txtNombre.insert(0,valores[0])
            self.txtAM.insert(0,valores[1])
            self.txtAP.insert(0,valores[2])
            self.txtEstilo.insert(0,valores[3])
            self.txtArea.insert(0,valores[4])
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtNombre.focus()

    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.tatuador.elimina_tatuador(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def fGuardar(self):
        if self.id ==-1:       
            self.tatuador.inserta_tatuador(self.txtNombre.get(),self.txtAM.get(),self.txtAP.get(),self.txtEstilo.get(),self.txtArea.get())           
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.tatuador.modifica_tatuador(self.id,self.txtNombre.get(),self.txtAM.get(),self.txtAP.get(),self.txtEstilo.get(),self.txtArea.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1
        self.limpiaGrid()
        self.llenaDatos()  
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")

    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=193, height=359)

        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="White")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar=Button(frame1, text="Modificr", command=self.fModificar, bg="blue", fg="White")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="White")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        frame2 = Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=359)

        lbl1 = Label(frame2, text="Nombre: ")
        lbl1.place(x=3,y=5)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=50,height=20)

        lbl2 = Label(frame2, text="Apellido M: ")
        lbl2.place(x=3,y=55)
        self.txtAM=Entry(frame2)
        self.txtAM.place(x=3,y=75,width=100,height=20)

        lbl3 = Label(frame2, text="Apellido P: ")
        lbl3.place(x=3,y=105)
        self.txtAP=Entry(frame2)
        self.txtAP.place(x=3,y=125,width=150,height=20)

        lbl4 = Label(frame2, text="Estilo: ")
        lbl4.place(x=3,y=155)
        self.txtEstilo=Entry(frame2)
        self.txtEstilo.place(x=3,y=175,width=200,height=20)

        lbl5 = Label(frame2, text="Area: ")
        lbl5.place(x=3,y=205)
        self.txtArea=Entry(frame2)
        self.txtArea.place(x=3,y=225,width=250,height=20)

        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=260, width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="green", fg="white")
        self.btnCancelar.place(x=80, y=260, width=60, height=30)

        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=259) 
        
        self.grid = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5"))

        self.grid.column("#0", width=50)
        self.grid.column("col1", width=60, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=70, anchor=CENTER)
        self.grid.column("col5", width=70, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido M", anchor=CENTER)
        self.grid.heading("col3", text="Apellido P", anchor=CENTER)
        self.grid.heading("col5", text="Area", anchor=CENTER)

        self.grid.place(x=247, y=0, width=420, height=340)
        self.grid.heading("col4", text="Estilo", anchor=CENTER)
   
       
        self.grid['selectmode']='browse' 