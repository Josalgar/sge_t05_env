#Realizar un programa que determine si el número introducido por el usuario es primo o no.

numero=int(input("Indica un número para saber si es primo: "))
print()

if numero<1 :
    print("El número indicado deber ser mayor que 0")
elif numero==1 :
    print("El número 1 no es primo")
else:
    
    for i in range(2,numero-1):
        if numero%i==0:
            print("El número no es primo")
            break
        
    print("El número dado es primo")
          
            