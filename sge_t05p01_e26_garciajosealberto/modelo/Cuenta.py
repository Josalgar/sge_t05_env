class Cuenta:
    numCuenta=None
    dni=None
    nombreT=None
    saldo=None
    movimientos=[]
    
    generadorCuenta=0
    def __init__(self,dni,nombreT,saldo,movimientos) :
        self.dni=dni
        self.nombreT=nombreT
        self.saldo=saldo
        self.movimientos=movimientos
        self.numCuenta=Cuenta.generadorCuenta
        Cuenta.generadorCuenta+=1
        
    def imprimir_cuenta:
        
    def hacer_movimiento(movimiento):
        if saldo>=0:
            saldo=saldo+movimiento
            return saldo
        else:
            print("Saldo ")