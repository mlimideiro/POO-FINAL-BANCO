from abc import abstractclassmethod

class Secuencia():

    nro_cuenta = 1000
    nro_dni = 20000000
    nro_cbu = 900000000000
    nro_plazo_fijo = 100
    
    @abstractclassmethod
    def next_nro_cuenta(cls):
        cls.nro_cuenta += 1
        return cls.nro_cuenta-1

    @abstractclassmethod
    def next_nro_dni(cls):
        cls.nro_dni += 1
        return cls.nro_dni-1
    
    @abstractclassmethod
    def next_cbu(cls):
        cls.nro_cbu += 1
        return cls.nro_cbu-1

    @abstractclassmethod
    def next_plazo_fijo(cls):
        cls.nro_plazo_fijo += 1
        return cls.nro_plazo_fijo-1