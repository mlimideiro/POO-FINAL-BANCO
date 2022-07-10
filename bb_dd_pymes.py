from abc import abstractclassmethod
from secuencia import *
import random as rd

class BaseDatosPymes():

    dic_clientes_pymes = {
        "py1" : {
            "Razón social" : "La perinola",
            "Domicilio" : "Acá al 1100",
            "Cuit/cuil" : Secuencia.next_nro_dni(),
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "laperinola@algo.com",
            "Nombre usuario" : "py1",
            "Password" : "pass1",
        },
        "py2" : {
            "Razón social" : "El Equipo",
            "Domicilio" : "Lejos 4200",
            "Cuit/cuil" : Secuencia.next_nro_dni(),
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "elequipo@algo.com",
            "Nombre usuario" : "py2",
            "Password" : "pass2",
        },
        "py3" : {
            "Razón social" : "El club",
            "Domicilio" : "Allá al 2000",
            "Cuit/cuil" : Secuencia.next_nro_dni(),
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "elclub@algo.com",
            "Nombre usuario" : "py3",
            "Password" : "pass3"
            }
        }
    

    def __init__(self, usuario_base_datos):
        self.usuario_base_datos = usuario_base_datos
    
    @abstractclassmethod
    def get_pymes(cls): 
        return cls.dic_clientes_pymes