from abc import abstractclassmethod
from secuencia import *
import random as rd
from datetime import date, datetime, timedelta

class BaseDatosCuentas():

    dic_cuentas = {
            Secuencia.next_nro_cuenta()  : {
                "Cuenta tipo" : "3",
                "Titular" : "py3",
                "Sucursal" : rd.randint(100,103),
                "N° de cuenta" : Secuencia.next_nro_cuenta()-1,
                "CBU" : Secuencia.next_cbu(),
                "Fecha apertura" : datetime.now(),
                "Moneda" : "Pesos",
                "Saldo" : 47500
                },
            Secuencia.next_nro_cuenta()  : {
                "Cuenta tipo" : "3",
                "Titular" : "py2",
                "Sucursal" : rd.randint(100,103),
                "N° de cuenta" : Secuencia.next_nro_cuenta()-1,
                "CBU" : Secuencia.next_cbu(),
                "Fecha apertura" : datetime.now(),
                "Moneda" : "Pesos",
                "Saldo" : 500
                },
            Secuencia.next_nro_cuenta()  : {
                "Cuenta tipo" : "3",
                "Titular" : "py1",
                "Sucursal" : rd.randint(100,103),
                "N° de cuenta" : Secuencia.next_nro_cuenta()-1,
                "CBU" : Secuencia.next_cbu(),
                "Fecha apertura" : datetime.now(),
                "Moneda" : "Pesos",
                "Saldo" : 420000
                },
            Secuencia.next_nro_cuenta()  : {
                "Cuenta tipo" : "3",
                "Titular" : "py3",
                "Sucursal" : rd.randint(100,103),
                "N° de cuenta" : Secuencia.next_nro_cuenta()-1,
                "CBU" : Secuencia.next_cbu(),
                "Fecha apertura" : datetime.now(),
                "Moneda" : "Pesos",
                "Saldo" : 20000
                },
            }
        

    def __init__(self, cuentas_base_datos):
        self.cuentas_base_datos = cuentas_base_datos
    
    @abstractclassmethod
    def get_cuentas(cls): 
        return cls.dic_cuentas