<<<<<<< HEAD
#    21. Crea un script que pida al usuario un número y luego pida valores para una lista (lista1) hasta que llegue a un 
# número de valores igual al número introducido  (incluido). Usa range(). Después hará lo mismo para una segunda lista (lista2). 
# Después trata de hacer las siguientes operaciones y muestra por pantalla el resultado (haz cada operación con un try/catch):
 #   • lista3=lista1*2
 #   • lista4=lista1+3
 #   • lista5=lista1*lista2
 #   • lista6=lista1+lista2
  #  • lista7 ← será una copia de la lista 1 de forma directa.

#Analiza qué ocurre.

#Finalmente, crea una lista (lista8) con los valores comunes a ambas listas. Si no hay valores comunes, la lista estará vacía. 
# Muestra el tamaño de esta lista.


#DEJO CÓDIGO RESIDUAL CON EL QUE TRATÉ DE IMPLEMENTAR CIERTAS FUNCIONES PERO QUE NO FUNCIONÓ CORRECTAMENTE


from itertools import zip_longest


def dobleLista(lista):
      lEspejo=[]
      
      for i in lista:
            lEspejo.append(i*2)
            
      # Traté de realizarlo así pero no funcionó
      #for i in range(0, len(lEspejo)):
            #lista[i]=lista[i]*2
            #lEspejo[i]=lEspejo[i]*2
      return lEspejo
def suma3Lista(lista):
      lEspejo=[]
      for i in lista:
            lEspejo.append(i+3)
      return lEspejo

def productoListas(list1,list2):
      #Tampoco función así
      '''if len(list1)>len(list2):
        for i in range(0, len(list1)): 
          return list1[i]*list2[i] 
      else:
        for i in range(0, len(list2)): 
          return list1[i]*list2[i]'''  
          
      lEspejo=[] 
      if len(list1)==len(list2):
            lEspejo = [i*x for i,x in zip(list1, list2)]
            return lEspejo       
      else:   
            lEspejo=[i*x for i,x in zip_longest(list1, list2, fillvalue=0)] 
            
            return lEspejo

def sumaListas(list1,list2):
      lEspejo=[]  
      #Ni así  
      '''if len(list1)>=len(list2):
            for i in list1: 
                  lEspejo.append(list1[i]+list2[i])
            return lEspejo       
      else:
            for i in list2: 
                  lEspejo.append(list1[i]+list2[i])  
            return lEspejo'''
      if len(list1)==len(list2):
            lEspejo = [i+x for i,x in zip(list1, list2)]
            #for i in list1: 
             #     for x in list2:
              #          lEspejo.append(i+x)
            return lEspejo       
      else:   
            lEspejo=[i+x for i,x in zip_longest(list1, list2, fillvalue=0)] 
            #lEspejo=map(sum, zip_longest(list1, list2, fillvalue=0))
            return lEspejo
      '''if len(list1)>len(list2):
            for i in range(0, len(list1)): 
                  lEspejo[i]=list1[i]+list2[i] 
            return lEspejo       
      else:
            for i in range(0, len(list2)): 
                  lEspejo[i]= list1[i]+list2[i]   
            return lEspejo'''

def encontrarDuplicados(list1,list2):
      lDuplicados=[]
      for i in list1:
            for x in list2:
                  if i==x:
                        lDuplicados.append(i)
                        
      lDuplicados=list(tuple(lDuplicados))
      return lDuplicados
      

numero1=int(input("Facilite la longitud de la lista 1 que va a crear"))
lista1=[]
for x in range(numero1):
    num1=int(input("Dame números para la lista: "))
    #lista1.insert(x,num1)
    lista1.append(num1)

print("Lista 1: ",lista1,)

numero2=int(input("Facilite la longitud de la lista 2 que va a crear"))
lista2=[]
for x in range(numero2):
    num2=int(input("Dame números para la lista: "))
    lista2.append(num2)

print("Lista 2: ",lista2,)

print()


lista3=[]
lista4 =[]
lista5 =[]
lista6 =[]
lista7 =[]
lista8 =[]
lista3=dobleLista(lista1)
lista4 =suma3Lista(lista1)
lista5 =productoListas(lista1,lista2)
lista6 =sumaListas(lista1,lista2)
lista7=lista1
lista8=encontrarDuplicados(lista1,lista2)
print("Lista 3: ",lista3,)
print("Lista 4: ",lista4,)
print("Lista 5: ",lista5,)
print("Lista 6: ",lista6,)
print("Lista 7:",lista7,)

