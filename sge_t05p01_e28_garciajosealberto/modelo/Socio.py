from datetime import datetime


class Socio:
    def __init__(self,_init_Usuario ,usuarioApp, nombre, apellidos,direccion, tfno,mail):
        self.usuarioApp=usuarioApp
        self.nombre=nombre
        self.apellidos=apellidos
        self.direccion=direccion
        self.tfno=tfno
        self.mail=mail
        self.bicicletas=False
        self.conyuge=False
        self.padre=False
        self.hijo=False
        self.cuota=None
        self.fechaAlta=

    def tieneConyuge(self,conyuge):
        self.conyuge=False

    def tieneHijos(self,padre):
        self.padre=False

    def esHijo(self,hijo):
        self.hijo=False

    def calcularCuota():

    
    
        