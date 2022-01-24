
from datetime import datetime
class Movimiento:
    fechaMov=None
    cantidad=None
    ingreso=None
    concepto=None
    
def _init_(self,cantidad,ingreso,concepto):
    self.cantidad=cantidad
    self.ingreso=ingreso
    self.concepto=concepto
    self.fechaMov=datetime.today().strptime('%d/%m/%y')
    
def esIngreso(self):
    self.ingreso=True


