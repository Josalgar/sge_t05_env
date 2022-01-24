#    20. Crear una calculadora que realice las siguientes operaciones: sumar, restar, multiplicar, dividir y calcular potencias. 
# Habrá un menú que se mostrará iterativamente hasta que el usuario indique que quiere salir.

# Cada operación se hará a través de una función.

#Además, el programa tendrá control de errores (try-catch):
#    • Solo se puede operar con números (enteros o reales). Si se introduce algo que no es un número, se detecta el error, 
# se avisa y se vuelve a pedir un valor válido.
#    • No se puede dividir por cero. Si detecta que va a ocurrir eso, se da un aviso y se vuelve a pedir un valor válido.
#    • Cualquier otro error. Si ocurre un error inesperado, se da un aviso y se vuelve a pedir el valor.

from locale import format_string


def menu(opcion):
    match opcion:
        case 1:
            
            
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            potencia()
        case 6:
            print("Ha seleccionado salir.")
            print("El programa ha terminado")
        #    exit()
        case _:
            print("La opción indicada no es válida, por favor, indique una opción correcta.")
        

def pedirNum():
    try:
        numero1 = int(input("Indique un valor entero para el número 1: "))
        
                        
    except ValueError:
        print ("El valor asignado no es válido, por favor, asigne otro.")

    
    try:
            
        numero2 = int(input("Indique un valor entero para el número 2: "))
        
            
    except ValueError:
        print ("El valor asignado no es válido, por favor, asigne otro.")
        
    
def sumar():
    pedirNum()
    print("La suma de ambos números es ",numero1+numero2)
        

    

def restar(numero1,numero2):
    while True:
        try:
            numero1 = int(input("Indique un valor entero para el minuendo: "))
                        
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
        
    while True:    
        try:
            
            numero2 = int(input("Indique un valor entero para el sustraendo: "))
            
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
        
    print("La resta de ambos números es "+str(numero1-numero2))
        
def multiplicar():
    while True:
        try:
            numero1 = int(input("Indique un valor entero para el número 1: "))
                        
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
        
    while True:    
        try:
            
            numero2 = int(input("Indique un valor entero para el número 2: "))
            
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
    print("La resultado de multiplicar ambos números es "+str(numero1*numero2))
    
def dividir():
    
    while True:
        try:
            dividendo=int(input("Indique un valor para el dividendo: "))
                        
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
        
    while True:    
        try:
            
            divisor=int(input("Indique un valor para el divisor: "))
            
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
            
        except ZeroDivisionError:
            print("No se puede dividir entre 0, facilite otro número.")
        
            
        else:
            break
    
    print("La división de ambos números es "+str(dividendo/divisor))

    
def potencia():
    while True:
        try:
            base = int(input("Indique un valor entero para la base: "))
                        
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
        
    while True:    
        try:
            
            exponente = int(input("Indique un valor entero para el exponente: "))
            
        except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            continue
        else:
            break
    print("La potencia es "+str(base**exponente))
        
opcion=None
while opcion!=6:
    print("Indique el número de la operación que quiere realizar:")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Calcular potencia")
    print("6.- Salir")
    print()
    
    try:
            opcion=int(input())
            menu(opcion)
    except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")
            
try:
            numero1 = int(input("Indique un valor entero para el número 1: "))
                        
except ValueError:
            print ("El valor asignado no es válido, por favor, asigne otro.")

    
try:
            
        numero2 = int(input("Indique un valor entero para el número 2: "))
            
except ValueError:
        print ("El valor asignado no es válido, por favor, asigne otro.")
else:
    print("El programa ha finalizado.")