print("Creamos la Lista 8 con Los valores comunes entre las dos listas introducidas manualmente, siendo: ",lista8,)
=======
#    21. Crea un script que pida al usuario un número y luego pida valores para una lista (lista1) hasta que llegue a un 
# número de valores igual al número introducido  (incluido). Usa range(). Después hará lo mismo para una segunda lista (lista2). 
# Después trata de hacer las siguientes operaciones y muestra por pantalla el resultado (haz cada operación con un try/catch):
 #   • lista3=lista1*2
 #   • lista4=lista1+3
 #   • lista5=lista1*lista2
 #   • lista6=lista1+lista2
  #  • lista7 ← será una copia de la lista 1 de forma directa.

#Analiza qué ocurre.

#Finalmente, crea una lista (lista8) con los valores comunes a ambas listas. Si no hay valores comunes, la lista estará vacía. 
# Muestra el tamaño de esta lista.


#DEJO CÓDIGO RESIDUAL CON EL QUE TRATÉ DE IMPLEMENTAR CIERTAS FUNCIONES PERO QUE NO FUNCIONÓ CORRECTAMENTE


from itertools import zip_longest


def dobleLista(lista):
      lEspejo=[]
      
      for i in lista:
            lEspejo.append(i*2)
            
      # Traté de realizarlo así pero no funcionó
      #for i in range(0, len(lEspejo)):
            #lista[i]=lista[i]*2
            #lEspejo[i]=lEspejo[i]*2
      return lEspejo
def suma3Lista(lista):
      lEspejo=[]
      for i in lista:
            lEspejo.append(i+3)
      return lEspejo

def productoListas(list1,list2):
      #Tampoco función así
      '''if len(list1)>len(list2):
        for i in range(0, len(list1)): 
          return list1[i]*list2[i] 
      else:
        for i in range(0, len(list2)): 
          return list1[i]*list2[i]'''  
          
      lEspejo=[] 
      if len(list1)==len(list2):
            lEspejo = [i*x for i,x in zip(list1, list2)]
            return lEspejo       
      else:   
            lEspejo=[i*x for i,x in zip_longest(list1, list2, fillvalue=0)] 
            
            return lEspejo

def sumaListas(list1,list2):
      lEspejo=[]  
      #Ni así  
      '''if len(list1)>=len(list2):
            for i in list1: 
                  lEspejo.append(list1[i]+list2[i])
            return lEspejo       
      else:
            for i in list2: 
                  lEspejo.append(list1[i]+list2[i])  
            return lEspejo'''
      if len(list1)==len(list2):
            lEspejo = [i+x for i,x in zip(list1, list2)]
            #for i in list1: 
             #     for x in list2:
              #          lEspejo.append(i+x)
            return lEspejo       
      else:   
            lEspejo=[i+x for i,x in zip_longest(list1, list2, fillvalue=0)] 
            #lEspejo=map(sum, zip_longest(list1, list2, fillvalue=0))
            return lEspejo
      '''if len(list1)>len(list2):
            for i in range(0, len(list1)): 
                  lEspejo[i]=list1[i]+list2[i] 
            return lEspejo       
      else:
            for i in range(0, len(list2)): 
                  lEspejo[i]= list1[i]+list2[i]   
            return lEspejo'''

def encontrarDuplicados(list1,list2):
      lDuplicados=[]
      for i in list1:
            for x in list2:
                  if i==x:
                        lDuplicados.append(i)
                        
      lDuplicados=list(tuple(lDuplicados))
      return lDuplicados
      

numero1=int(input("Facilite la longitud de la lista 1 que va a crear"))
lista1=[]
for x in range(numero1):
    num1=int(input("Dame números para la lista: "))
    #lista1.insert(x,num1)
    lista1.append(num1)

print("Lista 1: ",lista1,)

numero2=int(input("Facilite la longitud de la lista 2 que va a crear"))
lista2=[]
for x in range(numero2):
    num2=int(input("Dame números para la lista: "))
    lista2.append(num2)

print("Lista 2: ",lista2,)

print()


lista3=[]
lista4 =[]
lista5 =[]
lista6 =[]
lista7 =[]
lista8 =[]
lista3=dobleLista(lista1)
lista4 =suma3Lista(lista1)
lista5 =productoListas(lista1,lista2)
lista6 =sumaListas(lista1,lista2)
lista7=lista1
lista8=encontrarDuplicados(lista1,lista2)
print("Lista 3: ",lista3,)
print("Lista 4: ",lista4,)
print("Lista 5: ",lista5,)
print("Lista 6: ",lista6,)
print("Lista 7:",lista7,)

print("Creamos la Lista 8 con Los valores comunes entre las dos listas introducidas manualmente, siendo: ",lista8,)
>>>>>>> 1cafc75f29b86e3c8ed0daa698f010cede8c18d9
print("La longito de la Lista 8 es :",len(lista8))