from cuentas import *
from saldoretenido import *

class CajaAhorroRS(Cuentas, SaldoRetenido):
    def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, monto_retenido, saldo):
        Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
        SaldoRetenido.__init__(self, monto_retenido)
        self.tipo = tipo
            
    def __str__(self):
        return ("Cuenta tipo: " + str(self.tipo) + "\nCaja Ahorro con Ret de Saldo" + "\n\tTitular: " + str(self.titular) + "\n\tN° cuenta: " + str(self.sucursal) + "-" + str(self.num_cuenta) +  "\n\tCBU: " + str(self.cbu) + "\n\tFecha de apertura: " + str(self.fecha_apert) + "\n\tSaldo: $" + str(self.saldo)+ "\n\tSaldo Retenido: $ " + str(self.monto_retenido))
