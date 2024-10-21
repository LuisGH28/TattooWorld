""" 
__author__ = "Luis Gonzalez, Sandra Fragoso"
__version__ = "0.1"
__maintainer__ = "Luis Gonzalez"
__email__ = "luisgnzhdz@gmail.com"
__status__ = "Production"
"""

import mysql.connector


class Connection:

    def __init__(self):
        try:
            self.cnn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                passwd="mininaluz19", 
                database="TattooWorld"
            )
            if self.cnn.is_connected():
                print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def __str__(self):
        datos = self.consulta_datos()        
        aux = ""
        for row in datos:
            aux += str(row) + "\n"
        return aux
        
    def consulta_datos(self):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT * FROM Tatuadores")
            datos = cur.fetchall()
            cur.close()
            return datos
        except Error as e:
            print(f"Error al realizar consulta: {e}")
    
    def buscar_tatuador(self, Id):
        try:
            cur = self.cnn.cursor()
            sql = "SELECT * FROM Tatuadores WHERE idTatuadores = {}".format(Id)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()
            return datos
        except Error as e:
            print(f"Error al buscar tatuador: {e}")

    def inserta_tatuador(self, Nombre, apellidoM, apellidoP, idEstilo, idArea):
        try:
            cur = self.cnn.cursor()
            sql = '''INSERT INTO Tatuadores (Nombre, Apellido_M, Apellido_P, idStyle, idArea) 
                    VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Nombre, apellidoM, apellidoP, idEstilo, idArea)
            cur.execute(sql)
            n = cur.rowcount
            self.cnn.commit()
            cur.close()
            return n
        except Error as e:
            print(f"Error al insertar tatuador: {e}")

    def elimina_tatuador(self, Id):
        try:
            cur = self.cnn.cursor()
            sql = "DELETE FROM Tatuadores WHERE idTatuadores = {}".format(Id)
            cur.execute(sql)
            n = cur.rowcount
            self.cnn.commit()
            cur.close()
            return n
        except Error as e:
            print(f"Error al eliminar tatuador: {e}")

    def modifica_tatuador(self, idTatuador, Nombre, apellidoM, apellidoP, idEstilo, idArea):
        try:
            cur = self.cnn.cursor()
            sql = '''UPDATE Tatuadores SET Nombre='{}', Apellido_M='{}', Apellido_P='{}', 
                     idStyle='{}', idArea='{}' WHERE idTatuadores={}'''.format(Nombre, apellidoM, apellidoP, idEstilo, idArea, idTatuador)
            cur.execute(sql)
            n = cur.rowcount
            self.cnn.commit()
            cur.close()
            return n
        except Error as e:
            print(f"Error al modificar tatuador: {e}")

