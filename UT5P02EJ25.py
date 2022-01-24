class Punto:
    X=None
    Y=None
    
    def _init_(self,X=0,Y=0):
        self.X=X
        self.Y=Y
        
    def __str__(self):
        coordenada="(self.X,self.Y)"
        return coordenada
    
    def cuadrante(self):
        if self.x==0 & self.y!=0:
            print("La coordenada está en el eje Y.")
        elif self.x!=0 & self.y==0:
            print("La coordenada está en el eje X.")
        elif self.x==0 & self.y==0:
            print("La coordenada está en el origen.")
        elif self.x>0 & self.y>0:
            print("La coordenada está en el cuadrante 1.")
        elif self.x>0 & self.y<0:
            print("La coordenada está en el cuadrante 4.")
        elif self.x<0 & self.y>0:
            print("La coordenada está en el cuadrante 2.")
        elif self.x<0 & self.y<0:
            print("La coordenada está en el cuadrante 3.")
        else:
            print("Coordenadas erróneas")
            
    def vector(self,puntoB):
        print("El vector resultante de los puntos facilitados es "+(puntoB.X-self.X,puntoB.Y-self.Y))
    
    def distancia(self, puntoB):
        dist=((puntoB.X-self.X)**2+(puntoB.Y-self.Y)**2)**0.5
        print("La distancia entre los puntos facilitados es "+dist)
        

class Rectangulo:
    def __init__(self,pInicial=0,pFinal=0):
        self.pInicial=pInicial
        self.pFinal=pFinal
        
    def es_rectangulo(self,puntoB):
        if self.X-puntoB.X!=0 & self.Y-puntoB.Y!=0 :
            print("Los puntos pueden formar un rectángulo")
        elif (self.X-puntoB.X) == (self.Y-puntoB.Y9):
            print("Los puntos dados forman un cuadrado")
        else:
            print("Los puntos dados no forman un rectángulo")
        
    def base(self,puntoB):
        base=0
        if self.X>puntoB.X :
            base=self.X-puntoB.X
            print("La base del rectángulo es "+base)
        elif self.X<puntoB.X :
            base=puntoB.X-self.X
            print("La base del rectángulo es "+base)
        else:
            print("La base es 0")
    
    def altura(self,puntoB):
        altura=0
        if self.Y>puntoB.Y:
            altura=self.Y-puntoB.Y
            print("La altura del rectángulo es "+altura)
        elif self.Y<puntoB.Y:
            altura=puntoB.Y-self.Y
            print("La altura del rectángulo es "+altura)
        else:
            print("La altura es 0")
        
    
    def area(self,puntoB):
        base=0
        if self.X>puntoB.X :
            base=self.X-puntoB.X
            return base
        elif self.X<puntoB.X :
            base=puntoB.X-self.X
            return base
        else:
            print("La base es 0")
            
        altura=0
        if self.Y>puntoB.Y:
            altura=self.Y-puntoB.Y
            print("La altura del rectángulo es "+altura)
        elif self.Y<puntoB.Y:
            altura=puntoB.Y-self.Y
            print("La altura del rectángulo es "+altura)
        else:
            print("La altura es 0")
punto1=None 
punto2=None
      
print("Facilita las coordenadas del eje X para el punto 1")    
X=input()
print("Facilita las coordenadas del eje Y para el punto 1")    
Y=input()

punto1=Punto(X,Y)

while punto2.X==punto1.X and punto2.Y==punto1.Y :
    print("Facilita las coordenadas del eje X para el punto 2")    
    X2=input()
    print("Facilita las coordenadas del eje Y para el punto 2")    
    Y2=input()
    punto2=Punto(X2,Y2)
opcion=None
subOpc=None
while opcion!=3 :
    print("Elige una opción del menú")
    print("Menú")
    print("1.- Operaciones con puntos.")
    print("2.- Operaciones con rectángulos.")
    print("3.- Salir")
    opcion=input()
    if opcion==1 :
        print("Elige una opción del submenú de Operaciones con puntos")
        print("Submenu")
        print("a. Mostrar cuadrante al que pertencen.")
        print("b. Calcular vector.")
        print("c. Calcular distancia.")
        subOpc=input()
            
        if subOpc=="a":
            Punto.cuadrante
        elif subOpc=="b" :
            Punto.vector
        elif subOpc=="c" :
            Punto.distancia
        else:
            print("Opción no válida.")  

    elif opcion==2 :
        print("Elige una opción del submenú de Operaciones con rectángulos")
        print("Submenu")
        print("a. Calcular la base.")
        print("b. Calcular la altura.")
        print("c. Calcular el área.")
        subOpc=input()
        
        if (subOpc=="a") :
            Rectangulo.base
        elif subOpc=="b" :
            Rectangulo.altura    
        elif subOpc=="c" :
            Rectangulo.area    
        else:
            print("Opción no válida.")     
    elif opcion==3 :
        print("Ha salido de la aplicación.")
        exit()
        
    else:
        print("Opción errónea, por favor indique otra.")

