from clases import *
import random as rd
from secuencia import *
from datetime import date, datetime, timedelta
from base_datos import *
from bb_dd_pymes import *
from bb_dd_cuentas import *

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
                    input("Presione cualquier tecla para continuar")
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
