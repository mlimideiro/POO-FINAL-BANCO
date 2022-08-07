from cuentas import *

class CajaAhorroComun(Cuentas):
    def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo):
        Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
        self.tipo = tipo
        
    def __str__(self):
        return ("\tCuenta tipo: " + str(self.tipo) + "\n\tCaja Ahorro Común: " + "\n\tN° cuenta: " + str(self.num_cuenta) + "\n\tSucursal: " +  str(self.sucursal) + "\n\tTitular: " + str(self.titular) + "\n\tCBU: " + str(self.cbu) + "\n\tFecha de apertura: " + str(self.fecha_apert) + "\n\tSaldo: $" + str(self.saldo))
