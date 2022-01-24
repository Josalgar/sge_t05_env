<<<<<<< HEAD
#Escribir un programa que tome dos tiempos introducidos por el usuario en el formato (horas:minutos:segundos) y lo convierta en segundos. 
# El programa posteriormente calculará la diferencia en segundos entre los dos tiempos introducidos por el usuario y la mostrará por 
# pantalla.

from datetime import time
from datetime import datetime

def calcularSeg(fecha):
    fechaF=fecha.split(":")
    intFechaF=[int(i) for i in fechaF]
    
   
    if intFechaF[0]<0 or intFechaF[0]>23 :
        print("La cantidad de horas es incorrecto")
    elif intFechaF[1]<0 or intFechaF[1]>60 :
        print("La cantidad de minutos es incorrecto")
    if intFechaF[2]<0 or intFechaF[2]>60 :
        print("La cantidad de segundos es incorrecto")
    else:
        segundosTotales=intFechaF[0]*3600+intFechaF[1]*60+intFechaF[2]
        return segundosTotales

h1=input("Dame una hora en formato hora:minutos:segundos - ")
h2=input("Dame una hora en formato hora:minutos:segundos - ")

segH1=calcularSeg(h1)
segH2=calcularSeg(h2)

DifSeg=int(segH1-segH2)
=======
#Escribir un programa que tome dos tiempos introducidos por el usuario en el formato (horas:minutos:segundos) y lo convierta en segundos. 
# El programa posteriormente calculará la diferencia en segundos entre los dos tiempos introducidos por el usuario y la mostrará por 
# pantalla.

from datetime import time
from datetime import datetime

def calcularSeg(fecha):
    fechaF=fecha.split(":")
    intFechaF=[int(i) for i in fechaF]
    
   
    if intFechaF[0]<0 or intFechaF[0]>23 :
        print("La cantidad de horas es incorrecto")
    elif intFechaF[1]<0 or intFechaF[1]>60 :
        print("La cantidad de minutos es incorrecto")
    if intFechaF[2]<0 or intFechaF[2]>60 :
        print("La cantidad de segundos es incorrecto")
    else:
        segundosTotales=intFechaF[0]*3600+intFechaF[1]*60+intFechaF[2]
        return segundosTotales

h1=input("Dame una hora en formato hora:minutos:segundos - ")
h2=input("Dame una hora en formato hora:minutos:segundos - ")

segH1=calcularSeg(h1)
segH2=calcularSeg(h2)

DifSeg=int(segH1-segH2)
>>>>>>> 1cafc75f29b86e3c8ed0daa698f010cede8c18d9
print("La diferencia de segundos entre la hora 1 y la hora 2 es: ",DifSeg)