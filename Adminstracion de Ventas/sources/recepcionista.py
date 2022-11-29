"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

from tkinter import *
from tkinter import ttk
from recepcionistaConeection import *
from tkinter import messagebox


class Recepcionista(Frame):
    
    recepcionista = Receptionistconeection()
        
    def __init__(self, master=None):
        super().__init__(master,width=680, height=260)
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
        self.txtapellidoM.configure(state=estado)
        self.txtapellidoP.configure(state=estado)
        self.txtCelular.configure(state=estado)
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
        self.txtapellidoM.delete(0,END)
        self.txtapellidoP.delete(0,END)
        self.txtCelular.delete(0,END)
        self.txtArea.delete(0,END)

        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatos(self):
        datos = self.recepcionista.consulta_recp()        
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
    
    def fGuardar(self): 
        if self.id ==-1:       
            self.recepcionista.inserta_recp(self.txtNombre.get(),self.txtapellidoM.get(),self.txtapellidoP.get(),self.txtCelular.get(),self.txtArea.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.recepcionista.modifica_recp(self.txtNombre.get(),self.txtapellidoM.get(),self.txtapellidoP.get(),self.txtCelular.get(),self.txtArea.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
                    
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
            self.txtapellidoM.insert(0,valores[1])
            self.txtapellidoP.insert(0,valores[2])
            self.txtCelular.insert(0,valores[3])            
            self.txtArea.insert(0, valores[4])
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtISO3.focus()
                                        
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
                n = self.recepcionista.elimina_recp(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=193, height=359)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30) 

        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=193, height=359)                        
        lbl1 = Label(frame2,text="Nombre: ")
        lbl1.place(x=3,y=5)        
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=50, height=20)                
        lbl2 = Label(frame2,text="Apellido M: ")
        lbl2.place(x=3,y=55)        
        self.txtapellidoM=Entry(frame2)
        self.txtapellidoM.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Apellido P: ")
        lbl3.place(x=3,y=105)        
        self.txtapellidoP=Entry(frame2)
        self.txtapellidoP.place(x=3,y=125,width=100, height=20)        
        lbl4 = Label(frame2,text="Celular: ")
        lbl4.place(x=3,y=155)        
        self.txtCelular=Entry(frame2)
        self.txtCelular.place(x=3,y=175,width=50, height=20)
        lbl5 = Label(frame2,text="Area: ")
        lbl5.place(x=3,y=205)        
        self.txtArea=Entry(frame2)
        self.txtArea.place(x=3,y=225,width=50, height=20)  

        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=80,y=200,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=230,width=60, height=30)    

        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=259)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4", "col5"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)   
        self.grid.column("col5",width=60, anchor=CENTER)      
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido M", anchor=CENTER)
        self.grid.heading("col3", text="Apellido P", anchor=CENTER)
        self.grid.heading("col4", text="Celular", anchor=CENTER)   
        self.grid.heading("col5", text="Area", anchor=CENTER)             
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'