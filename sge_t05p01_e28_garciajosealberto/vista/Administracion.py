
opcion=None

def menu(opcion):
    match opcion:
        case 1:
            #verlistadosocios
            pass
            
        case 2:
            #insertar socio
            pass
        case 3:
            #añadir familia
            pass
        case 4:
            #ver eventos
            pass
        case 5:
            #buscar evnetos
            pass
        case 6:
            #añadir evento
            pass
        case 7:
            #control cuotas
            pass
        case 8:
            #actualizar control cuotas
            pass
        case 9:
            #pago cuota socio
            pass

        case _:
            print("La opción indicada no es válida, por favor, indique una opción correcta.")

while opcion!=0:
    print("MENÚ ADMINISTRACIÓN")
    input=int("Elige la opción a realizar.")
    print("1.- Ver listado completo de socios.")
    print("2.- Insertar nuevo socio y crear usuario.")
    print("3.-Añadir familia a un socio.")
    print("4.-Ver listado completo de los próximos eventos.")
    print("5.-Buscar eventos por fecha y mostrar su información.")
    print("6.-Añadir un nuevo evento.")
    print("7.-Acceder al control de cuotas-socios por años.")
    print("8.-Actualizar el control de cuotas-socio para el año en curso.")
    print("9.-Realizar el pago de una cuota de socio")
    print("0.- Salir.")
