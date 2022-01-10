#Crear un programa que dado un año introducido por el usuario determine si es bisiesto o no.

agno=float(input("Indícame un año: "))

if agno%4==0 and agno%100!=0 :
    print("El año indicado es bisiesto")
elif agno%100==0 and agno%400==0 :
    print("El año indicado es bisiesto")
else :
    print("El año indicado NO es bisiesto")   