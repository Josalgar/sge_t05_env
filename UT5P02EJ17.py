#17. Realizar un programa en Python que calcule el valor obtenido al aplicar la ecuación:
#Para ello el programa pedirá el valor n, y después calculará la ecuación. El programa mostrará finalmente por 
# pantalla el resultado obtenido. El valor de n debe ser un entero mayor o igual que 1.

n=int(input("Facilita el valor n para calcular el sumatorio, de 1 a n, de ((n+1)**2)/(i+1).\n"))
i=1
resultado=0
if (n>=1):
    while i<=n:
        operacion=((n+1)**2)/(i+1)
        resultado+=operacion
        i+=1
    else:
        print(f"El resultado del sumatorio es {resultado}.")
else:
    print("El número facilitado no puede ser inferior a 1.")