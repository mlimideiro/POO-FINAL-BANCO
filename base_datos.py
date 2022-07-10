from abc import abstractclassmethod
from secuencia import *
import random as rd
         
class Base_datos():

    dic_cli_nombre_us = {
        "us1" : {
            "Nombre" : "Juan",
            "Apellido" : "Lopez",
            "Domicilio" : "Allá al 1100",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "jlopez@algo.com",
            "Nombre usuario" : "us1",
            "Password" : "pass1"
            },
        "us2" : {
            "Nombre" : "Pedro",
            "Apellido" : "Gomez",
            "Domicilio" : "Allá al 2000",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "pgomez@algo.com",
            "Nombre usuario" : "us2",
            "Password" : "pass2"
            },
        "us3" : {
            "Nombre" : "Marcelo",
            "Apellido" : "Gutierrez",
            "Domicilio" : "Lejos 500",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "mgutierrez@algo.com",
            "Nombre usuario" : "us3",
            "Password" : "pass3"
            },
        "us4" : {
            "Nombre" : "José",
            "Apellido" : "Garcia",
            "Domicilio" : "Perón 1100",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "jgarcia@algo.com",
            "Nombre usuario" : "us4",
            "Password" : "pass4"
            },
        "us5" : {
            "Nombre" : "Pepe",
            "Apellido" : "Rodriguez",
            "Domicilio" : "Paz 350",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "prodriguez@algo.com",
            "Nombre usuario" : "us5",
            "Password" : "pass5"
            },
        "us6" : {
            "Nombre" : "Santiago",
            "Apellido" : "Rojas",
            "Domicilio" : "Alem 871",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "srojas@algo.com",
            "Nombre usuario" : "us6",
            "Password" : "pass6"
            },
        "us7" : {
            "Nombre" : "José",
            "Apellido" : "Martínez",
            "Domicilio" : "Alberdi 895",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "jmartinez@algo.com",
            "Nombre usuario" : "us7",
            "Password" : "pass7"
            },
        "us8" : {
            "Nombre" : "Pedro",
            "Apellido" : "Fernández",
            "Domicilio" : "Avellaneda 2354",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "pfernandez@algo.com",
            "Nombre usuario" : "us8",
            "Password" : "pass8"
            },
        "us9" : {
            "Nombre" : "Martín",
            "Apellido" : "Gómez",
            "Domicilio" : "Rivadavia 87",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "mgomez@algo.com",
            "Nombre usuario" : "us9",
            "Password" : "pass9"
            },
        "us10" : {
            "Nombre" : "Sebastián",
            "Apellido" : "Reyes",
            "Domicilio" : "Rodriguez 894",
            "D.N.I." : Secuencia.next_nro_dni(),
            "Cuit/Cuil" : Secuencia.next_nro_dni()-1,
            "Teléfono" : rd.randint(5550000,5559999),
            "Email" : "sreyes@algo.com",
            "Nombre usuario" : "us10",
            "Password" : "pass10"
            }

        }
    
    def __init__(self, nombre_base_datos):
        self.nombre_base_datos = nombre_base_datos

    @abstractclassmethod
    def get_usuarios_nombre(cls): 
        return cls.dic_cli_nombre_us   