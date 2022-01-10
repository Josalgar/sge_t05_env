#10. Hacer un programa que lea caracteres desde teclado hasta que lea 10 veces la letra 'a'. Cuando aparezca una 'a' debe mostrar un mensaje indicando 
# el número de aes que faltan para que el programa termine. Cuando lea las 10 letras 'a' el programa terminará.

contador=0
pendiente=0

while contador<10 :
    letra=input("Indica una relacion de caracteres: ")
    

    if letra.lower()=="a" :
        contador+=1
        pendiente=10-contador
        print(f"Quedan por registrar {pendiente}")
else :
    print("Han aparecido 10 letras A")
    
        