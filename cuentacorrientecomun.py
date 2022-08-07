from cuentas import *

class CuentaCorrienteComun(Cuentas):
    def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, saldo):
        Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
        self.tipo = tipo
        self.moneda = moneda

    def __str__(self):
        return("Cuenta tipo: " + str(self.tipo) + " \n\tCuenta Corriente Común \n\tTitular: "  + str(self.titular) + " \n\tSucursal: " + str(self.sucursal) + " \n\tN° de cuenta: " + str(self.num_cuenta) + " \n\tCBU: " + str(self.cbu) + " \n\tFecha de apertura: " + str(self.fecha_apert) + " \n\tMoneda: " + str(self.moneda) + " \n\tSaldo: $ " + str(self.saldo))

