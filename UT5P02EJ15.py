#    15. Determinar si un número entero dado leído desde el teclado es abundante o no.
#Un número abundante es un número natural cuyos divisores (todos los divisores excepto el propio número) 
# sumen más que dicho número. Ejemplo: 24 < 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36.

numero=int(input("Facilita un número:\n"))
suma=0
for i in range(1,numero-1):
    if numero%i==0:
        suma+=i
       
if suma>numero :
    print(f"La suma de los divisores es {suma}. El número facilitado es abundante")
else :
    print(f"La suma de los divisores es {suma}. El número facilitado no es abundante")