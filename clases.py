# class Usuario():

#     def __init__(self,nombre_us, password):
#         self.nombre_us = nombre_us
#         self.password = password
#         self.dic_us = {}

#     def validar_login():
#         pass

 
# class Administrador(Usuario):
#     def __init__ (self, nombre_us, password):
#         Usuario.__init__(self, nombre_us, password)
#         self.nombre_us = "ADMINISTRADOR"
#         self.password = "ADM1N1STR4DOR"

# class Clientes():
#     def __init__(self, domicilio, cuitCuil, telefono, email):
#         self.domicilio = domicilio
#         self.cuitCuil = cuitCuil
#         self.telefono = telefono
#         self.email = email
       
# class Individuos(Clientes,Usuario):
#     def __init__ (self, nombre, apellido, domicilio, dni, cuitCuil, telefono, email, nombre_us, password):
#         Clientes.__init__(self, domicilio, cuitCuil, telefono, email)
#         Usuario.__init__(self,nombre_us, password)
#         self.nombre = nombre
#         self.apellido = apellido
#         self.dni = dni
#         self.cuentas = {}

#     def get_cuentas (self):
#         return self.cuentas
        
#     def __str__(self):
#         return ("Nombre: " + str(self.nombre) + "\nApellido: " + str(self.apellido) + "\nDomicilio: " + str(self.domicilio) + "\nDNI: " + str(self.dni) + "\nCUIT/CUIL: " + str(self.cuitCuil) + "\nTelefono: " + str(self.telefono) + "\nEmail: " + str(self.email) + "\nUsuario: " + str(self.nombre_us) + "\nPassword: " + str(self.password) + "\nCuentas:\n\t" + str(self.cuentas) + "\n")

# class Pymes(Clientes, Usuario):
#     def __init__ (self, razon_social, domicilio, cuitCuil, telefono, email, nombre_us, password):
#         Clientes.__init__(self, domicilio, cuitCuil, telefono, email)
#         Usuario.__init__(self,nombre_us, password)
#         self.razon_social = razon_social
#         self.cuentas = {}

#     def get_cuentas (self):
#         return self.cuentas

#     def __str__(self):
#         return ("Nombre Pyme: " + str(self.razon_social) + "\nDomicilio: " + str(self.domicilio) + "\nCUIT/CUIL: " + str(self.cuitCuil) + "\nTelefono: " + str(self.telefono) + "\nEmail: " + str(self.email) + "\nUsuario: " + str(self.nombre_us) + "\nPassword: " + str(self.password) + "\nCuentas:\n\t" + str(self.cuentas) + "\n")

# class Empleado():
#     def __init__(self, nombre, apellido, dni, banco, puesto, empresa, sueldo, salario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.dni = dni
#         self.banco = banco
#         self.puesto = puesto
#         self.empresa = empresa
#         self.sueldo = sueldo
#         self.salario = salario
        
#     def __str__(self):
#         return ("Empleado: \n\tApellido y nombre: " + str(self.apellido) + " " + str(self.nombre) + "\n\tEmpresa: " + str(self.empresa) +"\n\tD.N.I.: " + str(self.dni) + "\n\tCliente banco: " + str(self.banco) + "\n\tPuesto: " + str(self.puesto) + "\n\tSueldo: $ " + str(self.sueldo))

# class Cuentas():
#     def __init__(self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo):
#         self.titular = titular
#         self.sucursal = sucursal
#         self.num_cuenta = num_cuenta
#         self.cbu = cbu
#         self.fecha_apert = fecha_apert
#         self.saldo = saldo
        
# class SaldoRetenido():
#     def __init__(self, monto_retenido):
#         self.monto_retenido = monto_retenido

# class CajaAhorroComun(Cuentas):
#     def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo):
#         Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
#         self.tipo = tipo
        
#     def __str__(self):
#         return ("\tCuenta tipo: " + str(self.tipo) + "\n\tCaja Ahorro Común: " + "\n\tN° cuenta: " + str(self.num_cuenta) + "\n\tSucursal: " +  str(self.sucursal) + "\n\tTitular: " + str(self.titular) + "\n\tCBU: " + str(self.cbu) + "\n\tFecha de apertura: " + str(self.fecha_apert) + "\n\tSaldo: $" + str(self.saldo))

# class CajaAhorroRS(Cuentas, SaldoRetenido):
#     def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, monto_retenido, saldo):
#         Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
#         SaldoRetenido.__init__(self, monto_retenido)
#         self.tipo = tipo
            
#     def __str__(self):
#         return ("Cuenta tipo: " + str(self.tipo) + "\nCaja Ahorro con Ret de Saldo" + "\n\tTitular: " + str(self.titular) + "\n\tN° cuenta: " + str(self.sucursal) + "-" + str(self.num_cuenta) +  "\n\tCBU: " + str(self.cbu) + "\n\tFecha de apertura: " + str(self.fecha_apert) + "\n\tSaldo: $" + str(self.saldo)+ "\n\tSaldo Retenido: $ " + str(self.monto_retenido))

# class CuentaCorrienteComun(Cuentas):
#     def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, saldo):
#         Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
#         self.tipo = tipo
#         self.moneda = moneda

#     def __str__(self):
#         return("Cuenta tipo: " + str(self.tipo) + " \n\tCuenta Corriente Común \n\tTitular: "  + str(self.titular) + " \n\tSucursal: " + str(self.sucursal) + " \n\tN° de cuenta: " + str(self.num_cuenta) + " \n\tCBU: " + str(self.cbu) + " \n\tFecha de apertura: " + str(self.fecha_apert) + " \n\tMoneda: " + str(self.moneda) + " \n\tSaldo: $ " + str(self.saldo))

# class CuentaCorrienteSR(Cuentas, SaldoRetenido):
#     def __init__(self, tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, saldo, monto_retenido):
#         Cuentas.__init__ (self, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
#         SaldoRetenido.__init__(self, monto_retenido)
#         self.tipo = tipo
#         self.moneda = moneda

#     def __str__(self):
#         return("Cuenta tipo: " + str(self.tipo) + "\n\tCuenta Corriente Saldo Ret. \n\tTitular: " + str(self.titular) + "\n\tSucursal: " + str(self.sucursal) + "\n\tN° de cuenta: " + str(self.num_cuenta) + "\n\tCBU: " + str(self.cbu) + "\n\tFecha de apertura: " + str(self.fecha_apert) + "\n\tMoneda: " + str(self.moneda) + "\n\tSaldo: $ " + str(self.saldo) + "\n\tSaldo Retenido: $ " + str(self.monto_retenido))

# class PlazoFijo():
#     def __init__(self, num_pf, titular, plazo, importe_inicial, fecha_inicio, importe_retiro, fecha_vencimiento):
#         self.num_pf = num_pf
#         self.titular = titular
#         self.plazo = plazo
#         self.importe_inicial = importe_inicial
#         self.fecha_inicio = fecha_inicio
#         self.importe_retiro = importe_retiro
#         self.fecha_vencimiento = fecha_vencimiento

#     def __str__(self):
#         return("Plazo fijo n° " + str(self.num_pf) + "\n\tTitular: " + str(self.titular) + "\n\tPlazo: " + str(self.plazo) + " dias\n\tImporte inicial: $ " + str(self.importe_inicial) + "\n\tFecha de alta: " + str(self.fecha_inicio) + "\n\tImporte a retirar: $ " + str(self.importe_retiro) + "\n\tFecha vencimiento: " + str(self.fecha_vencimiento))
    