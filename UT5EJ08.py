
minutosTotales=float(input("Indica un número de minutos"))

if minutosTotales>60:
    horas=minutosTotales//60
    minutos=minutosTotales-horas*60
    print(f"El número total de minutos son {horas} horas y {minutos} minutos.")
    
else:
    print(f"El número total de minutos es {minutosTotales}")