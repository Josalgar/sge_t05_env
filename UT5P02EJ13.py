#13.-Escribir un programa que pida al usuario un número entero impar. Si es par dará un error. 
# Si es impar mostrará por pantalla un triángulo rectángulo como el de la imagen:

def esImpar(numero):
    if numero%2==0 :
        raise ValueError("ERROR. El número facilitado no es impar")
    else :
        miMatriz=[numero,numero+2,numero+4,numero+6,numero+8]

        print(miMatriz[0])
        print(miMatriz[1],miMatriz[0])
        print(miMatriz[2],miMatriz[1],miMatriz[0])
        print(miMatriz[3],miMatriz[2],miMatriz[1],miMatriz[0])
        print(miMatriz[4],miMatriz[3],miMatriz[2],miMatriz[1],miMatriz[0])
        
numero=int(input("Indícame un número impar:\n"))

try:
    esImpar(numero)

except ValueError as ErrorDeNumeroPar:
    print(ErrorDeNumeroPar)

