import os
from datetime import datetime
class Fecha:
    
   dia=None
   mes=None
   agno=None
   
   def _init_(self,dia=0, mes=0, agno=0):
      self.dia=dia
      self.mes=mes
      self.agno=agno


   def fActual(self):
      fechaActual=datetime.now()
      return self(fechaActual.day,fechaActual.month,fechaActual.year)
   
   fechaAct=Fecha().fActual()