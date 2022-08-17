import random as rd
from secuencia import *
from datetime import date, datetime, timedelta
from base_datos import *
from bb_dd_pymes import *
from bb_dd_cuentas import *
from individuos import *
from usuario import *
from administrador import *
from clientes import *
from cajaahorrocomun import *
from cuentas import *
from cuentacorrientesr import *
from plazofijo import *
from saldoretenido import *
from cajaahorrocomun import *
from cuentacorrientecomun import *
from pymes import *
from empleado import *
from cajaahorrors import *


class Banco():

    #Constructor de la clase Banco:
    #Diccionarios que almacenan datos de cuentas, clientes_dni, clientes_usuarios, clientes_pymes,
    #sueldos_pymes, dic_plazofijo, movimientos_cuentas, clientes_log, adm_usuarios, adm_password,
    #costos_mantenim y sucursales
    def __init__(self):

        self.cuenta = {}
        self.clientes_dni = {}
        self.clientes_usuarios = {}
        self.clientes_pymes = {}
        self.sueldos_pymes = {}
        self.dic_plazo_fijo = {}
        self.movimientos_cuentas = {}
        self.cliente_log = None
        self.adm_usuario = "administrador"
        self.adm_password = "adm1n1str4d0r"
        self.costos_mantenim = { 
            1: ["Monto Minimo Saldo Retenido (SR)",5000],
            2: ["Mantenimiento Caja Ahorro común",200],
            3: ["Mantenimiento Caja Ahorro SR",0],
            4: ["Transferencia C.A.Común",5],
            5: ["Transferencia C.A.S.R.",0],
            6: ["Pagos en línea C.A.Común",3],
            7: ["Pagos en línea C.C.S.R. y C.A.S.R.",0],
            8: ["Mantenimiento Cuenta Corriente en Pesos",500],
            9: ["Mantenimiento Cuenta Corriente Moneda Extranjera",800],
            10: ["Mantenimiento Cuenta Corriente con SR",0],
            11: ["Transferencia C.C.Común",5],
            12: ["Transferencia C.C.SR",0],
            13: ["Pagos en linea C.C.Común",3],
            14: ["Plazo fijo", 3, 5, 8, 10, 13],
            15: ["Costo depósito C.A.Común",5],
            16: ["Costo depósito C.A.S.R.",0],
            17: ["Costo depósito C.C.Común",5],
            18: ["Costo depósito C.C.S.R.",0],
            19: ["Pago Sueldos Mismo Banco",0],
            20: ["Pago Sueldos Otro Banco",4],
            21: ["Cotización Dólar",rd.randint(240,300)],
            22: ["Valor Bonos",rd.randint(1000,5000)],
            23: ["Variación Bonos",rd.randint(2,5)]
        }
        self.dictSucursales = {
            100: ["Tandil"],
            101: ["Olavarría"],
            102: ["Bolívar"],
            103: ["Azul"]
        }
    #Crea objeto datos con el dicc de la base de datos
    def load_datos(self):
        for dato in Base_datos.get_usuarios_nombre():
            datos = Base_datos.get_usuarios_nombre()[dato]
            ob_cliente = Individuos(datos["Nombre"],datos["Apellido"], datos["Domicilio"],datos["D.N.I."],datos["Cuit/Cuil"],datos["Teléfono"],datos["Email"],datos["Nombre usuario"], datos["Password"])
            self.clientes_usuarios[datos["Nombre usuario"]] = ob_cliente
            self.clientes_dni[datos["D.N.I."]] = ob_cliente 

    #Crea objeto pymes con el dicc de las pymes
    def load_pymes(self):
        for py in BaseDatosPymes.get_pymes():
            pymes = BaseDatosPymes.get_pymes()[py]
            ob_pymes = Pymes(pymes["Razón social"], pymes["Domicilio"], pymes["Cuit/cuil"], pymes["Teléfono"], pymes["Email"], pymes["Nombre usuario"], pymes["Password"])
            self.clientes_pymes[pymes["Nombre usuario"]] = ob_pymes
    
    #Crea objeto cuentas con el dicc de las pymes
    def load_cuentas(self):
        for cu in BaseDatosCuentas.get_cuentas():
            cuentas = BaseDatosCuentas.get_cuentas()[cu]
            ob_cuentas = CuentaCorrienteComun(cuentas["Cuenta tipo"], cuentas["Titular"], cuentas["Sucursal"], cuentas["N° de cuenta"], cuentas["CBU"], cuentas["Fecha apertura"], cuentas["Moneda"], cuentas["Saldo"])
            self.cuenta[cuentas["N° de cuenta"]] = ob_cuentas
            cu = ob_cuentas.num_cuenta
            dia = ob_cuentas.fecha_apert
            self.movimientos_cuentas[cu] = {}
            self.movimientos_cuentas[cu][dia] = ( 
            "APERTURA DE CUENTA")

    #Carga el menú de loguin de eleccion de usuario
    def loguin(self):
        print("\n\n**********************")
        print("    BANCO  BRULIM    ")
        print("**********************")
        print("*   MENU PRINCIPAL   *")
        print("**********************")
        print("1- ADMINISTRADOR\n2- CLIENTE INDIVIDUO\n3- CLIENTE PYME")
        opc = input("Opción: ")
        intento = 2
        #BUCLE INFINITO PARA MENU
        while intento >0: #PERMITE 2 INTENTOS, SI SON ERRONEOS SALE DEL MENÚ
            if opc == "1":
                usuario = input("Ingrese el usuario: ") or ("administrador")#VALIDA EL USUARIO
                password = input("Ingrese la contraseña: ") or ("adm1n1str4d0r")#VALIDA EL PASSWORD
                if usuario == self.adm_usuario and password == self.adm_password:
                    print("\nHa ingresado como administrador\n")
                    self.menu_administrador()
                else:
                    print("Usuario o contraseña incorrecto")
                    print("Ingreselo nuevamente")
                    intento-=1
                    if intento ==0:
                        self.loguin()
            elif opc == "2":
                usuario = input("Ingrese el usuario: ") or ("us1")#VALIDA EL USUARIO
                password = input("Ingrese la contraseña: ") or ("pass1")#VALIDA EL PASSWORD
                if usuario in self.clientes_usuarios:
                    if password == self.clientes_usuarios[usuario].password:
                        us = self.clientes_usuarios.get(usuario)
                        print("\nHa ingresado como individuo\n")
                        self.cliente_log = us
                        self.menu_individuos()
                else:
                    print("Usuario o contraseña incorrecto")
                    print("Ingreselo nuevamente")
                    intento-=1
                    if intento ==0:
                        self.loguin()
            elif opc == "3":
                usuario = input("Ingrese el usuario: ") or ("py3")#VALIDA EL USUARIO
                password = input("Ingrese la contraseña: ") or ("pass3")#VALIDA EL PASSWORD
                if usuario in self.clientes_pymes:
                    if password == self.clientes_pymes[usuario].password:
                        us = self.clientes_pymes.get(usuario)
                        print("\nHa ingresado como Pyme\n")
                        self.cliente_log = us
                        self.menu_pyme()
                else:
                    print("Usuario o contraseña incorrecto")
                    print("Ingreselo nuevamente")
                    intento-=1
                    if intento ==0:
                        self.loguin()
            else:
                print("OPCION INVÁLIDA\nINGRESE UNA OPCION VALIDA")
                self.loguin()

    #MENU_ADMINISTRADOR
    def menu_administrador(self):
        loguin = True
        while loguin == True:
            print("BIENVENIDO ADMINISTRADOR\n", "QUÉ DESEA HACER?")
            print("****MENÚ DE ADMINISTRADOR****\n","0- LISTAR SUCURSALES\n", "1- AGREGAR SUCURSAL\n", "2- LISTAR COSTOS MANTENIMIENTO\n", "3- MODIFICAR COSTOS MANTENIMIENTO\n", "4- ALTA NUEVO CLIENTE\n","5- LISTAR CLIENTES\n","6- BUSCAR CLIENTE\n", "7- MOVIMIENTOS\n", "8- MODIFICAR DATOS CLIENTE\n","9- LISTADO DE CUENTAS\n","10- SALDOS\n", "11- LISTAR PLAZOS FIJOS\n", "S- SALIR DEL MENU ADMINISTRADOR")
            op = True
            while op == True:
                opc_adm = input("Ingrese opción: ")
                if opc_adm == "0":
                    print("Estas son las sucursales del banco")
                    self.listar_sucursales() #1358

                elif opc_adm == "1":
                    print("Agregar nueva sucursal")
                    self.agregar_sucursal() #1366
                    
                elif opc_adm == "2":
                    print("Costos de mantenimiento")
                    self.listar_costos_mant()
                    print("Intereses mensuales plazo fijo:\n\t 30 DIAS = ", self.costos_mantenim[14][1], " %\n\t 60 DIAS = ", self.costos_mantenim[14][2], " %\n\t 90 DIAS = ", self.costos_mantenim[14][3], " %\n\t180 DIAS = ", self.costos_mantenim[14][4], " % \n\t360 DIAS = ", self.costos_mantenim[14][5], " %")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_administrador()

                elif opc_adm == "3":
                    for cos in self.costos_mantenim:
                        print("""\t {} => {}  Monto actual: $ {}""".format(cos,self.costos_mantenim[cos][0], self.costos_mantenim[cos][1]))
                    print("Intereses mensuales plazo fijo:\n\t 30 DIAS = ", self.costos_mantenim[14][1], " %\n\t 60 DIAS = ", self.costos_mantenim[14][2], " %\n\t 90 DIAS = ", self.costos_mantenim[14][3], " %\n\t180 DIAS = ", self.costos_mantenim[14][4], " % \n\t360 DIAS = ", self.costos_mantenim[14][5], " %")
                    while True:
                        print("Ingrese el id del costo a modificar")
                        while True:
                            op = input("Ingrese un número entre 1 y 20: ")
                            try:
                                op = int(op)
                                if  op >0 and op <20:
                                    break
                            except ValueError:
                                print("DEBE INGRESAR UN N° ENTRE 1 Y 20")
                        if op == 14:
                            self.modif_int_pla_fijo()
                        else:
                            self.modif_costos(op)
                        print("""Si desea modificar otro costo presione "Y"\n o cualquier tecla para volver al menú""")
                        op = input(" ")
                        op = op.upper()
                        if op == "Y":
                            True  
                        else:
                            self.menu_administrador()
    
                elif opc_adm == "4":
                    print("****CARGAR NUEVO CLIENTE****")
                    cli = input("1- CLIENTE INDIVIDUO\n2- CLIENTE PYME\n3- SALIR\nIngrese opción: ")
                    if cli == "1":
                        self.alta_cli_indiv()
                        op = False
                    elif cli =="2":
                        self.alta_cli_pymes()
                        op = False
                    elif cli =="3":
                        self.menu_administrador()
                    else:
                        print("OPCION INCORRECTA")
                        
                elif opc_adm == "5":
                    print("LISTAR CLIENTES\n1- CLIENTES INDIVIDUO\n2- CLIENTES PYMES\n3- SALIR")
                    clien = input("Ingrese opción: ")
                    if clien == "1":
                        print("Lista de clientes")
                        self.listar_cli_ind()
                    elif clien == "2":
                        self.listar_pymes()
                    elif clien =="3":
                        self.menu_administrador()
                    else:
                        print("OPCION INCORRECTA")
                        opc_adm == "5"
                
                elif opc_adm == "6":
                    while opc_adm == "6":
                        busqueda = input("1- BUSCAR POR D.N.I.\n2- BUSCAR POR USUARIO\n3- VOLVER\n")
                        if busqueda == "1":
                            while True:
                                dni = input("Ingrese el D.N.I. a buscar: ")
                                try:
                                    dni = int(dni)
                                    break
                                except ValueError:
                                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                            self.buscar_cliente_dni(dni)
                        elif busqueda == "2":
                            cliente = input("¿Qué cliente desea buscar?: ")
                            self.buscar_cliente(cliente)
                        elif busqueda == "3":
                            self.menu_administrador()
                        else:
                            print("OPCION INCORRECTA")
                            opc_adm = "6"

                elif opc_adm == "7":
                    self.movimientos()

                elif opc_adm == "8":
                    print("Eligió la opción para modificar datos de un cliente")
                    op = True
                    while op == True:
                        cli = input("TIPO DE CLIENTE\n1- Cliente individuo\n2- Cliente Pymes\n3- Salir\nIngrese opción: ")
                        if cli == "1":
                            self.modif_datos_cliente()
                        elif cli == "2":
                            self.modif_datos_cliente_pymes()
                        elif cli == "3":
                            self.menu_administrador()
                        else:
                            print("OPCION INCORRECTA")
                            op = True

                elif opc_adm == "9":
                    self.listar_cuentas()
                    self.menu_administrador()

                elif opc_adm == "10":
                    self.saldos()
                    op = False

                elif opc_adm == "11":
                    self.listar_plazos_fijos()
                    self.menu_administrador()

                elif opc_adm == "S" or opc_adm == "s":
                    self.loguin()

                else:
                    print("OPCION INCORRECTA")
                    self.menu_administrador()
                    op = False

    def movimientos(self):
        op = True
        while op == True:
            opcion = input("MENU DE MOVIMIENTOS\n1- MOVIMIENTOS DE TODAS LAS CUENTAS DEL BANCO\n2- MOVIMIENTOS DE UNA CUENTA\n3- VOLVER AL MENU ANTERIOR\nIngrese la opción ")
            if opcion == "1":
                for cu in self.movimientos_cuentas:
                    mov = self.movimientos_cuentas.get(cu) 
                    print("Movimientos de la cuenta N° ", cu)
                    print("\n\t", mov)
                op = True
            elif opcion == "2":
                cli = input("TIPO DE CLIENTE\n1- INDIVIDUO\n2- PYMES\n3- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                opc = True
                while opc == True:
                    if cli == "1":
                        for cli in self.clientes_usuarios:
                            cliente = self.clientes_usuarios.get(cli)
                            print("Cliente: \n\t", cliente.apellido, "", cliente.nombre, "\n\tD.N.I.:", cliente.dni, "\n\tNombre de usuario: ", cliente.nombre_us)
                        tit = input("Ingrese el nombre de usuario del cliente: ")
                        for cli in self.clientes_usuarios:
                            cliente = self.clientes_usuarios.get(cli)
                            if cliente.nombre_us == tit:
                                for cu in self.cuenta:
                                    cuenta = self.cuenta.get(cu)
                                    if cuenta.titular == tit:
                                        print("Cuenta n°",cuenta.num_cuenta)
                                while True:
                                    cuenta_a_buscar = input("Ingrese el n° de cuenta para ver sus movimientos: ")
                                    try:
                                        cuenta_a_buscar = int(cuenta_a_buscar)
                                        break
                                    except ValueError:
                                        print("DEBE INGRESAR UN NUMERO, SIN PUNTOS")
                                c = cuenta_a_buscar in self.movimientos_cuentas
                                if c:
                                    for cu in self.movimientos_cuentas:
                                        if cu == cuenta_a_buscar:
                                            mov = self.movimientos_cuentas.get(cu)
                                            print("Movimientos de la cuenta N° ", cuenta_a_buscar)
                                            print("\n\t", mov)
                                            input("Presione cualquier tecla para continuar ")
                                    self.movimientos()
                                else:
                                    print("La cuenta n° ", cuenta_a_buscar, " no exite o no pertenece al cliente ", cliente.apellido, cliente.nombre)
                                    self.movimientos()
                        print("\nEl cliente ", tit, " NO EXISTE O NO POSEE CUENTAS\n")
                        self.movimientos()
                    elif cli == "2":
                        for cli in self.clientes_pymes:
                            cliente = self.clientes_pymes.get(cli)
                            print("Cliente: \n\t", cliente.razon_social, "\n\tNombre de usuario: ", cliente.nombre_us)
                        tit = input("Ingrese el nombre de usuario del cliente: ")
                        for cli in self.clientes_pymes:
                            cliente = self.clientes_pymes.get(cli)
                            if cliente.nombre_us == tit:
                                for cu in self.cuenta:
                                    cuenta = self.cuenta.get(cu)
                                    if cuenta.titular == tit:
                                        print("Cuenta n°",cuenta.num_cuenta)
                                while True:
                                    cuenta_a_buscar = input("Ingrese el n° de cuenta para ver sus movimientos: ")
                                    try:
                                        cuenta_a_buscar = int(cuenta_a_buscar)
                                        break
                                    except ValueError:
                                        print("DEBE INGRESAR UN NUMERO, SIN PUNTOS")
                                c = cuenta_a_buscar in self.movimientos_cuentas
                                if c:
                                    for cu in self.movimientos_cuentas:
                                        if cu == cuenta_a_buscar:
                                            mov = self.movimientos_cuentas.get(cu)
                                            print("Movimientos de la cuenta N° ", cuenta_a_buscar)
                                            print("\n\t", mov)
                                            input("Presione cualquier tecla para continuar ")
                                    self.movimientos()
                                else:
                                    print("La cuenta n° ", cuenta_a_buscar, " no exite o no pertenece al cliente ", cliente.razon_social)
                                    self.movimientos()
                        print("\nEl cliente ", tit, " NO EXISTE O NO POSEE CUENTAS\n")
                        self.movimientos()
                    elif cli == "3":
                        self.menu_administrador()
                    else:
                        print("OPCIÓN INCORRECTA")
                        opc = True
            elif opcion == "3":
                self.menu_administrador()
            else:
                print("OPCIÓN INCORRECTA")
                op = True

    def listar_plazos_fijos(self): #LISTAR_PLAZOS_FIJOS
        print("Lista de plazos fijos")
        for cu in self.dic_plazo_fijo:
            print(self.dic_plazo_fijo[cu].__str__())
        input("Presione cualquier tecla para continuar")

    def menu_individuos(self):
        loguin = True
        while loguin == True:
            print("BIENVENIDO ",self.cliente_log.apellido, " ", self.cliente_log.nombre,"\nELIJA UNA OPCION\n")
            print("****MENÚ DE INDIVIDUO*****\n1- CREAR UNA NUEVA CUENTA\n2- REALIZAR UN DEPOSITO\n3- REALIZAR UNA TRANSFERENCIA\n4- REALIZAR UN PAGO EN LINEA\n5- LISTAR CUENTAS\n6- MOVIMIENTOS\n7- REALIZAR UN RETIRO\n8- LISTAR SALDO DE MIS CUENTAS\n9- CERRAR CUENTA\nS- SALIR")
            opc_ind = input("Ingrese opción: ")               
            if opc_ind == "1":
                self.crear_cuenta()
            elif opc_ind == "2":
                self.deposito()
            elif opc_ind == "3":
                self.transferencia_indiv()
            elif opc_ind == "4":
                self.pago_en_linea_indiv()
            elif opc_ind == "5":
                self.listar_cuentas_propias(self.cliente_log.nombre_us)
            elif opc_ind == "6":
                self.movimientos_mi_cuenta_ind()
            elif opc_ind == "7":
                self.extraccion()
            elif opc_ind == "8":
                self.mis_saldos(self.cliente_log.nombre_us)
            elif opc_ind == "9":
                self.cerrar_cuenta_individuo(self.cliente_log.nombre_us)
            elif opc_ind == "s" or opc_ind == "S":
                self.loguin()
            else:
                print("INGRESÓ UNA OPCIÓN INCORRECTA")
                self.menu_individuos()
                
    def menu_pyme (self):
        loguin = True
        while loguin == True:
            print("****Menú pymes****")
            print("BIENVENIDO PYMES: ",self.cliente_log.razon_social,"\nELIJA UNA OPCION\n")
            print("0- ABRIR UNA CUENTA\n1- LISTAR MIS CUENTA\n2- REALIZAR UN DEPOSITO\n3- HACER UNA TRANSFERENCIA\n4- REALIZAR UN PAGO EN LINEA\n5- PLAZO FIJO\n6- COMPRAR  MONEDA EXTRANJERA\n7- INVERTIR EN BONOS\n8- PAGAR SUELDOS\n9- LISTAR SALDO DE MIS CUENTAS\n10- MOVIMIENTOS\n11- CERRAR CUENTA\nS- SALIR")
            op = input("Ingrese opción: ")
            if op == "0":
                self.crear_cuenta_pymes()
            elif op == "1":
                self.listar_cuentas_propias(self.cliente_log.nombre_us)
            elif op == "2":
                self.deposito()
            elif op == "3":
                self.transferencia_pyme()
            elif op == "4":
                self.pago_en_linea_pyme()
            elif op == "5":
                self.plazo_fijo()
            elif op == "6":
                self.comprar_mon_ext()
            elif op == "7":
                self.bonos()
            elif op == "8":
                self.pagar_sueldos()
            elif op == "9":
                 self.mis_saldos(self.cliente_log.nombre_us)
            elif op == "10":
                self.movimientos_mi_cuenta_pyme()
            elif op == "11":
                self.cerrar_cuenta_pyme(self.cliente_log.nombre_us)
            elif op == "s" or op == "S":
                self.loguin()
            else:
                print("OPCIÓN INCORRECTA")
                self.menu_pyme()

    def movimientos_mi_cuenta_ind(self): #MOVIMIENTOS_CUENTA_INDIVIDUOS
        for cli in self.clientes_usuarios:
            cliente = self.clientes_usuarios.get(cli)
            if cliente.nombre_us == self.cliente_log.nombre_us:
                for cu in self.cuenta:
                    cuenta = self.cuenta.get(cu)
                    if cuenta.titular == self.cliente_log.nombre_us:
                        print("Cuenta n°",cuenta.num_cuenta)
                while True:
                    cuenta_a_buscar = input("Ingrese el n° de cuenta para ver sus movimientos: ")
                    try:
                        cuenta_a_buscar = int(cuenta_a_buscar)
                        break
                    except ValueError:
                        print("DEBE INGRESAR UN NUMERO, SIN PUNTOS")
                c = cuenta_a_buscar in self.movimientos_cuentas
                if c:
                    for cu in self.movimientos_cuentas:
                        if cu == cuenta_a_buscar:
                            mov = self.movimientos_cuentas.get(cu)
                            print("Movimientos de la cuenta N° ", cuenta_a_buscar)
                            print("\n\t", mov)
                            input("Presione cualquier tecla para continuar ")
                            self.menu_individuos()
                    self.movimientos_mi_cuenta_ind()
                else:
                    print("La cuenta n° ", cuenta_a_buscar, " no me pertenece")
                    otra = True
                    while otra == True:
                        int_otra = input("1- Intentar con otra cuenta\n2- volver\nIngrese la opción: ")
                        if int_otra == "1":
                            self.movimientos_mi_cuenta_ind()
                        elif int_otra == "2":
                            self.menu_individuos()
                        else:
                            print("OPCION INCORRECTA")
                            otra = True

    def movimientos_mi_cuenta_pyme(self):#MOVIMIENTOS_CUENTAS_PYME
        for cli in self.clientes_pymes:
            cliente = self.clientes_pymes.get(cli)
            if cliente.nombre_us == self.cliente_log.nombre_us:
                for cu in self.cuenta:
                    cuenta = self.cuenta.get(cu)
                    if cuenta.titular == self.cliente_log.nombre_us:
                        print("Cuenta n°",cuenta.num_cuenta)
                while True:
                    cuenta_a_buscar = input("Ingrese el n° de cuenta para ver sus movimientos: ")
                    try:
                        cuenta_a_buscar = int(cuenta_a_buscar)
                        break
                    except ValueError:
                        print("DEBE INGRESAR UN NUMERO, SIN PUNTOS")
                c = cuenta_a_buscar in self.movimientos_cuentas
                if c:
                    for cu in self.movimientos_cuentas:
                        if cu == cuenta_a_buscar:
                            mov = self.movimientos_cuentas.get(cu)
                            print("Movimientos de la cuenta N° ", cuenta_a_buscar)
                            print("\n\t", mov)
                            input("Presione cualquier tecla para continuar ")
                            self.menu_pyme()
                    self.movimientos_mi_cuenta_pyme()
                else:
                    print("La cuenta n° ", cuenta_a_buscar, " no me pertenece")
                    otra = True
                    while otra == True:
                        int_otra = input("1- Intentar con otra cuenta\n2- volver\nIngrese la opción: ")
                        if int_otra == "1":
                            self.movimientos_mi_cuenta_pyme()
                        elif int_otra == "2":
                            self.menu_pyme()
                        else:
                            print("OPCION INCORRECTA")
                            otra = True

    def pagar_sueldos(self): 
        print("****MENÚ SUELDOS****\n1- AGREGAR EMPLEADO\n2- LISTAR EMPLEADOS\n3- MODIFICAR DATOS EMPLEADOS\n4- LISTAR SUELDOS A PAGAR\n5- PAGAR SUELDOS\nS- SALIR")
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            self.agregar_empleado()
        elif opcion == "2":
            self.listar_empleados(self.cliente_log.razon_social)
        elif opcion == "3":
            self.modif_datos_empl()
        elif opcion == "4":
            self.listar_sueldos(self.cliente_log.razon_social)
        elif opcion == "5":
            self.liq_sueldos(self.cliente_log.razon_social)
        elif opcion == "s" or opcion == "S":
            self.menu_pyme()
        else:
            print("OPCIÓN INCORRECTA")
            input("Presione cualquier tecla para continuar ")
            self.pagar_sueldos()
        
    def agregar_empleado(self):
        otro_emp = True
        while otro_emp == True:
            print("INGRESE LOS DATOS DEL NUEVO EMPLEADO")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = Secuencia.next_nro_dni()
            print("D.N.I.: ", dni)
            banco = input("Es cliente del banco: Y/N ")
            if banco == "y" or banco == "Y":
                banco = "Brulim"
            elif banco == "n" or banco == "N":
                banco =  input("Ingrese el nombre del banco al que pertenece: ")
            else:
                print("OPCION INCORRECTA")
                self.agregar_empleado()
            puesto = input("Puesto: ")
            empresa = self.cliente_log.razon_social
            while True:
                salario = input("Sueldo: $ ")
                try:
                    salario = int(salario)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            sueldo = str(salario)
            empleado = Empleado(nombre, apellido, dni, banco, puesto, empresa, sueldo, salario)
            self.sueldos_pymes[dni] = empleado
            otro = input("1- AGREGAR OTRO EMPLEADO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
            if otro == "1":
                otro_emp = True
            elif otro == "2":
                self.pagar_sueldos()
            else:
                print("OPCION INCORRECTA")
                otro_emp = False

    def listar_empleados(self, tit):
        print("LISTA DE EMPLEADOS DE ", tit)
        lista = True
        if lista:
            for emp in self.sueldos_pymes:
                employee = self.sueldos_pymes.get(emp)
                if employee.empresa == tit:
                    print(employee)
                else:
                    pass
            lista = False
            input("Presione cualquier tecla para continuar ")
            self.pagar_sueldos()

    def modif_datos_empl(self): #MODIFICAR_DATOS_EMPLEADOR
        print("Menú para modificar datos de un empleado")
        while True:
            dni_empl = input("Ingrese el D.N.I.: ")
            try:
                dni_empl = int(dni_empl)
                break
            except ValueError:
                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
        print("****MENU PARA MODIFICAR DATOS DE CLIENTE PYMES****")
        existe = dni_empl in self.sueldos_pymes
        if existe:
            for emp in self.sueldos_pymes:
                empleado_a_modif = self.sueldos_pymes.get(emp)
                if empleado_a_modif.dni == dni_empl:
                    print("Datos del empleado:\n\t ", empleado_a_modif.apellido, " ", empleado_a_modif.nombre)
                    print("--OPCIONES PARA MODIFICAR--")
                    while True:
                        opcion = input("1- BANCO\n2- PUESTO\n3- SUELDO\nS- VOLVER AL MENU ANTERIOR\n Ingrese opción ")
                        if opcion == "1":
                            banco = input("Ingrese el nuevo banco: ")
                            empleado_a_modif.banco = banco
                            otro = input("MODIFICAR OTRO DATO Y/N\n Ingrese opción ")
                            op = True
                            while op == True:
                                if otro == "y" or otro == "Y":
                                    op = False
                                elif otro == "n" or otro == "N":
                                    self.pagar_sueldos()
                        elif opcion == "2":
                            puesto = input("Ingrese el nuevo puesto: ")
                            empleado_a_modif.puesto = puesto
                            op = True
                            while op == True:
                                otro = input("MODIFICAR OTRO DATO Y/N\n Ingrese opción ")
                                if otro == "y" or otro == "Y":
                                    op = False
                                elif otro == "n" or otro == "N":
                                    self.pagar_sueldos()
                                else:
                                    print("OPCION INCORRECTA")
                                    op = True
                        elif opcion == "3":
                            while True:
                                sueldo = input("Ingrese el nuevo sueldo: $ ")
                                try:
                                    sueldo = int(sueldo)
                                    break
                                except ValueError:
                                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                            empleado_a_modif.sueldo = sueldo
                            op = True
                            while op == True:
                                otro = input("MODIFICAR OTRO DATO Y/N\n Ingrese opción ")
                                if otro == "y" or otro == "Y":
                                    op = False
                                elif otro == "n" or otro == "N":
                                    self.pagar_sueldos()
                                else:
                                    print("OPCION INCORRECTA")
                                    op = True
                        elif opcion == "s" or opcion == "S":
                            self.pagar_sueldos()
                        else:
                            print("OPCION INCORRECTA")
                            True
        else:
            print("NO EXISTE EL EMPLEADO CON EL D.N.I. ", dni_empl)
            input("Presione cualquier tecla para continuar ")
            self.pagar_sueldos()

    def listar_sueldos(self, tit):
        print("LISTA DE EMPLEADOS y SUELDOS A LIQUIDAR DE ", tit)
        lista = True
        if lista:
            for emp in self.sueldos_pymes:
                employee = self.sueldos_pymes.get(emp)
                if employee.empresa == tit:
                    print(employee.apellido + " " + employee.nombre + ": \n\t" + "\n\tBanco: " + str(employee.banco) +" Sueldo: $ " + employee.sueldo)
                else:
                    pass
            lista = False
            input("Presione cualquier tecla para continuar")
            self.pagar_sueldos()

    def liq_sueldos(self, tit): #LIQUIDAR_SUELDOS
        print("SE VAN A LIQUIDAR LOS SUELDOS DE SUS EMPLEADOS: ")
        print("ELIJA UNA CUENTA DE DONDE DEBITAR LOS SUELDOS")
        self.mis_saldos(self.cliente_log.nombre_us)
        lista = True
        while lista == True:
            while True:
                cuenta_a_debitar = input("Ingrese el n° de cuenta: ")
                try:
                    cuenta_a_debitar = int(cuenta_a_debitar)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            cue = cuenta_a_debitar in self.cuenta
            if cue:
                if lista:
                    tot_comision = 0
                    total = 0
                    for emp in self.sueldos_pymes:
                        employee = self.sueldos_pymes.get(emp)
                        if employee.empresa == tit:
                            total = total + employee.salario
                            if employee.banco == "Brulim":
                                tot_comision += self.costos_mantenim[19][1]
                            else:
                                tot_comision += self.costos_mantenim[20][1]
                        else:
                            pass
                    lista = False
                if self.cuenta[cuenta_a_debitar].titular == self.cliente_log.nombre_us:
                    print("Se va a debitar el total de $ ", total + tot_comision, " de su cuenta n° ", cuenta_a_debitar)
                    acepta = input("Acepta? Y/N ")
                    if acepta == "y" or acepta == "Y":
                        monto=True
                        while monto == True:
                            c= cuenta_a_debitar in self.cuenta
                            if c:
                                self.cuenta[cuenta_a_debitar].saldo -=  total + tot_comision
                                suel = datetime.now()
                                self.movimientos_cuentas[cuenta_a_debitar]["Día ", suel.year, suel.month, suel.day, "Hora ", suel.hour, suel.minute, suel.second] = ("PAGO DE SUELDOS POR $ " + str(total + tot_comision))
                                print("El saldo actual de la cuenta n° " + str(cuenta_a_debitar) + " es $ ", str(self.cuenta[cuenta_a_debitar].saldo))
                                input("Presione cualquier tecla para continuar ")
                                monto = False 
                            else:
                                print("LA CUENTA N° ", cuenta_a_debitar, " NO EXISTE")
                                o = True
                                while o == True:
                                    otra = input("1- Intentar con otra cuenta\n2- Salir\nIngrese opción: ")
                                    if otra == "1":
                                        o = False
                                        monto = False
                                        lista = True
                                    elif otra == "2":
                                        o = False
                                        self.pagar_sueldos()
                                    else:
                                        print("OPCION INCORRECTA")
                                        o = True
                    else:
                        print("La cuenta n° ", cuenta_a_debitar, " no le pertenece.")
                        input("Presione cualquier tecla para continuar")
                        self.pagar_sueldos()
                else:
                    lista = False
                    self.pagar_sueldos()
            else:
                print("La cuenta n° ", cuenta_a_debitar, " no existe")
                input("Presione cualquier tecla para continuar")
                self.menu_pyme()

    def alta_cli_pymes(self): #ALTA_CLIENTE_PYMES
        print("Cargar un cliente Pyme")
        razon_social = input("Razón social: ")
        domicilio = input("Domicilio: ")
        num = Secuencia.next_nro_dni()
        cuit = rd.randint(20,30)
        guion= rd.randint(0,9)
        cuitCuil = cuit,"-",num,"-",guion
        print("Cuit/Cuil: ",cuit,"-",num,"-",guion)
        telefono = rd.randint(5550000,5559999)
        print("Teléfono: ",telefono)
        email = input("Email: ")
        disponible = True
        while disponible == True:
            nombre_us = input("Nombre de usuario: ")
            disponible = nombre_us in self.clientes_pymes
            if disponible == False:
                password = input("Password: ")
            else:
                print("Nombre de usuario no disponible.\nEscoja otro")
                disponible = True
        py_nueva = Pymes(razon_social, domicilio, cuitCuil, telefono, email, nombre_us, password)
        self.clientes_pymes[nombre_us] = py_nueva

    def alta_cli_indiv(self): #ALTA_CLIENTE_INDIVIDUO
        print("Cargar un cliente Individuo")
        nombre = input("Nombre: ")
        apellido = input("Apellido :")
        domicilio = input("Domicilio: ")
        dni = Secuencia.next_nro_dni()
        print("D.N.I.: ",dni)
        cuit = rd.randint(20,30)
        guion= rd.randint(0,9)
        cuitCuil = cuit,"-",dni,"-",guion
        print("Cuit/Cuil: ",cuit,"-",dni,"-",guion)
        telefono = rd.randint(5550000,5559999)
        print("Teléfono: ",telefono)
        email = input("Email: ")
        disponible = True
        while disponible == True:
            nombre_us = input("Nombre de usuario: ")
            disponible = nombre_us in self.clientes_usuarios
            if disponible == False:
                password = input("Password: ")
            else:
                disponible = True
                print("Nombre de usuario no disponible.\nEscoja otro")
        cli_nuevo = Individuos(nombre, apellido, domicilio, dni, cuitCuil, telefono, email, nombre_us, password)
        self.clientes_usuarios[nombre_us] = cli_nuevo
        self.clientes_dni[dni] = cli_nuevo

    def modif_datos_cliente(self): #MODIFICAR_DATOS-CLIENTE
        print("****MENU PARA MODIFICAR DATOS DE CLIENTE INDIVIDUO****")
        while True:
            dni = input("Ingrese el D.N.I. del cliente: ")
            try:
                dni = int(dni)
                break
            except ValueError:
                print("DEBE INGRESAR NÚMEROS, SIN PUNTOS")
        existe = dni in self.clientes_dni
        if existe:
            modificar = True
            while modificar == True:
                print("Cliente ", self.clientes_dni[dni].apellido, " ",self.clientes_dni[dni].nombre)
                print("Datos actuales:\n\tTeléfono: ", self.clientes_dni[dni].telefono,"\n\tEmail: ", self.clientes_dni[dni].email, "\n\tDomicilio: ", self.clientes_dni[dni].domicilio)
                dato = input("1- Modificar teléfono\n2- Modificar Email\n3- Modificar domicilio\n4- Salir\n OPCION: ")
                if dato == "1":
                    while True:
                        tel = input("Ingrese el nuevo teléfono: ")
                        try:
                            tel = int(tel)
                            break
                        except ValueError:
                            print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                    self.clientes_dni[dni].telefono = tel
                    print("Modificación exitosa")
                    print("Tel: ", self.clientes_dni[dni].telefono)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "2":
                    mail = input("Nuevo email: ")
                    self.clientes_dni[dni].email = mail
                    print("Modificación exitosa")
                    print("Mail: ", self.clientes_dni[dni].email)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "3":
                    dom = input("Nuevo domicilio: ")
                    self.clientes_dni[dni].domicilio = dom
                    print("Modificación exitosa")
                    print("Domicilio: ", self.clientes_dni[dni].domicilio)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "4":
                    self.menu_administrador()
                else:
                    print("OPCION INCORRECTA")
                    modificar = True
        else:
            print("El cliente con D.N.I. no existe\n1- Intentar con otro D.N.I.\n2- Salir")
            otro = input("\nIngrese opción: ")
            opcion = True
            while opcion == True:
                if otro == "1":
                    self.modif_datos_cliente()
                elif otro == "2":
                    self.menu_administrador()
                else:
                    opcion = False

    def modif_datos_cliente_pymes(self): #MODIFICAR_DATOS-PYMES
        nom_pyme = input("Ingrese el nombre de usuario de la pymes: ")
        print("****MENU PARA MODIFICAR DATOS DE CLIENTE PYMES****")
        existe = nom_pyme in self.clientes_pymes
        if existe:
            modificar = True
            while modificar == True:
                print("Cliente Pymes ", self.clientes_pymes[nom_pyme].razon_social)
                print("Datos actuales:\n\tTeléfono: ", self.clientes_pymes[nom_pyme].telefono,"\n\tEmail: ", self.clientes_pymes[nom_pyme].email, "\n\tDomicilio: ", self.clientes_pymes[nom_pyme].domicilio)
                dato = input("1- Modificar teléfono\n2- Modificar Email\n3- Modificar domicilio\n4- Salir\nIngrese opción: : ")
                if dato == "1":
                    while True:
                        tel = input("Ingrese el nuevo teléfono: ")
                        try:
                            tel = int(tel)
                            break
                        except ValueError:
                            print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                    self.clientes_pymes[nom_pyme].telefono = tel
                    print("Modificación exitosa")
                    print("Tel: ", self.clientes_pymes[nom_pyme].telefono)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "2":
                    mail = input("Nuevo email: ")
                    self.clientes_pymes[nom_pyme].email = mail
                    print("Modificación exitosa")
                    print("Mail: ", self.clientes_pymes[nom_pyme].email)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "3":
                    dom = input("Nuevo domicilio: ")
                    self.clientes_pymes[nom_pyme].domicilio = dom
                    print("Modificación exitosa")
                    print("Domicilio: ", self.clientes_pymes[nom_pyme].domicilio)
                    otro = input("1- Modificar otro dato\n2- Volver\nIngrese opción: ")
                    if otro == "1":
                        modificar = True
                    else:
                        self.menu_administrador()
                elif dato == "4":
                    self.menu_administrador()
                else:
                    print("OPCION INCORRECTA")
                    modificar = True
        else:
            print("La pymes ",  nom_pyme, " no existe\n1- Intentar con otro nombre\n2- Salir")
            otro = input("\nIngrese opción: ")
            opcion = True
            while opcion == True:
                if otro == "1":
                    self.modif_datos_cliente_pymes()
                elif otro == "2":
                    self.menu_administrador()
                else:
                    opcion = False

    def saldos (self): #MENU_SALDOS
        print("****MENU SALDOS****")
        print("Ver el saldo de: ")
        opcion = input("1- TODAS LAS CUENTAS\n2- CAJA AHORRO COMÚN\n3- CAJA AHORRO CON SALDO RETENIDO\n4- CUENTA CORRIENTE COMÚN\n5- CUENTA CORRIENTE CON SALDO RETENIDO\n6- CUENTAS CORRIENTE CON SALDO DEUDOR\n7- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
        if opcion == "1":
            tipo = None
            print("Lista de todas las cuentas del banco")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "1":
                    tipo = "Caja Ahorro Común"
                elif self.cuenta[cu].tipo == "2":
                    tipo ="Caja Ahorro Saldo Ret."
                elif self.cuenta[cu].tipo == "3":
                    tipo = "Cuenta Corriente Común"
                elif self.cuenta[cu].tipo == "3":
                    tipo = "Cuenta Corriente Saldo Ret."
                print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
            input("Presione cualquier tecla para continuar ")
            self.saldos()
        elif opcion == "2":
            print("Lista de las cuentas del tipo Caja Ahorro Común")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "1":
                    tipo = "Caja Ahorro Común"
                    print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
                else:
                    pass
            input("Presione cualquier tecla para continuar ")
            self.saldos()
        elif opcion =="3":
            print("Lista de las cuentas del tipo Caja Ahorro con Retención de Saldo")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "2":
                    tipo = "Caja Ahorro Saldo Ret."
                    print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
                else:
                    pass
            input("Presione cualquier tecla para continuar ")
            self.saldos()
        elif opcion == "4":
            print("Lista de las cuentas del tipo Cuenta Corriente Común")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "3":
                    tipo = "Cuenta Corriente Común"
                    print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
                else:
                    pass
            input("Presione cualquier tecla para continuar")
            self.saldos()
        elif opcion == "5":
            print("Lista de las cuentas del tipo Cuenta Corriente con Retención de Saldo")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "4":
                    tipo = "Cuenta Corriente Saldo Ret."
                    print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
                else:
                    pass
            input("Presione cualquier tecla para continuar")
            self.saldos()
        elif opcion == "6":
            print("Lista de las cuentas con Saldo Deudor")
            for cu in self.cuenta:
                if self.cuenta[cu].tipo == "3" or self.cuenta[cu].tipo == "4":
                    if self.cuenta[cu].tipo == "3":
                        tipo = "Cuenta Corriente Común"
                    elif self.cuenta[cu].tipo == "4":
                        tipo = "Cuenta Corriente Saldo Ret."
                    if self.cuenta[cu].saldo < 0:
                        print("Cuenta n° ",self.cuenta[cu].num_cuenta," ", tipo, " saldo $ ", self.cuenta[cu].saldo)
                else:
                    pass
            input("Presione cualquier tecla para continuar ")
            self.saldos()
        elif opcion == "7":
            self.menu_administrador()
        else:
            print("OPCION INCORRECTA")
            self.saldos()

    def buscar_cliente(self, cliente): #BUSCAR_CLIENTES
        a = cliente in self.clientes_pymes
        if a:
            print("\nCLIENTE ", cliente, "\n", self.clientes_pymes[cliente],"\n")
            input("Presione cualquier tecla para continuar ")
        elif a == False:
            a = cliente in self.clientes_usuarios
            if a:
                print("\nCLIENTE ", cliente, " ENCONTRADO\n\n", self.clientes_usuarios[cliente],"\n")
                input("Presione cualquier tecla para continuar ")
            else:
                print("\nEL CLIENTE ",cliente," NO EXISTE\n")

    def buscar_cliente_dni(self, dni): #BUSCAR_DNI
        a = dni in self.clientes_dni
        if a:
            print("\nEL CLIENTE CON DNI ", dni, "ES:\n", self.clientes_dni[dni],"\n")
            input("Presione cualquier tecla para continuar ")
        else:
            print("\nEL CLIENTE CON DNI ",dni," NO EXISTE\n")

    def deposito(self): #DEPOSITO_CUENTA
        while True:
            dep = input("Monto a depositar: $ ")
            cta = input("N° de cuenta destino: ")
            try:
                dep = int(dep)
                cta = int(cta)
                break
            except ValueError:
                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
        tipo = self.cuenta[cta].tipo
        if tipo == "1":
            costo = self.costos_mantenim[15][1]
        elif tipo == "2":
            costo = self.costos_mantenim[16][1]
        elif tipo == "3":
            costo = self.costos_mantenim[17][1]
        elif tipo == "4":
            costo = self.costos_mantenim[18][1]
        c = cta in self.cuenta
        if c:
            self.cuenta[cta].saldo +=  dep - costo
        depo = datetime.now()
        self.movimientos_cuentas[cta]["Día ", depo.year, depo.month, depo.day, "Hora ", depo.hour, depo.minute, depo.second] = ("REALIZO UN DEPOSITO POR $ " + str(dep))

    def transferencia_indiv(self): #TRANSFERENCIA_INDIVIDUO
        print("****REALIZAR UNA TRANSFERENCIA****")
        monto = True
        while monto == True:
            while True:
                origen = input("Ingrese n° de cuenta origen: ")
                importe = input("Monto a transferir: ")
                destino = input("Ingrese n° de cuenta destino: ")
                try:
                    origen = int(origen)
                    importe = int(importe)
                    destino = int(destino)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            orig = origen in self.cuenta
            dest = destino in self.cuenta
            if orig == True and dest == True:
                tipo = self.cuenta[origen].tipo
                if tipo == "1":
                    costo = self.costos_mantenim[4][1]
                elif tipo == "2":
                    costo = self.costos_mantenim[5][1]
                elif tipo == "3":
                    costo = self.costos_mantenim[11][1]
                elif tipo == "4":
                    costo = self.costos_mantenim[12][1]
                if self.cuenta[origen].titular == self.cliente_log.nombre_us:
                    if self.cuenta[origen].saldo < 0 + costo:
                        print("SU CUENTA NO TIENE SALDO")
                        input("Presione cualquier tecla para continuar")
                        self.menu_individuos()
                    elif self.cuenta[origen].saldo >=importe + costo:
                        self.cuenta[destino].saldo += importe
                        self.cuenta[origen].saldo -= importe + costo
                        print("TRANSFERENCIA EXITOSA")
                        tran = datetime.now()
                        self.movimientos_cuentas[origen]["Día ", tran.year, tran.month, tran.day, "Hora ", tran.hour, tran.minute, tran.second] = ( 
            "REALIZO UNA TRANSFERENCIA A LA CUENTA N° " + str(destino) + " POR $ " + str(importe))
                        self.movimientos_cuentas[destino]["Día ", tran.year, tran.month, tran.day, "Hora ", tran.hour, tran.minute, tran.second] = ( 
            "RECIBIO UNA TRANSFERENCIA DE LA CUENTA N° " + str(origen) + " POR $ " + str(importe))
                        print("El saldo de la cuenta ", origen, " es $ ", self.cuenta[origen].saldo)
                        input("Presione cualquier tecla para continuar ")
                        monto = False
                    else:
                        print("FONDOS INSUFICIENTES\n INGRESE UN MONTO < o = A $ ", self.cuenta[origen].saldo - costo)
                        input("Presione cualquier tecla para continuar ")
                        monto = True
                else:
                    print("Ud no es el titular de la cuenta ", origen)
                    input("Presione cualquier tecla para continuar ")
                    self.menu_individuos()
            elif orig == False:
                print("La cuenta n° ", origen, " no existe")
                error = True
                while error == True:
                    volver = input("1- Intentar con otra cuenta\n 2- Volver al menú anterior\nIngrese opción: ")
                    if volver == "1":
                        monto == True
                        error = False
                    elif volver == "2":
                        self.menu_individuos()
                    else:
                        print("OPCION INCORRECTA")
                        error = True
            else:
                print("La cuenta n° ", destino, " no existe")
                error = True
                while error == True:
                    volver = input("1- Intentar con otra cuenta\n 2- Volver al menú anterior\nIngrese opción: ")
                    if volver == "1":
                        monto == True
                        error = False
                    elif volver == "2":
                        self.menu_individuos()
                    else:
                        print("OPCION INCORRECTA")
                        error = True

    def transferencia_pyme(self):
        print("****REALIZAR UNA TRANSFERENCIA****")
        monto = True
        while monto == True:
            while True:
                origen = input("Ingrese n° de cuenta origen: ")
                importe = input("Monto a transferir: ")
                destino = input("Ingrese n° de cuenta destino: ")
                try:
                    origen = int(origen)
                    importe = int(importe)
                    destino = int(destino)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            orig = origen in self.cuenta
            dest = destino in self.cuenta
            if orig == True and dest == True:
                tipo = self.cuenta[origen].tipo
                if tipo == "1":
                    costo = self.costos_mantenim[4][1]
                elif tipo == "2":
                    costo = self.costos_mantenim[5][1]
                elif tipo == "3":
                    costo = self.costos_mantenim[11][1]
                elif tipo == "4":
                    costo = self.costos_mantenim[12][1]
                if self.cuenta[origen].titular == self.cliente_log.nombre_us:
                    self.cuenta[destino].saldo += importe
                    self.cuenta[origen].saldo -= importe + costo
                    print("TRANSFERENCIA EXITOSA")
                    tran = datetime.now()
                    self.movimientos_cuentas[origen]["Día ", tran.year, tran.month, tran.day, "Hora ", tran.hour, tran.minute, tran.second] = ( 
            "REALIZO UNA TRANSFERENCIA A LA CUENTA N° " + str(destino) + " POR $ " + str(importe))
                    self.movimientos_cuentas[destino][["Día ", tran.year, tran.month, tran.day, "Hora ", tran.hour, tran.minute, tran.second]] = ( 
            "RECIBIO UNA TRANSFERENCIA DE LA CUENTA N° " + str(origen) + " POR $ " + str(importe))
                    print("El saldo de la cuenta ", origen, " es $ ", self.cuenta[origen].saldo)
                    input("Presione cualquier tecla para continuar ")
                    monto = False
                else:
                    print("Ud no es el titular de la cuenta ", origen)
                    input("Presione cualquier tecla para continuar ")
                    self.menu_individuos()
            elif orig == False:
                print("La cuenta n° ", origen, " no existe")
                error = True
                while error == True:
                    volver = input("1- Intentar con otra cuenta\n 2- Volver al menú anterior\nIngrese opción: ")
                    if volver == "1":
                        monto == True
                        error = False
                    elif volver == "2":
                        self.menu_individuos()
                    else:
                        print("OPCION INCORRECTA")
                        input("Presione cualquier tecla para continuar ")
                        error = True
            else:
                print("La cuenta n° ", destino, " no existe")
                error = True
                while error == True:
                    volver = input("1- Intentar con otra cuenta\n 2- Volver al menú anterior\nIngrese opción: ")
                    if volver == "1":
                        monto == True
                        error = False
                    elif volver == "2":
                        self.menu_individuos()
                    else:
                        print("OPCION INCORRECTA")
                        input("Presione cualquier tecla para continuar ")
                        error = True
              
    def extraccion (self):
        monto=True
        while monto == True:
            while True:
                ext = input("Monto a extraer: $ ")
                cta = input("N° de cuenta: ")
                try:
                    ext = int(ext)
                    cta = int(cta)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            c= cta in self.cuenta
            if c:
                if self.cuenta[cta].titular == self.cliente_log.nombre_us:
                    if self.cuenta[cta].saldo >= ext:
                        self.cuenta[cta].saldo -=  ext
                        print("Saldo actual: $ ", self.cuenta[cta].saldo)
                        reti = datetime.now()
                        self.movimientos_cuentas[cta]["Día ", reti.year, reti.month, reti.day, "Hora ", reti.hour, reti.minute, reti.second] = ( 
            "REALIZO UNA EXTRACCION POR $ "+ str(ext))
                        input("Presione cualquier tecla para continuar")
                        monto = False
                    else:
                        print("FONDOS INSUFICIENTES\n INGRESE UN MONTO <= A $ ", self.cuenta[cta].saldo)
                        monto = True
                else:
                    print("La cuenta ", cta, " no le pertenece")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_individuos()
            else:
                print("LA CUENTA N° ", cta, " NO EXISTE")
                o = True
                while o == True:
                    otra = input("1- Intentar con otra cuenta\n2- Salir\nIngrese opción: ")
                    if otra == "1":
                        o = False
                        monto = True
                    elif otra == "2":
                        o = False
                        monto = False
                    else:
                        print("Opción incorrecta")
                        o = True
        
    def pago_en_linea_indiv(self): #PAGO_EN_LINEA_INDIVIDUO
        monto=True
        while monto == True:
            while True:
                pago = input("Monto a pagar: $ ")
                cta = input("N° de cuenta: ")
                try:
                    pago = int(pago)
                    cta = int(cta)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            c= cta in self.cuenta
            if c:
                if self.cuenta[cta].titular == self.cliente_log.nombre_us:
                    if self.cuenta[cta].tipo == "1":
                        if self.cuenta[cta].saldo >= pago + self.costos_mantenim[6][1]:
                            self.cuenta[cta].saldo -=  pago + self.costos_mantenim[6][1]
                            monto = False
                            print("****PAGO REALIZADO******")
                            movim = datetime.now()
                            self.movimientos_cuentas[cta]["Día ", movim.year, movim.month, movim.day, "Hora ", movim.hour, movim.minute, movim.second] = ( 
            "REALIZO UN PAGO EN LINEA POR $ "+ str(pago))
                            print("Saldo actual: $ ", self.cuenta[cta].saldo)
                            input("Presione cualquier tecla para continuar ")
                        else:
                            print("FONDOS INSUFICIENTES\n SU SALDO ACTUAL ES: $ " ,self.cuenta[cta].saldo ,"\n PARA REALIZAR EL PAGO DESEADO NECESITA DISPONER DE : $ ", pago + self.costos_mantenim[6][1])
                            dep = input("¿Desea hacer un depósito?\n Y/N ")
                            if dep == "y" or dep == "Y":
                                self.deposito()
                            else:
                                monto = False
                    elif self.cuenta[cta].tipo == "2" or self.cuenta[cta].tipo == "4":
                        if self.cuenta[cta].saldo - self.cuenta[cta].monto_retenido >= pago + self.costos_mantenim[7][1]:
                            self.cuenta[cta].saldo -=  pago + self.costos_mantenim[7][1]
                            monto = False
                            print("****PAGO REALIZADO******")
                            print("Saldo actual: $ ", self.cuenta[cta].saldo)
                            input("Presione cualquier tecla para continuar ")
                        else:
                            print("FONDOS INSUFICIENTES\n SU SALDO ACTUAL ES: $ " ,self.cuenta[cta].saldo - self.cuenta[cta].monto_retenido,"\n PARA REALIZAR EL PAGO DESEADO NECESITA DISPONER DE : $ ", pago + self.costos_mantenim[7][1])
                            dep = input("¿Desea hacer un depósito?\n Y/N ")
                            if dep == "y" or dep == "Y":
                                self.deposito()
                            else:
                                monto = False
                    elif self.cuenta[cta].tipo == "3":
                        if self.cuenta[cta].saldo >= pago + self.costos_mantenim[13][1]:
                            self.cuenta[cta].saldo -=  pago + self.costos_mantenim[13][1]
                            monto = False
                            print("****PAGO REALIZADO******")
                            print("Saldo actual: $ ", self.cuenta[cta].saldo)
                            input("Presione cualquier tecla para continuar ")
                        else:
                            print("FONDOS INSUFICIENTES\n SU SALDO ACTUAL ES: $ " ,self.cuenta[cta].saldo ,"\n PARA REALIZAR EL PAGO DESEADO NECESITA DISPONER DE : $ ", pago + self.costos_mantenim[13][1])
                            dep = input("¿Desea hacer un depósito?\n Y/N ")
                            if dep == "y" or dep == "Y":
                                self.deposito()
                            else:
                                monto = False
                else:
                    print("La cuenta ", cta, " no le pertenece")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_individuos()
            else:
                print("LA CUENTA N° ", cta, " NO EXISTE")
                monto = True

    def pago_en_linea_pyme(self):
        monto=True
        while monto == True:
            while True:
                pago = input("Monto a pagar: $ ")
                cta = input("N° de cuenta: ")
                try:
                    pago = int(pago)
                    cta = int(cta)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            c= cta in self.cuenta
            if c:
                if self.cuenta[cta].titular == self.cliente_log.nombre_us:
                    if self.cuenta[cta].tipo == "4":
                        self.cuenta[cta].saldo -=  pago + self.costos_mantenim[7][1]
                        monto = False
                        print("****PAGO REALIZADO******")
                        movim = datetime.now()
                        self.movimientos_cuentas[cta]["Día ", movim.year, movim.month, movim.day, "Hora ", movim.hour, movim.minute, movim.second] = ( 
            "REALIZO UN PAGO EN LINEA POR $ "+ str(pago))
                        print("Saldo actual: $ ", self.cuenta[cta].saldo, "\nSaldo disponible: $ ", self.cuenta[cta].saldo - self.costos_mantenim[1][1])
                        input("Presione cualquier tecla para continuar")
                    elif self.cuenta[cta].tipo == "3":
                        self.cuenta[cta].saldo -=  pago + self.costos_mantenim[13][1]
                        movim = datetime.now()
                        self.movimientos_cuentas[cta]["Día ", movim.year, movim.month, movim.day, "Hora ", movim.hour, movim.minute, movim.second] = ( 
            "REALIZO UN PAGO EN LINEA POR $ "+ str(pago))
                        monto = False
                        print("****PAGO REALIZADO******")
                        print("Saldo actual: $ ", self.cuenta[cta].saldo)
                        input("Presione cualquier tecla para continuar ")
                else:
                    print("La cuenta ", cta, " no le pertenece")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_pyme()
            else:
                print("LA CUENTA N° ", cta, " NO EXISTE")
                input("Presione cualquier tecla para continuar ")
                monto = True

    def listar_sucursales (self): #LISTA_SUCURSALES
        for suc in self.dictSucursales:
            print(
            """ N° sucursal: {}
                Localidad: {}
            """.format(suc, self.dictSucursales[suc][0]))
        input("Presione cualquier tecla para continuar ")

    def agregar_sucursal(self): 
        while True:
            num_suc = input("Ingrese el n° de sucursal: ")
            try:
                num_suc = int(num_suc)
                break
            except ValueError:
                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
        ciudad = input("Ingrese la localidad: ")
        self.dictSucursales[num_suc] = [ciudad]

    def listar_costos_mant(self): #LISTA_COSTO_MANTENIMIENTO
        print ("********\n COSTOS DE MANTENIMIENTO Y COMISIONES")
        for cos in self.costos_mantenim:
            print("""\t\t ID: {}
                Tipo de costo: {}
                Monto: $ {}""".format(cos,self.costos_mantenim[cos][0], self.costos_mantenim[cos][1]))

    def modif_costos(self,id): #MODIFICAR_COSTOS_MANTENIMIENTO
        print("El costo actual para ",self.costos_mantenim[id][0], " es $ ",self.costos_mantenim[id][1])
        while True:
            nuevo = input("Ingrese el nuevo monto: $ ")
            try:
                nuevo = int(nuevo)
                break
            except ValueError:
                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
        self.costos_mantenim[id][1] = nuevo
        print("El nuevo costo para ", self.costos_mantenim[id][0], " es $ ", self.costos_mantenim[id][1])

    def listar_cli_ind(self): #LISTAR_CLIENTES_INDIVIDUO LISTADO_CLIENTE_INDIVIDUO
        print("*****LISTADO DE CLIENTES INDIVIDUOS*****")
        for cli in self.clientes_usuarios:
            print(self.clientes_usuarios[cli])
        input("Presione cualquier tecla para continuar ")
        self.menu_administrador()
    
    def listar_pymes(self): #LISTAR_PYMES LISTADO_PYMES
        print("*****LISTADO DE USUARIOS PYMES*****")
        for py in self.clientes_pymes:
            print(self.clientes_pymes[py])
        input("Presione cualquier tecla para continuar ")
        self.menu_administrador()

    def listar_cuentas(self):
        print("Lista de cuentas")
        for cu in self.cuenta:
            print(self.cuenta[cu].__str__())
        input("Presione cualquier tecla para continuar ")
        self.menu_administrador()

    def listar_cuentas_propias(self, tit): #LISTADO_CUENTAS_PROPIAS
        lista = True
        if lista:
            print("Lista de cuentas")
            for cu in self.cuenta:
                cuenta = self.cuenta.get(cu)
                if cuenta.titular == tit:
                    print(cuenta)
                else:
                    pass
            lista = False
            input("Presione cualquier tecla para continuar ")

    def ver_mis_plazos_fijos(self): #LISTADO_PLAZOS_FIJOS
        lista = True
        if lista:
            print("Mis plazos fijos")
            for pl in self.dic_plazo_fijo:
                plazo = self.dic_plazo_fijo.get(pl)
                if plazo.titular == self.cliente_log.razon_social:
                    print(plazo)
                else:
                    pass
            lista = False
            input("Presione cualquier tecla para continuar ")
        
    def mis_saldos (self,tit): #LISTAR_SALDOS
        lista = True
        if lista:
            print("Saldo de mis cuentas")
            for cu in self.cuenta:
                cuenta = self.cuenta.get(cu)
                if cuenta.titular == tit:
                    print("Cuenta n° ",cuenta.num_cuenta," Saldo $ ", cuenta.saldo)
                else:
                    pass
            lista = False
            input("Presione cualquier tecla para continuar ")

    def crear_cuenta_pymes(self):
        retencion = self.costos_mantenim[1][1]
        print("****MENU ABRIR CUENTA****")
        tipo_cu = input("Ingrese el tipo de cuenta a crear:\n1- Cuenta Corriente Común\n2- Cuenta Corriente con Ret de Saldo\nIngrese opción: ")
        if tipo_cu =="1":
            tipo = "3"
            titular = self.cliente_log.nombre_us
            sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
            num_cuenta = Secuencia.next_nro_cuenta()
            cbu = Secuencia.next_cbu()
            fecha_apert = datetime.now()
            mon = input("1- Pesos\n2- Dolares\n3- Otra\nIngrese opción: ")
            if mon =="1":
                moneda = "Pesos"
            elif mon == "2":
                moneda = "Dólares"
            elif mon == "3":
                moneda = input("Ingrese moneda: ")
            else:
                print("Opción incorrecta")
            saldo = 0
            c_c_c = CuentaCorrienteComun(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, saldo)
            self.cuenta[num_cuenta] = c_c_c
            self.movimientos_cuentas[num_cuenta] = {}
            self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
            print("Se creó la Cuenta Corriente Común: ",self.cuenta[num_cuenta])
            self.cliente_log.cuentas[num_cuenta] = c_c_c
            dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
            error = True
            if dep == "3":
                self.menu_pyme()
            elif dep == "2":
                self.crear_cuenta_pymes()
            while dep == "1" and error == True:
                while True:
                    imp = input("Ingrese el importe a depositar: $ ")
                    try:
                        imp = int(imp)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                c_c_c.saldo += imp - self.costos_mantenim[17][1]
                deposito = datetime.now()
                self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_c_c.saldo)
                print("El nuevo saldo de la cuenta ", c_c_c.num_cuenta, " es $ ", c_c_c.saldo, "\n\n")
                self.cuenta[num_cuenta].saldo = c_c_c.saldo
                menu = True
                while menu == True:
                    dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                    if dep == "1":
                        menu = False
                    elif dep == "2":
                        self.menu_pyme()
                    else:
                        print("OPCION INCORRECTA")
                        input("Presione cualquier tecla para continuar ")
                        menu = True
            else:
                self.menu_pyme()
        elif tipo_cu == "2":
            print("\nPara abrir esta cuenta debe hacer un depósito inicial de $ ", retencion)
            seg = input("\nS- Desea continuar con la apertura\nN- Volver al menú anterior\nIngrese opción: ")
            seg = seg.upper()
            if seg == "S":
                tipo = "4"
                titular = self.cliente_log.nombre_us
                sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
                num_cuenta = Secuencia.next_nro_cuenta()
                cbu = Secuencia.next_cbu()
                fecha_apert = datetime.now()
                mon = input("1- Pesos\n2- Dolares\n3- Otra")
                if mon =="1":
                    moneda = "Pesos"
                elif mon == "2":
                    moneda = "Dólares"
                elif mon == "3":
                    moneda = input("Ingrese moneda: ")
                else:
                    print("Opción incorrecta")
                monto_retenido = retencion
                saldo = monto_retenido
                c_c_r_s = CuentaCorrienteSR(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, monto_retenido, saldo)
                self.cuenta[num_cuenta] = c_c_r_s
                self.movimientos_cuentas[num_cuenta]= {}
                self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
                self.cliente_log.cuentas[num_cuenta] = c_c_r_s
                print("SE CREÓ LA CUENTA CORRIENTE CON RETENSION DE SALDO\n\tDel cliente: ", titular, "\n\tn° de cuenta: ",sucursal, "-", num_cuenta,  "\n\tMoneda: " + moneda + "\n\tCBU", cbu, "\n\tSaldo: $ ", saldo)
                dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
                error = True
                while dep == "1" and error == True:
                    while True:
                            imp = input("Ingrese el importe a depositar: $")
                            try:
                                imp = int(imp)
                                break
                            except ValueError:
                                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                    c_c_r_s.saldo += imp - self.costos_mantenim[18][1]
                    deposito = datetime.now()
                    self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                    print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_c_r_s.saldo)
                    print("El nuevo saldo de la cuenta ", c_c_r_s.num_cuenta, " es $ ", c_c_r_s.saldo, "\n\n")
                    self.cuenta[num_cuenta].saldo = c_c_r_s.saldo 
                    menu = True
                    while menu == True:
                        dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                        if dep == "1":
                            menu = False
                        elif dep == "2":
                            self.menu_pyme()
                        elif dep == "3":
                            self.loguin()
                        else:
                            print("OPCION INCORRECTA")
                            input("Presione cualquier tecla para continuar ")
                            menu = True
            else:
                input("Presione cualquier tecla para continuar ")
                self.menu_pyme()

    def plazo_fijo(self):
        print("****MENU PLAZO FIJO****") #MENU_PLAZO_FIJO
        volver = True
        while volver == True:
            opcion = input("1- Abrir un plazo fijo\n2- Listar mis plazos fijos\n3- Volver al menú anterior\nIngrese la opción: ")
            if opcion == "1":
                print("INTERESES ACTUALES DE PLAZO FIJO")
                print("    DIAS     INTERES ACTUAL \n1-  30        ", self.costos_mantenim[14][1], " %\n2-  60        ", self.costos_mantenim[14][2], " %\n3-  90        ", self.costos_mantenim[14][3], " %\n4-  180       ", self.costos_mantenim[14][4], " % \n5-  360       ", self.costos_mantenim[14][5], " %", "\n6-  Volver al menú anterior")
                while True:
                    dias = input("Ingrese la opción: ")
                    importe = input("Ingrese el importe: $ ")
                    try:
                        dias = int(dias)
                        importe = int(importe)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                if dias == 1:
                    retiro = timedelta(30)
                    fecha = date.today()
                    total = importe + (importe * self.costos_mantenim[14][1] / 100)
                    print("$ ", importe, " a 30 dias obtendrá $ ", total, "\nFecha vencimiento: ", fecha + retiro)
                    print("El día ", fecha + retiro, " deberá retirar $ ", total)
                    acepta = input("1- Acepta\n2- No acepta\nIngrese opción ")
                    if acepta == "1":
                        num = Secuencia.next_plazo_fijo()
                        titular = self.cliente_log.razon_social
                        plazo = 30
                        monto = importe
                        inicio = fecha
                        a_retirar = total
                        vencim = fecha + timedelta(30)
                        plazo_fijo = PlazoFijo(num, titular, plazo, monto, inicio, a_retirar, vencim)
                        self.dic_plazo_fijo[num] = plazo_fijo
                        print("Plazo fijo creado con éxito")
                        input("Presione cualquier tecla para continuar ")
                        self.menu_pyme()
                    elif acepta == "2":
                        self.menu_pyme()
                    else:
                        print("Opción incorrecta")
                        input("Presione cualquier tecla para continuar ")
                elif dias == 2:
                    retiro = timedelta(60)
                    fecha = date.today()
                    total = importe + (importe * self.costos_mantenim[14][2] / 100)*2
                    print("$ ", importe, " a 60 dias obtendrá $ ", total, "\nFecha vencimiento: ", fecha + retiro)
                    print("El día ", fecha + retiro, " deberá retirar $ ", total)
                    acepta = input("1- Acepta\n2- No acepta\nIngrese opción ")
                    if acepta == "1":
                        num = Secuencia.next_plazo_fijo()
                        titular = self.cliente_log.razon_social
                        plazo = 60
                        monto = importe
                        inicio = fecha
                        a_retirar = total
                        vencim = fecha + timedelta(60)
                        plazo_fijo = PlazoFijo(num, titular, plazo, monto, inicio, a_retirar, vencim)
                        self.dic_plazo_fijo[num] = plazo_fijo
                        print("Plazo fijo creado con éxito")
                        input("Presione cualquier tecla para continuar ")
                        self.menu_pyme()
                    elif acepta == "2":
                        self.menu_pyme()
                    else:
                        print("Opción incorrecta")
                        input("Presione cualquier tecla para continuar ")
                elif dias == 3:
                    retiro = timedelta(90)
                    fecha = date.today()
                    total = importe + (importe * self.costos_mantenim[14][3] / 100)*3
                    print("$ ", importe, " a 90 dias obtendrá $ ", total)
                    print("El día ", fecha + retiro, " deberá retirar $ ", total)
                    acepta = input("1- Acepta\n2- No acepta\nIngrese opción ")
                    if acepta == "1":
                        num = Secuencia.next_plazo_fijo()
                        titular = self.cliente_log.razon_social
                        plazo = 90
                        monto = importe
                        inicio = fecha
                        a_retirar = total
                        vencim = fecha + timedelta(90)
                        plazo_fijo = PlazoFijo(num, titular, plazo, monto, inicio, a_retirar, vencim)
                        self.dic_plazo_fijo[num] = plazo_fijo
                        print("Plazo fijo creado con éxito")
                        input("Presione cualquier tecla para continuar ")
                        self.menu_pyme()
                    elif acepta == "2":
                        self.menu_pyme()
                    else:
                        print("Opción incorrecta")
                        input("Presione cualquier tecla para continuar ")
                elif dias == 4:
                    retiro = timedelta(180)
                    fecha = date.today()
                    total = importe + (importe * self.costos_mantenim[14][4] / 100)*6
                    print("$ ", importe, " a 180 dias obtendrá $ ", total)
                    print("El día ", fecha + retiro, " deberá retirar $ ", total)
                    acepta = input("1- Acepta\n2- No acepta\nIngrese opción ")
                    if acepta == "1":
                        num = Secuencia.next_plazo_fijo()
                        titular = self.cliente_log.razon_social
                        plazo = 180
                        monto = importe
                        inicio = fecha
                        a_retirar = total
                        vencim = fecha + timedelta(180)
                        plazo_fijo = PlazoFijo(num, titular, plazo, monto, inicio, a_retirar, vencim)
                        self.dic_plazo_fijo[num] = plazo_fijo
                        print("PLAZO FIJO REALIZADO CON EXITO")
                        input("Presione cualquier tecla para continuar ")
                        self.menu_pyme()
                        input("Presione cualquier tecla para continuar ")
                    elif acepta == "2":
                        self.menu_pyme()
                    else:
                        print("Opción incorrecta")
                        input("Presione cualquier tecla para continuar ")
                elif dias == 5:
                    retiro = timedelta(360)
                    fecha = date.today()
                    total = importe + (importe * self.costos_mantenim[14][5] / 100)*12
                    print("$ ", importe, " a 360 dias obtendrá $ ", total)
                    print("El día ", fecha + retiro, " deberá retirar $ ", total)
                    acepta = input("1- Acepta\n2- No acepta\nIngrese opción ")
                    if acepta == "1":
                        num = Secuencia.next_plazo_fijo()
                        titular = self.cliente_log.razon_social
                        plazo = 360
                        monto = importe
                        inicio = fecha
                        a_retirar = total
                        vencim = fecha + timedelta(360)
                        plazo_fijo = PlazoFijo(num, titular, plazo, monto, inicio, a_retirar, vencim)
                        self.dic_plazo_fijo[num] = plazo_fijo
                        print("Plazo fijo creado con éxito")
                        input("Presione cualquier tecla para continuar ")
                        self.menu_pyme()
                        input("Presione cualquier tecla para continuar ")
                        input("Presione cualquier tecla para continuar ")
                    elif acepta == "2":
                        self.menu_pyme()
                    else:
                        print("Opción incorrecta")
                        input("Presione cualquier tecla para continuar ")
                elif dias == 6:
                    self.menu_pyme()
            elif opcion == "2":
                self.ver_mis_plazos_fijos()
            elif opcion == "3":
                self.menu_pyme()
            else:
                print("Opción incorrecta")
                volver = True
        else:
            volver = True
            
    def modif_int_pla_fijo(self): #MODIFICAR_INTERES_PLAZO_FIJO
        print("****MENU PARA MODIFICAR INTERESES DE PLAZO FIJOS****")
        modif = True
        while modif == True:
            print("    DIAS     INTERES ACTUAL \n1-  30        ", self.costos_mantenim[14][1], " %\n2-  60        ", self.costos_mantenim[14][2], " %\n3-  90        ", self.costos_mantenim[14][3], " %\n4-  180       ", self.costos_mantenim[14][4], " % \n5-  360       ", self.costos_mantenim[14][5], " %")
            op = input("Ingrese opción: ")
            if op == "1":
                print("Interés mensual actual a 30 DIAS = ", self.costos_mantenim[14][1], " %")
                while True:
                    nuevo = input("Nuevo valor: interés % ")
                    try:
                        nuevo = int(nuevo)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                self.costos_mantenim[14][1] = nuevo
                print("El nuevo interés para PLAZO FIJO a 30 DIAS es de ", self.costos_mantenim[14][1], " %")
                otro = input("1- MODIFICAR OTRO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                if otro == "1":
                    modif = True
                else:
                    self.menu_administrador()

            elif op == "2":
                print("Interés mensual actual a 60 DIAS = ", self.costos_mantenim[14][2], " %")
                while True:
                    nuevo = input("Nuevo valor: interés % ")
                    try:
                        nuevo = int(nuevo)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                self.costos_mantenim[14][2] = nuevo
                print("El nuevo interés para PLAZO FIJO a 60 DIAS es de ", self.costos_mantenim[14][2], " %")
                otro = input("1- MODIFICAR OTRO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                if otro == "1":
                    modif = True
                else:
                    self.menu_administrador()

            elif op == "3":
                print("Interés mensual actual a 90 DIAS = ", self.costos_mantenim[14][3], " %")
                while True:
                    nuevo = input("Nuevo valor: interés % ")
                    try:
                        nuevo = int(nuevo)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                self.costos_mantenim[14][3] = nuevo
                print("El nuevo interés para PLAZO FIJO a 90 DIAS es de ", self.costos_mantenim[14][3], " %")
                otro = input("1- MODIFICAR OTRO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                if otro == "1":
                    modif = True
                else:
                    self.menu_administrador()

            elif op == "4":
                print("Interés mensual actual a 180 DIAS = ", self.costos_mantenim[14][4], " %")
                while True:
                    nuevo = input("Nuevo valor: interés % ")
                    try:
                        nuevo = int(nuevo)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                self.costos_mantenim[14][4] = nuevo
                print("El nuevo interés para PLAZO FIJO a 180 DIAS es de ", self.costos_mantenim[14][4], " %")
                otro = input("1- MODIFICAR OTRO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                if otro == "1":
                    modif = True
                else:
                    self.menu_administrador()

            elif op == "5":
                print("Interés mensual actual a 360 DIAS = ", self.costos_mantenim[14][5], " %")
                while True:
                    nuevo = input("Nuevo valor: interés % ")
                    try:
                        nuevo = int(nuevo)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                self.costos_mantenim[14][5] = nuevo
                print("El nuevo interés para PLAZO FIJO a 360 DIAS es de ", self.costos_mantenim[14][5], " %")
                otro = input("1- MODIFICAR OTRO\n2- VOLVER AL MENU ANTERIOR\nIngrese opción: ")
                if otro == "1":
                    modif = True
                else:
                    self.menu_administrador()
            else:
                print("OPCION INCORRECTA")
                modif = True

    def comprar_mon_ext(self): #COMPRAR_MONEDA_EXTRANJERA
        monto = True
        while monto == True:
            print("VA A REALIZAR UNA COMPRA DE DOLARES ESTADOUNIDENSES")
            print("Cotización actual: $", self.costos_mantenim[21][1])
            while True:
                dol = input("Cantidad de dólares a comprar: U$S ")
                cta = input("N° de cuenta a debitar: ")
                try:
                    dol = int(dol)
                    cta = int(cta)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            imp = dol * self.costos_mantenim[21][1]
            print("SE DEBITARON DE LA CUENTA N° " + str(cta) + ' ',"$" + str(imp))
            c = cta in self.cuenta
            if c:
                if self.cuenta[cta].titular == self.cliente_log.nombre_us:
                    if self.cuenta[cta].saldo >= imp:
                        self.cuenta[cta].saldo -= imp
                        monto = False
                        print("****COMPRA DE DOLARES REALIZADA******")
                        dolar = datetime.now()
                        self.movimientos_cuentas[cta]["Día ", dolar.year, dolar.month, dolar.day, "Hora ", dolar.hour, dolar.minute, dolar.second] = ( 
            "COMPRA DE U$S "+ str(dol)+" POR $ "+ str(imp))
                        print("Saldo actual: $ ", self.cuenta[cta].saldo)
                        input("Presione cualquier tecla para continuar ")
                    else:
                        print("FONDOS INSUFICIENTES\n SU SALDO ACTUAL ES: $ " ,self.cuenta[cta].saldo ,"\n PARA REALIZAR LA COMPRA DESEADA NECESITA DISPONER DE : ", imp)
                        dep = input("¿Desea hacer un depósito?\n Y/N ")
                        if dep == "y" or dep == "Y":
                            self.deposito()
                        else:
                            monto = False
                else:
                    print("La cuenta n°", cta, " no le pertenece")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_individuos()
            else:
                print("LA CUENTA N° ", cta, " NO EXISTE")
                monto = True

    def bonos(self): #COMPRAR_BONOS
        monto = True
        while monto == True:
            print("VA A REALIZAR UNA COMPRA DE BONOS")
            print("Cotización actual: $ ", self.costos_mantenim[22][1])
            print("% mensual al día de hoy: ", self.costos_mantenim[23][1])
            while True:
                bon = input("Cantidad de Bonos a comprar: ")
                cta = input("N° de cuenta a debitar: ")
                try:
                    bon = int(bon)
                    cta = int(cta)
                    break
                except ValueError:
                    print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
            imp = bon * self.costos_mantenim[22][1]
            print("Va a comprar $ ",imp, " en bonos al ", self.costos_mantenim[23][1], "% mensual.")
            c = cta in self.cuenta
            if c:
                if self.cuenta[cta].titular == self.cliente_log.nombre_us:
                    if self.cuenta[cta].saldo >= imp:
                        self.cuenta[cta].saldo -= imp
                        print("****COMPRA DE BONOS REALIZADA******")
                        bono = datetime.now()
                        self.movimientos_cuentas[cta]["Día ", bono.year, bono.month, bono.day, "Hora ", bono.hour, bono.minute, bono.second] = ("COMPRA DE "+ str(bon) + " BONOS POR $ "
            + str(imp))
                        print("Saldo actual: $ ", self.cuenta[cta].saldo)
                        # fecha_actual = datetime.utcnow()
                        # nueva = datetime.timedelta(days=1)
                        #print(datetime.utcnow() + datetime(days=30))
                        input("Presione cualquier tecla para continuar ")
                        monto = False
                    else:
                        print("FONDOS INSUFICIENTES\n SU SALDO ACTUAL ES: $ " ,self.cuenta[cta].saldo ,"\n PARA REALIZAR LA COMPRA DESEADA NECESITA DISPONER DE : $ ", imp)
                        dep = input("¿Desea hacer un depósito?\n Y/N ")
                        if dep == "y" or dep == "Y":
                            self.deposito()
                        else:
                            input("Presione cualquier tecla para continuar ")
                            monto = False
                else:
                    print("La cuenta n°", cta, " no le pertenece")
                    input("Presione cualquier tecla para continuar ")
                    self.menu_pyme()
            else:
                print("LA CUENTA N° ", cta, " NO EXISTE")
                input("Presione cualquier tecla para continuar ")
                monto = True

    def crear_cuenta(self):
        retencion = self.costos_mantenim[1][1]
        error = False
        while error == False:
            tipo = input("Ingrese el tipo de cuenta a crear:\n1- Caja de Ahorro Común\n2- Caja de ahorro con Ret de Saldo\n3- Cuenta Corriente Común\n4- Cuenta Corriente con Ret de Saldo\n5- Salir\nIngrese opción: ")
            if tipo == "1":
                titular = self.cliente_log.nombre_us
                sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
                num_cuenta = Secuencia.next_nro_cuenta()
                cbu = Secuencia.next_cbu()
                fecha_apert = datetime.now()
                saldo = 0
                tipo = "1"
                c_a = CajaAhorroComun(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, saldo)
                self.cuenta[num_cuenta] = c_a
                self.movimientos_cuentas[num_cuenta]= {}
                self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
                self.cliente_log.cuentas[num_cuenta] = c_a
                print("La cuenta fué creada con éxito")
                print("Cuenta n°: ",c_a.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido, "\n\tSaldo: ",c_a.saldo)
                dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
                error = True
                while dep == "1" and error == True:
                    while True:
                        imp = input("Ingrese el importe a depositar: $ ")
                        try:
                            imp = int(imp)
                            break
                        except ValueError:
                            print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                    c_a.saldo += imp - self.costos_mantenim[15][1]
                    deposito = datetime.now()
                    self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                    print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_a.saldo)
                    print("El nuevo saldo de la cuenta ", c_a.num_cuenta, " es $ ", c_a.saldo, "\n\n")
                    print("Cuenta n°: ",c_a.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido, "\n\tSaldo: ",c_a.saldo)
                    self.cuenta[num_cuenta].saldo = c_a.saldo 
                    menu = True
                    while menu == True:
                        dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                        if dep == "1":
                            menu = False
                        elif dep == "2":
                            self.menu_individuos()
                        elif dep == "3":
                            self.loguin()
                        else:
                            print("OPCION INCORRECTA")
                            input("Presione cualquier tecla para continuar ")
                            menu = True
            elif tipo == "2":
                print("\nPara abrir esta cuenta debe hacer un depósito inicial de $ ", retencion)
                seg = input("\nS- Desea continuar con la apertura\nN- Volver al menú anterior\n S/N\nIngrese opción: ")
                seg = seg.upper()
                if seg == "S":
                    tipo = "2"
                    titular = self.cliente_log.nombre_us
                    sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
                    num_cuenta = Secuencia.next_nro_cuenta()
                    cbu = Secuencia.next_cbu()
                    fecha_apert = datetime.now()
                    monto_retenido = retencion
                    saldo = monto_retenido
                    c_a_r_s = CajaAhorroRS(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, monto_retenido, saldo)
                    self.cuenta[num_cuenta] = c_a_r_s
                    self.movimientos_cuentas[num_cuenta]= {}
                    self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
                    self.cliente_log.cuentas[num_cuenta] = c_a_r_s
                    print("La cuenta fué creada con éxito")
                    print("Cuenta n°: ",c_a_r_s.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido, "\n\tSaldo: ",c_a_r_s.saldo, "\n\tSaldo disponible: ",c_a_r_s.saldo-c_a_r_s.monto_retenido)
                    dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
                    error = True
                    if dep == "3":
                        self.menu_individuos()
                    elif dep == "2":
                        self.crear_cuenta()
                    while dep == "1" and error == True:
                        while True:
                            imp = input("Ingrese el importe a depositar: $ ")
                            try:
                                imp = int(imp)
                                break
                            except ValueError:
                                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                        c_a_r_s.saldo +=  imp - self.costos_mantenim[16][1]
                        deposito = datetime.now()
                        self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                        print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_a_r_s.saldo)
                        print("El nuevo saldo de la cuenta ", c_a_r_s.num_cuenta, " es $ ", c_a_r_s.saldo, "\n\n")
                        print("Cuenta n°: ",c_a_r_s.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido, "\n\tSaldo: $ ",c_a_r_s.saldo, "\n\tSaldo disponible: $ ",c_a_r_s.saldo-c_a_r_s.monto_retenido)
                        self.cuenta[num_cuenta].saldo = c_a_r_s.saldo
                        menu = True
                        while menu == True:
                            dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                            if dep == "1":
                                menu = False
                            elif dep == "2":
                                self.menu_individuos()
                            else:
                                print("OPCION INCORRECTA")
                                input("Presione cualquier tecla para continuar ")
                                menu = True
                else:
                    self.menu_individuos()
            elif tipo =="3":
                tipo = "3"
                titular = self.cliente_log.nombre_us
                sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
                num_cuenta = Secuencia.next_nro_cuenta()
                cbu = Secuencia.next_cbu()
                fecha_apert = datetime.now()
                mon = input("1- Pesos\n2- Dolares\n3- Otra\nIngrese opción: ")
                if mon =="1":
                    moneda = "Pesos"
                elif mon == "2":
                    moneda = "Dólares"
                elif mon == "3":
                    moneda = input("Ingrese moneda: ")
                else:
                    print("Opción incorrecta")
                    input("Presione cualquier tecla para continuar ")
                saldo = 0
                c_c_c = CuentaCorrienteComun(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, saldo)
                self.cuenta[num_cuenta] = c_c_c
                self.movimientos_cuentas[num_cuenta]= {}
                self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
                self.cliente_log.cuentas[num_cuenta] = c_c_c
                print("La cuenta fué creada con éxito")
                print("Cuenta n°: ",c_c_c.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido,"\n\tMoneda: ", c_c_c.moneda, "\n\tSaldo: $ ",c_c_c.saldo)
                dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
                error = True
                if dep == "3":
                    self.menu_individuos()
                elif dep == "2":
                    self.crear_cuenta()
                while dep == "1" and error == True:
                    while True:
                            imp = input("Ingrese el importe a depositar: $ ")
                            try:
                                imp = int(imp)
                                break
                            except ValueError:
                                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                    c_c_c.saldo += imp - self.costos_mantenim[17][1]
                    deposito = datetime.now()
                    self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                    print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_c_c.saldo)
                    print("El nuevo saldo de la cuenta ", c_c_c.num_cuenta, " es $ ", c_c_c.saldo, "\n\n")
                    print("Cuenta n°: ",c_c_c.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido,"\n\tMoneda: ", c_c_c.moneda, "\n\tSaldo: $ ",c_c_c.saldo)
                    self.cuenta[num_cuenta].saldo = c_c_c.saldo 
                    menu = True
                    while menu == True:
                        dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                        if dep == "1":
                            menu = False
                        elif dep == "2":
                            self.menu_individuos()
                        else:
                            print("OPCION INCORRECTA")
                            input("Presione cualquier tecla para continuar ")
                            menu = True
                else:
                    self.menu_individuos()

            elif tipo == "4":
                print("\nPara abrir esta cuenta debe hacer un depósito inicial de $ ", retencion)
                seg = input("\nS- Desea continuar con la apertura\nN- Volver al menú anterior\n S/N\nIngrese opción: ")
                seg = seg.upper()
                if seg == "S":
                    tipo = "4"
                    titular = self.cliente_log.nombre_us
                    sucursal = rd.randint(100, 99 + len(self.dictSucursales.keys()))
                    num_cuenta = Secuencia.next_nro_cuenta()
                    cbu = Secuencia.next_cbu()
                    fecha_apert = datetime.now()
                    mon = input("1- Pesos\n2- Dolares\n3- Otra")
                    if mon =="1":
                        moneda = "Pesos"
                    elif mon == "2":
                        moneda = "Dólares"
                    elif mon == "3":
                        moneda = input("Ingrese moneda: ")
                    else:
                        print("Opción incorrecta")
                    monto_retenido = retencion
                    saldo = monto_retenido
                    c_c_r_s = CuentaCorrienteSR(tipo, titular, sucursal, num_cuenta, cbu, fecha_apert, moneda, monto_retenido, saldo)
                    self.cuenta[num_cuenta] = c_c_r_s
                    self.movimientos_cuentas[num_cuenta]= {}
                    self.movimientos_cuentas[num_cuenta]["Día ", fecha_apert.year, fecha_apert.month, fecha_apert.day, "Hora ", fecha_apert.hour, fecha_apert.minute, fecha_apert.second] = ( 
            "APERTURA DE CUENTA")
                    self.cliente_log.cuentas[num_cuenta] = c_c_r_s
                    print("La cuenta fué creada con éxito")
                    print("Cuenta n°: ",c_c_r_s.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido,"\n\tMoneda: ", c_c_r_s.moneda, "\n\tSaldo: $ ",c_c_r_s.saldo, "\n\tSaldo disponible: $ ",c_c_r_s.saldo-c_c_r_s.monto_retenido)
                    dep = input("1- Hacer un depósito\n2- Volver al menú anterior\n3- Salir\nIngrese opción: ")
                    error = True
                    while dep == "1" and error == True:
                        while True:
                            imp = input("Ingrese el importe a depositar: $ ")
                            try:
                                imp = int(imp)
                                break
                            except ValueError:
                                print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                        c_c_r_s.saldo = c_c_r_s.saldo + imp - self.costos_mantenim[18][1]
                        deposito = datetime.now()
                        self.movimientos_cuentas[num_cuenta]["Día ", deposito.year, deposito.month, deposito.day, "Hora ", deposito.hour, deposito.minute, deposito.second] = ( 
            "DEPOSITO POR $ " + str(imp))
                        print( "ÚLTIMO DEPÓSITO $ ", imp, " ----> SALDO $ ",c_c_r_s.saldo)
                        print("Cuenta n°: ",c_c_r_s.num_cuenta,"\n\tCliente: ",self.cliente_log.nombre," ",self.cliente_log.apellido,"\n\tMoneda: ", c_c_r_s.moneda, "\n\tSaldo: $ ",c_c_r_s.saldo, "\n\tSaldo disponible: $ ",c_c_r_s.saldo-c_c_r_s.monto_retenido)
                        self.cuenta[num_cuenta].saldo = c_c_r_s.saldo 
                        menu = True
                        while menu == True:
                            dep = input("1- Hacer otro depósito a la misma cuenta\n2- Salir\nIngrese opción: ")
                            if dep == "1":
                                menu = False
                            elif dep == "2":
                                self.menu_individuos()
                            elif dep == "3":
                                self.loguin()
                            else:
                                print("OPCION INCORRECTA")
                                menu = True
                else:
                    self.menu_individuos()
            elif tipo == "5":
                self.menu_individuos()
            else:
                print("OPCIÓN INCORRECTA")
                error = False

    def cerrar_cuenta_pyme(self, titular):
        print("ESTÁ POR CERRAR UNA CUENTA")
        menu = True
        while menu == True:
            seguir = input("1- CONTINUAR\n2- VOLVER AL MENÚ ANTERIOR\nIngrese opción: ")
            if seguir == "1":
                while True:
                    cerrar = input("Ingrese el n° de cuenta ")
                    try:
                        cerrar = int(cerrar)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                c = cerrar in self.cuenta
                if c:
                    for cu in self.cuenta:
                        iterar = True
                        while iterar == True:
                            if cu == cerrar:
                                cuenta = self.cuenta.get(cu)
                                saldo = cuenta.saldo
                                if cuenta.titular == titular:
                                    if saldo == 0:
                                        del self.cuenta[cerrar]
                                        print("CUENTA N°", cerrar, " CERRADA CON EXITO")
                                        cierre = datetime.now()
                                        self.movimientos_cuentas[cerrar]["Día ", cierre.year, cierre.month, cierre.day, "Hora ", cierre.hour, cierre.minute, cierre.second] = ( 
            "CIERRE DE CUENTA")
                                        input("Presione cualquier tecla para continuar ")
                                        self.menu_pyme()
                                        iterar = False
                                    elif saldo > 0:
                                        print("Debe retirar el total del saldo\nSaldo actual: $ ", saldo)
                                        self.extraccion()
                                    else:
                                        print("Tiene la cuenta en descubierto\nDebe saldar su deuda de $ ", saldo)
                                        self.deposito()
                                else:
                                    print("Ud no puede cerrar ésta cuenta\nLa cuenta n°", cerrar, " no le pertenece")
                            else:
                                iterar = False
                                menu = False
                    else:
                        menu = False
                else:
                    print("La cuenta n°", cerrar, " no existe")
            elif seguir == "2":
                menu = False
            else:
                print("OPCIÓN INCORRECTA")
                menu = True

    def cerrar_cuenta_individuo(self, titular):
        print("ESTÁ POR CERRAR UNA CUENTA")
        menu = True
        while menu == True:
            seguir = input("1- CONTINUAR\n2- VOLVER AL MENÚ ANTERIOR\nIngrese opción: ")
            if seguir == "1":
                while True:
                    cerrar = input("Ingrese el n° de cuenta ")
                    try:
                        cerrar = int(cerrar)
                        break
                    except ValueError:
                        print("DEBE INGRESAR NUMEROS, SIN PUNTOS")
                c = cerrar in self.cuenta
                if c:
                    for cu in self.cuenta:
                        iterar = True
                        while iterar == True:
                            if cu == cerrar:
                                cuenta = self.cuenta.get(cu)
                                saldo = cuenta.saldo
                                if cuenta.titular == titular:
                                    if saldo == 0:
                                        del self.cuenta[cerrar]
                                        print("CUENTA CERRADA CON EXITO")
                                        cierre = datetime.now()
                                        self.movimientos_cuentas[cerrar]["Día ", cierre.year, cierre.month, cierre.day, "Hora ", cierre.hour, cierre.minute, cierre.second] = ( 
            "CIERRE DE CUENTA")
                                        input("Presione cualquier tecla para continuar ")
                                        self.menu_individuos()
                                        iterar = False
                                    else:
                                        print("Debe retirar el total del saldo\nSaldo actual: $", saldo)
                                        self.extraccion()
                                else:
                                    print("Ud no puede cerrar ésta cuenta\nLa cuenta n°", cerrar, " no le pertenece")
                                    input("Presione cualquier tecla para continuar ")
                                    iterar = False
                            else:
                                iterar = False
                                menu = False
                    else:
                        menu = False
                else:
                    print("La cuenta ", cerrar, " no existe")
                    menu = True
            elif seguir == "2":
                menu = False
            else:
                print("OPCIÓN INCORRECTA")
                menu = True
            
banco = Banco()
banco.load_datos()
banco.load_pymes()
banco.load_cuentas()
banco.loguin()