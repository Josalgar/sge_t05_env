from datetime import datetime

class Fecha(object):
    
   dia=None
   mes=None
   agno=None
   
   def _init_(self,dia=0, mes=0, agno=0):
      self.dia=dia
      self.mes=mes
      self.agno=agno


   def fActual(self,dia,mes,agno):
      self.dia=dia.now("%d")
      self.mes=mes.now("%m")
      self.agno=agno.now("%y")
      return self(dia,mes,agno)
   
   fechaAct=Fecha().fActual()