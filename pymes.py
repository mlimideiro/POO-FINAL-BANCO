from clientes import *
from usuario import *

class Pymes(Clientes, Usuario):
    def __init__ (self, razon_social, domicilio, cuitCuil, telefono, email, nombre_us, password):
        Clientes.__init__(self, domicilio, cuitCuil, telefono, email)
        Usuario.__init__(self,nombre_us, password)
        self.razon_social = razon_social
        self.cuentas = {}

    def get_cuentas (self):
        return self.cuentas

    def __str__(self):
        return ("Nombre Pyme: " + str(self.razon_social) + "\nDomicilio: " + str(self.domicilio) + "\nCUIT/CUIL: " + str(self.cuitCuil) + "\nTelefono: " + str(self.telefono) + "\nEmail: " + str(self.email) + "\nUsuario: " + str(self.nombre_us) + "\nPassword: " + str(self.password) + "\nCuentas:\n\t" + str(self.cuentas) + "\n")
