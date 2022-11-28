"""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import mysql.connector  

class Data_logging():

    def __init__(self):
        self.conecction  = mysql.connector(
            host='localhost',
            database='TattooWorld',
            user='root',
            password='mininaluz19'
        )

    def insert_data(self, Nombre, Apellido_M, Apellido_P, idStyle, idArea):
        cur = self.conecction.cursor()
        sql='''INSERT INTO Tatuadores (Nombre. Apellido_M, Apellido_P, idStyle, idArea)
                VALUES ('{}'. '{}', '{}', '{}', '{}')'''.format(Nombre, Apellido_M, Apellido_P, idStyle, idArea)
        cur.execute(sql)
        self.conecction.commit()
        cur.close()

    def show_data(self):
        cursor = self.conecction.cursor()
        sql="SELECT * FROM Tatuadores"
        cursor.execute(sql)
        registration = cursor.fetchall()
        return registration

    def search_data(self, tattooist_name):
        cur = self.conecction.cursor()
        sql = "SELECT * FROM Tatuadores WHERE Nombre = {}".format(tattooist_name)
        cur.execute(sql)
        any_name = cur.fetchall()
        cur.close()
        return any_name

    def delete_data(self, name):
        cur = self.conecction.cursor()
        sql = '''DELETE FROM Tatuadores WHERE Nombre = {}'''.format(name)
        cur.execute(sql)
        self.conecction.commit()
        cur.close()

    def update_data(self,idTatuadores, Nombre, Apellido_M, Apellido_P, idStyle, idArea):
        cur = self.conecction.cursor()
        sql = '''UPDATE Tatuadores SET NOMBRE = '{}', APELLIDO_M = '{}', APELLIDO_P = '{}', IDSTYLE = '{}' IDAREA = '{}' 
            WHERE idTatuadores = '{}' '''.format(Nombre, Apellido_M, Apellido_P, idStyle, idArea, idTatuadores)
        cur.execute(sql)
        updated = cur.rowcount 
        self.conecction.commit()
        cur.close()
        return updated