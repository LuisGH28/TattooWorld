"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import mysql.connector

class Areaconeection:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="mininaluz19", database="TattooWorld")
 
    def __str__(self):
        datos=self.consulta_area()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_area(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Area")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_area(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM Area WHERE idArea = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_area(self,Nombre):
        cur = self.cnn.cursor()
        sql='''INSERT INTO Area (Nombre) 
        VALUES('{}')'''.format(Nombre)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_area(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Area WHERE idArea = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_area(self,idArea, Nombre):
        cur = self.cnn.cursor()
        sql='''UPDATE Area SET Nombre='{}'
            WHERE idArea={}'''.format(Nombre, idArea)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   