#Escribir un programa que almacene las siguientes matrices en una lista y muestre por pantalla su producto:
    
lista1=[1,2,3]
lista2=[4,5,6]
lista3=[-1,0]
lista4=[0,1]
lista5=[1,1]

matriz1=[lista1,
         lista2]
matriz2=[lista3,
         lista4,
         lista5]

resultado=[]

for i in range(len(matriz1)):
    resultado.append([])
    for j in range(len(matriz2[0])):
        resultado[i].append(0)    

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz1[0])):
            resultado[i][j]+=matriz1[i][k]*matriz2[k][j]  

for r in resultado:
    print(r) 
