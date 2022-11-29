"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import mysql.connector

class Receptionistconeection:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="mininaluz19", database="TattooWorld")
 
    def __str__(self):
        datos=self.consulta_recp()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_recp(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Recepcionista")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_recp(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM Recepcionista WHERE idRecepcionista = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_recp(self,Nombre, apellidoM, apellidoP, Celular, Area):
        cur = self.cnn.cursor()
        sql='''INSERT INTO Recepcionista (Nombre, Apellido_M, Apellido_P, Celular, idArea) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Nombre, apellidoM, apellidoP, Celular, Area)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_recp(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Recepcionista WHERE idRecepcionista = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_recp(self,idRecepcionista, Nombre, apellidoM, apellidoP, Celular, idArea):
        cur = self.cnn.cursor()
        sql='''UPDATE Style_Tattoo SET Nombre='{}', Apellido_M = '{}', Apellido_P = '{}',
            Celular = '{}', idArea = '{}'
            WHERE idRecepcionista={}'''.format(Nombre, apellidoM, apellidoP, Celular, idArea, idRecepcionista)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  