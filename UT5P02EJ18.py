# 18. Hacer un script que calcule el factorial de un número entero leído desde teclado. Primero de forma iterativa, 
# luego de forma recursiva.

#Haz dos funciones.

#Recuerda: El factorial de un número n es el producto de todos los números naturales desde 1 hasta n inclusive. 
# Así, factorial de 5 (5!) es: 5! = 5 x 4 x 3 x 2 x 1 = 120.

#Contempla qué debe ocurrir si el número es 0 o 1 y qué debe ocurrir si el número es negativo.

def factorialRecursivo(numero):
    
    if numero<=1:
        return 1
    return numero*factorialRecursivo(numero-1)


if __name__ == "__main__":

    numero=int(input("Facilite un número.\n"))
    factorial=1
    
#Factorial calculado de forma iterativa

if numero==0:
    print("El factorial de 0 es 1")
elif numero==1:
    print("El factorial de 1 es 1")
elif numero<0:
    print("El factorial de un número negativo no se puede calcular ")
else:
    for i in range(1,numero+1) :
        factorial*=i
    print(f"El factorial, calculado de forma iterativa, de {numero} es {factorial}") 
    print(f"El factorial, calculado de forma recursiva, da {factorialRecursivo(numero)}")

