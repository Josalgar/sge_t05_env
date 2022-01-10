#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

importe=float(input("Indica la cantidad que quieres invertir: "))
interes=float(input("Indica el porcentaje de interés: "))
agnos=float(input("Indica el número de años de la inversión: "))

ganancia=importe*agnos*interes/100

print(f"El capital que ganaremos será de {ganancia} Euros")

