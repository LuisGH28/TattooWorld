import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect (host='localhost',
                                                database = 'FashionTec',
                                                user = 'root',
                                                password = 'mininayluz19')
        