<<<<<<< HEAD
#    19. Realizar un programa en Python que calcule el factorial impar de un número entero. 

#Nota. El factorial impar de un número n es el producto de todos los números naturales impares desde el 1 hasta n o n-1, 
# dependiendo de si n es par o impar. Ejemplo:
#5! = 5 x 3 x 1 = 15

numero=int(input("Facilita un número:\n"))
print()

factorial=1

if (numero==0 or numero==1) :
    print("El factorial de 0 es 1.")
    
elif numero<0:
    print("El factorial de un número negativo no se puede calcular. ")
else:
    
    for i in range(1,numero+1,2):
        factorial*=i
    print(f"El factorial impar, calculado de forma iterativa, de {numero} es {factorial}.")
       
        
=======
#    19. Realizar un programa en Python que calcule el factorial impar de un número entero. 

#Nota. El factorial impar de un número n es el producto de todos los números naturales impares desde el 1 hasta n o n-1, 
# dependiendo de si n es par o impar. Ejemplo:
#5! = 5 x 3 x 1 = 15

numero=int(input("Facilita un número:\n"))
print()

factorial=1

if (numero==0 or numero==1) :
    print("El factorial de 0 es 1.")
    
elif numero<0:
    print("El factorial de un número negativo no se puede calcular. ")
else:
    
    for i in range(1,numero+1,2):
        factorial*=i
    print(f"El factorial impar, calculado de forma iterativa, de {numero} es {factorial}.")
       
        
>>>>>>> 1cafc75f29b86e3c8ed0daa698f010cede8c18d9
        