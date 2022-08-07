from clientes import *
from usuario import *


class Individuos(Clientes,Usuario):
    def __init__ (self, nombre, apellido, domicilio, dni, cuitCuil, telefono, email, nombre_us, password):
        Clientes.__init__(self, domicilio, cuitCuil, telefono, email)
        Usuario.__init__(self,nombre_us, password)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuentas = {}

    def get_cuentas (self):
        return self.cuentas
        
    def __str__(self):
        return ("Nombre: " + str(self.nombre) + "\nApellido: " + str(self.apellido) + "\nDomicilio: " + str(self.domicilio) + "\nDNI: " + str(self.dni) + "\nCUIT/CUIL: " + str(self.cuitCuil) + "\nTelefono: " + str(self.telefono) + "\nEmail: " + str(self.email) + "\nUsuario: " + str(self.nombre_us) + "\nPassword: " + str(self.password) + "\nCuentas:\n\t" + str(self.cuentas) + "\n")
