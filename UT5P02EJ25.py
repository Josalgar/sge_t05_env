from pickle import FALSE


class Punto:
    X=None
    Y=None
    
    def __init__(self,X=0,Y=0):
        self.X=X
        self.Y=Y
        
    def __str__(self):
        coordenada="(%d,%d)" % (self.X, self.Y)
        return coordenada
    
    def cuadrante(self):
        if (self.X==0 and self.Y!=0):
            print("La coordenada está en el eje Y.")
        elif (self.X!=0 and self.Y==0):
            print("La coordenada está en el eje X.")
        elif (self.X==0 and self.Y==0):
            print("La coordenada está en el origen.")
        elif (self.X>0 and self.Y>0):
            print("La coordenada está en el cuadrante 1.")
        elif (self.X>0 and self.Y<0):
            print("La coordenada está en el cuadrante 4.")
        elif (self.X<0 and self.Y>0):
            print("La coordenada está en el cuadrante 2.")
        elif (self.X<0 and self.Y<0):
            print("La coordenada está en el cuadrante 3.")
        else:
            print("Coordenadas erróneas")
            
    def vector(self,puntoB):
        vtor=puntoB.X-self.X,puntoB.Y-self.Y
        print("El vector resultante de los puntos facilitados es "+format(vtor))
    
    def distancia(self, puntoB):
        dist=((puntoB.X-self.X)**2+(puntoB.Y-self.Y)**2)**0.5
        print("La distancia entre los puntos facilitados es "+format(dist))
        

class Rectangulo:
    def __init__(self,pInicial=0,pFinal=0):
        self.pInicial=pInicial
        self.pFinal=pFinal
        
    def es_rectangulo(self):
        if self.pInicial.X-self.pFinal.X!=0 and self.pInicial.Y-self.pFinal.Y!=0 :
            return True
       
        else:
            return False
        
    def base(self):
        base=None
        if self.pInicial.X>self.pFinal.X :
            base=self.pInicial.X-self.pFinal.X
            return base
        elif self.pInicial.X<self.pFinal.X :
            base=self.pFinal.X-self.pInicial.X
            return base
        else:
            return base
    
    def altura(self):
        altura=0
        if self.pInicial.Y>self.pFinal.Y:
            altura=self.pInicial.Y-self.pFinal.Y
            return altura
        elif self.pInicial.Y<self.pFinal.Y:
            altura=self.pFinal.Y-self.pInicial.Y
            return altura
        else:
            return altura
        
    
    def area(self):
        area=self.base()*self.altura()
        print("El área del rectángulo que forman los puntos es "+format(area))
        
        
punto1=None 
punto2=None
puntosDistintos=False
      
print("Facilita las coordenadas del eje X para el punto 1: ")    
X=int(input())
print("Facilita las coordenadas del eje Y para el punto 1: ")    
Y=int(input())

punto1= Punto(X,Y)
print("Punto1:",punto1)



while (not puntosDistintos):
    print("Facilita las coordenadas del eje X para el punto 2: ")    
    X=int(input())
    print("Facilita las coordenadas del eje Y para el punto 2: ")    
    Y=int(input())
    punto2= Punto(X,Y)
    
    
    if punto2.X==punto1.X and punto2.Y==punto1.Y :
        print("Los puntos creados no pueden tener las mismas coordenadas")
    else:
        puntosDistintos=True

print("Punto 2:",punto2)

opcion=None
subOpc=None
while opcion!=3 :
    print("Elige una opción del menú")
    print("Menú")
    print("1.- Operaciones con puntos.")
    print("2.- Operaciones con rectángulos.")
    print("3.- Salir")
    opcion=input()
    if opcion=="1" :
        print("Elige una opción del submenú de Operaciones con puntos")
        print("Submenu")
        print("a. Mostrar cuadrante al que pertencen.")
        print("b. Calcular vector.")
        print("c. Calcular distancia.")
        subOpc=input()
            
        if subOpc=="a":
            print("Punto 1: ")
            punto1.cuadrante()
            print("Punto 2: ")
            punto2.cuadrante()
        elif subOpc=="b" :
            punto1.vector(punto2)
        elif subOpc=="c" :
            punto1.distancia(punto2)
        else:
            print("Opción no válida.")  

    elif opcion=="2" :
        print("Elige una opción del submenú de Operaciones con rectángulos")
        print("Submenu")
        print("a. Calcular la base.")
        print("b. Calcular la altura.")
        print("c. Calcular el área.")
        subOpc=input()
        
        if Rectangulo(punto1,punto2).es_rectangulo==True:
            if (subOpc=="a") :
           
                print("La base es ",Rectangulo(punto1,punto2).base())
            elif subOpc=="b" :
                print("La altura es ",Rectangulo(punto1,punto2).altura())  
            elif subOpc=="c" :
                Rectangulo(punto1,punto2).area()    
            else:
                print("Opción no válida.") 
        else:
            print("La operación no se puede realizar, los puntos no forman un rectángulo")    
    elif opcion=="3" :
        print("Ha salido de la aplicación.")
        exit()
        
    else:
        print("Opción errónea, por favor indique otra.")

