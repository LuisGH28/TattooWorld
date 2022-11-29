"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import mysql.connector

class Styleconeection:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="mininaluz19", database="TattooWorld")
 
    def __str__(self):
        datos=self.consulta_estilos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_estilos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Style_Tattoo")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_estilo(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM Style_Tattoo WHERE idStyle = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_estilo(self,Nombre, descripcion):
        cur = self.cnn.cursor()
        sql='''INSERT INTO Style_Tattoo (Nombre, Descripcion) 
        VALUES('{}', '{}')'''.format(Nombre, descripcion)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_estilo(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Style_Tattoo WHERE idStyle = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_estilo(self,idStyle, Nombre, descripcion):
        cur = self.cnn.cursor()
        sql='''UPDATE Style_Tattoo SET Nombre='{}', Descripcion='{}'
            WHERE idStyle={}'''.format(Nombre, descripcion, idStyle)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   