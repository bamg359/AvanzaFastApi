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


    def insertar_estudiante(self, db):
        query = "insert into estudiante(id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiante, correo, telefono, contrasena)values(%s,%s,%s,%s,%s;%s,%s)"
        values = (self.id_estudiante, self.tipo_documento, self.nombre_estudiante, self.Apellido_estudiante, self.correo, self.telefono, self.contrasena)
        db.connect()

    ##Aqui van los getters and setters
    @app.post('/registrar_est/{id_estudiante, tipo_documento, nombre_estudiante, apellido_estudiante, correo, telefono, contrasena}' , tags=["Registrar Estudiante"])
    def registrarEstudiante(self, id_estudiante: int = Body(), tipo_documento: str= Body(), nombre_estudiante: str = Body(), apellido_estudiante: str = Body(), correo: str = Body(), telefono: str = Body(), contrasena: str = Body() ):
        self.insertar_estudiante(db)







