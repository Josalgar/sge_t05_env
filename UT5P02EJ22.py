<<<<<<< HEAD
#    22. Crear un script que pida al usuario valores alfanuméricos para una lista (por ejemplo fabricantes de dispositivos móviles) 
# hasta que el usuario escriba la palabra salir.

#Finalmente el script determina si hay elementos duplicados o no en dicha lista y después si la lista está ordenada o no alfabéticamente.

import collections
from locale import format_string
from pickle import TRUE

def hayDuplicados (lista):
    
    if len(lista) != len(set(lista)):
        print("Hay valores duplicados en la lista.")
    else:
        print("No hay valores duplicados en la lista.")
        
def estaOrdenadaAlfabeticamente(lista):
    #Corrección de como lo había planteado
    '''listaOrdenada=lista[:]
    listaOrdenada.sort()
    if lista!=listaOrdenada:
        print("La lista no está ordenada alfabeticamente.")
        
    else:
        print("La lista está ordenada alfabéticamente.")'''
    
    #Planteamiento según tus indicaciones
    for i in range(len(lista)-1):
        if (lista[i]>lista[i+1]):
            return False
    
    return True
            
        
    

listaValores=[]
valores=0
while valores!="salir" :
    
    valores=input("Indica nombres de marcas de fabricantes de telefonía móvil. Escribe salir para finalizar. \n") 
    
    if valores!="salir":
        listaValores.append(valores)
    

print(listaValores)

hayDuplicados(listaValores)
if estaOrdenadaAlfabeticamente(listaValores)==True:
    print("La lista está ordenada alfabéticamente")
else:
    print("La lista NO está ordenada alfabéticamente")
=======
#    22. Crear un script que pida al usuario valores alfanuméricos para una lista (por ejemplo fabricantes de dispositivos móviles) 
# hasta que el usuario escriba la palabra salir.

#Finalmente el script determina si hay elementos duplicados o no en dicha lista y después si la lista está ordenada o no alfabéticamente.

import collections
from locale import format_string
from pickle import TRUE

def hayDuplicados (lista):
    
    if len(lista) != len(set(lista)):
        print("Hay valores duplicados en la lista.")
    else:
        print("No hay valores duplicados en la lista.")
        
def estaOrdenadaAlfabeticamente(lista):
    #Corrección de como lo había planteado
    '''listaOrdenada=lista[:]
    listaOrdenada.sort()
    if lista!=listaOrdenada:
        print("La lista no está ordenada alfabeticamente.")
        
    else:
        print("La lista está ordenada alfabéticamente.")'''
    
    #Planteamiento según tus indicaciones
    for i in range(len(lista)-1):
        if (lista[i]>lista[i+1]):
            return False
    
    return True
            
        
    

listaValores=[]
valores=0
while valores!="salir" :
    
    valores=input("Indica nombres de marcas de fabricantes de telefonía móvil. Escribe salir para finalizar. \n") 
    
    if valores!="salir":
        listaValores.append(valores)
    

print(listaValores)

hayDuplicados(listaValores)
if estaOrdenadaAlfabeticamente(listaValores)==True:
    print("La lista está ordenada alfabéticamente")
else:
    print("La lista NO está ordenada alfabéticamente")
>>>>>>> 1cafc75f29b86e3c8ed0daa698f010cede8c18d9
