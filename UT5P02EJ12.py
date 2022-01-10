# 12. Crear un script que dada una palabra determine si es un palíndromo.

palabra=input("Dime una palabra:\n ")
palabraInv=palabra[::-1]

if (palabra.lower()==palabraInv.lower()) :
    print("La palabra es palíndroma")
else :
    print("La palabra no es palíndroma")

