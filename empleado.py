class Empleado():
    def __init__(self, nombre, apellido, dni, banco, puesto, empresa, sueldo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.banco = banco
        self.puesto = puesto
        self.empresa = empresa
        self.sueldo = sueldo
        self.salario = salario
        
    def __str__(self):
        return ("Empleado: \n\tApellido y nombre: " + str(self.apellido) + " " + str(self.nombre) + "\n\tEmpresa: " + str(self.empresa) +"\n\tD.N.I.: " + str(self.dni) + "\n\tCliente banco: " + str(self.banco) + "\n\tPuesto: " + str(self.puesto) + "\n\tSueldo: $ " + str(self.sueldo))
