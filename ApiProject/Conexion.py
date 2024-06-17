import mysql.connector

class Conexion:

    def __init__(self, host, port , user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(

                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conexion Establecida")
        except mysql.connector.Error as err:
            print("Error al conectar la base de datos", err)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexion Cerrada")

    def execute_query(self, query, params= None):
        cursor = self.connection.cursor(buffered = True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query ejecutado exitosamente")
            if query.lower().startwith('select'):
                result = cursor.fetchall()
                return  result
        except mysql.connector.Error as err:
            print("Error al ejecutar el query" , err)
            return None
        finally:
            cursor.close()