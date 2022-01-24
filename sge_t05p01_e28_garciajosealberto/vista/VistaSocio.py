opcion=None

def menu(opcion):
    match opcion:
        case 1:
            #Ver prox eventos y socios inscritos
            pass

        case 2:
            #Ver/apuntarme prox eventos
            pass

        case 3:
            #Ver mis bicicletas
            pass
        case 4:
            #Ver mis reparaciones/mantenimientos
            pass
        case 5:
            #Añadir bicicleta
            pass

        case 6:
            #Añadir reparación/mantenimiento a bici
            pass

        case 7:
            #Ver mi familia
            pass

        case 8:
            #Ver historio y cuotas
            pass
        case 9:
            exit
        
        case _:
            print("La opción indicada no es correcta, por favor indica una nueva.")

while opcion!=0:
    print("Menú Socio")
    opcion=int(input("Elige la opción a realizar."))
    print("1.- Ver mis próximos eventos y socios inscritos.")
    print("2.- Ver/Apuntarme a proximo eventos abiertos.")
    print("3.- Ver mis bicicletas.")
    print("4.- Ver mis reparaciones/mantenimientos.")
    print("5.- Añadir nueva bicicleta.")
    print("6.- Añadir reparación/mantenimiento a bicicleta.")
    print("7.- Ver mi familia.")
    print("8.- Ver mi historico y estado de cuotas.")
    print("0.- Salir")