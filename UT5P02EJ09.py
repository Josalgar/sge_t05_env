#ej.9
#9. Realizar un programa que pida al usuario que vaya introduciendo caracteres por teclado, de forma que éste vaya contando el número de vocales, 
# el número de consonantes y el número de otros signos introducidos hasta que el usuario teclee el carácter blanco (‘ ‘) que indicará que el usuario no desea 
# introducir más caracteres. Finalmente, mostrará por pantalla el número de vocales, el número de consonantes y el número de otros signos introducidos, así 
# como el número total de caracteres tecleados por el usuario (sin contar el espacio en blanco final). Hazlo sin hacer uso de expresiones regulares.

contadorLetras=0
contadorVocales=0
contadorConsonantes=0
contadorSignos=0
letra=""
vocales=(["a","e","i","o","u"])
consonantes=(["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"])

while letra !=" " :
        
    letra=input("Indica una serie de letras por teclado. Cuando quieras acabar pincha espacio. ")
        
    if letra.lower() in vocales :
        contadorVocales+=1
        contadorLetras+=1
    elif letra.lower() in consonantes :
        contadorConsonantes+=1
        contadorLetras+=1
    elif letra.lower() in " ":
        print("Has finalizado la secuencia")
        break
    else :
        contadorSignos+=1
        contadorLetras+=1
   
    
print(f"El número de vocales introducidas es {contadorVocales}")
print(f"El número de consonantes introducidas es {contadorConsonantes}")
print(f"El número de signos introducidas es {contadorSignos}")
print(f"El número de letras introducidas es {contadorLetras}")
