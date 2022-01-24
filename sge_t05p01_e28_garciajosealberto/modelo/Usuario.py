from datetime import datetime

class Usuario:
    def _init_(self, dni, contrasegna, ultAcceso):
        self.dni=dni
        self.contrasegna=contrasegna
        self.ultAcceso=datetime.timestamp
        self.esAdmdor=False

    def hacerAdmdor(self):
        self.esAdmdor=True

    def cambiarContrasegna(self, contrasegna):
        self.contrasegna=contrasegna

    


