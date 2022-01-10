#Realizar un programa que calcule el valor medio de una secuencia de números enteros introducidos por teclado hasta que 
# se introduzca un valor negativo, que no será tenido en cuenta para calcular la media. 
# El programa mostrará finalmente por pantalla el valor medio obtenido.

contador=0
total=0


numero=int(input("Indica una relación de números y te indicaremos la media. Facilita un número negativo para salir. "))

if numero>=0 :
    contador+=1
    total+=numero
    
    while numero >= 0 :
        numero=int(input("Indica una relación de números y te indicaremos la media. Facilita un número negativo para salir. "))
        if numero>=0 :
            contador+=1
            total+=numero
    else:
        media=(total/contador)
        print(f"La media de los números dados sería {media}")