from usuario import *

class Administrador(Usuario):
    def __init__ (self, nombre_us, password):
        Usuario.__init__(self, nombre_us, password)
        self.nombre_us = "ADMINISTRADOR"
        self.password = "ADM1N1STR4DOR"
