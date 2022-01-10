#    22. Crear un script que pida al usuario valores alfanuméricos para una lista (por ejemplo fabricantes de dispositivos móviles) 
# hasta que el usuario escriba la palabra salir.

#Finalmente el script determina si hay elementos duplicados o no en dicha lista y después si la lista está ordenada o no alfabéticamente.

import collections

def hayDuplicados (lista):
    
    if len(lista) != len(set(lista)):
        print("Hay valores duplicados en la lista.")
    else:
        print("No hay valores duplicados en la lista.")
        
def estaOrdenadaAlfabeticamente(lista):
    listaOrdenada=lista[:]
    listaOrdenada.sort()
    if len(lista)!=len(listaOrdenada):
        print("La lista no está ordenada alfabeticamente.")
        
    else:
        print("La lista está ordenada alfabéticamente.")
        
    

listaValores=[]
valores=0
while valores!="salir" :
    
    valores=input("Indica nombres de marcas de fabricantes de telefonía móvil. Escribe salir para finalizar. \n") 
    
    if valores!="salir":
        listaValores.append(valores)
    

print(listaValores)

hayDuplicados(listaValores)
estaOrdenadaAlfabeticamente(listaValores)
