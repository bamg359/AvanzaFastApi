from fastapi import FastAPI, Body

from fastapi.responses import  HTMLResponse

from Conexion import Conexion

db = Conexion(host= 'localhost', port = 3306, user = 'root', password= "", database= 'api_project')
db.connect()

app = FastAPI(
    title = "Api_Project",
    description= "Proyecto final Avanza",
    version = "0.0.1"
)

@app.get('/')
def read_root():
    return {"Hello":"world"}


class Estudiante:

    id_estudiante = None
    tipo_documento = None
    nombre_estudiante = None
    Apellido_estudiante = None
    correo = None
    telefono = None
    contrasena = None

    def __init__(self, id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiente, correo, telefono, contrasena):
        self.id_estudiante = id_estudiante
        self.tipo_documento = tipo_documento
        self.nombre_estudiante = nombre_estudiante
        self.Apellido_estudiante = apellido_estudiente
        self.correo = correo
        self.telefono = telefono
        self.contrasena = contrasena




    ##Aqui van los getters and setters
    @app.post('/registrar_est/{id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiante, correo, telefono, contrasena}' , tags=["Registrar Estudiante"])
    def registrarEstudiante(id_estudiante: int = Body(), tipo_documento: str= Body(), nombre_estudiante: str = Body(), apellido_estudiante: str = Body(), correo: str = Body(), telefono: str = Body(), contrasena: str = Body() ):

        query = "insert into estudiante(id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiante, correo, telefono, contrasena)values(%s,%s,%s,%s,%s,%s,%s)"
        values = (
            id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiante, correo,
            telefono, contrasena)
        db.execute_query(query, values)

    @staticmethod
    def from_row(row):
        return Estudiante(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    @staticmethod
    @app.get('/get_estudiante/{id_estudiante}', tags=["Obtener Estudiantes"])
    def consultar_estudiente(id_estudiante: int):

        query = "SELECT * FROM estudiante WHERE id_estudiante = %s"
        result = db.execute_query(query , (id_estudiante,))
        if result:
            return Estudiante.from_row(result[0])
        else:
            print("Estudiante no encontrado")
            return None


    @staticmethod
    @app.get('/get_estudiantes', tags = ["Obtener estudiantes"])
    def consultar_estudiantes():
        query = "SELECT * FROM estudiante"
        result = db.execute_query(query)
        if result:
         listado_estudiantes = []
         for row in result:
             estudiante = Estudiante.from_row(row)
             listado_estudiantes.append(estudiante)
         return listado_estudiantes
        else:
            return []


    @staticmethod
    @app.delete('/delete_estudiante/{id_estudiante}', tags=["Eliminar_estudiante"])
    def eliminar_estudiante(id_estudiante: int):
        query = "DELETE FROM estudiante WHERE id_estudiante = %s"
        db.execute_query(query, (id_estudiante,))











