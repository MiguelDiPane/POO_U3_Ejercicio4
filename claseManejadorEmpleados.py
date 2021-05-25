import numpy as np
from datetime import datetime
from datetime import date
from claseEmpleado import Empleado
from claseEmpleadoContratado import EmpleadoContratado
from claseEmpleadoExterno import EmpleadoExterno
from claseEmpleadoPlanta import EmpleadoPlanta
from claseMenu import Menu

class ManejadorEmpleados:
    #Atributos
    __empleados = None
    __actual = 0

    def __init__(self,dimension = 0):
        self.__empleados = np.empty(dimension,dtype=Empleado)
        
    def addEmpleado(self,empleado):
        if isinstance(empleado,Empleado):
            self.__empleados[self.__actual] = empleado
            self.__actual += 1
        else:
            print('Error: No corresponde a un empleado.')

    def crearEmpleadoPlanta(self,dni,nom,dir,tel,basico,ant):
        try:
            if dni.isdigit() and tel.isdigit():
                basico = float(basico)
                ant = int(ant)
                newEmpleado = EmpleadoPlanta(dni,nom,dir,tel,basico,ant)
                self.addEmpleado(newEmpleado)
            else:
                print('Error: No se pudo cargar el empleado de planta')
        except ValueError:
            print('Error: No se pudo cargar el empleado de planta')

    def crearEmpleadoContratado(self,dni,nom,dir,tel,fIn,fFin,CantH):
        try:
            if dni.isdigit() and tel.isdigit():
                #convierto string a objeto fecha hora
                fIn = datetime.strptime(fIn,'%d/%m/%y')
                fFin = datetime.strptime(fFin,'%d/%m/%y')
                #Quito la hora, convierte objeto datetime en date
                fIn = fIn.date()
                fFin = fFin.date()
                CantH = int(CantH)
                newEmpleado = EmpleadoContratado(dni,nom,dir,tel,fIn,fFin,CantH)
                self.addEmpleado(newEmpleado)
            else:
                print('Error: No se pudo cargar el empleado contratado')
        except ValueError:
            print('Error: No se pudo cargar el empleado contratado')

    def crearEmpleadoExterno(self,dni,nom,dir,tel,tarea,fIn,fFin,viatico,cObra,mSeguro):
        try:
            if dni.isdigit() and tel.isdigit():
                #convierto string a objeto fecha hora
                fIn = datetime.strptime(fIn,'%d/%m/%y')
                fFin = datetime.strptime(fFin,'%d/%m/%y')
                #Quito la hora, convierte objeto datetime en date
                fIn = fIn.date()
                fFin = fFin.date()        
                #Conversion de otros atributos
                viatico = float(viatico)
                cObra = float(cObra)
                mSeguro = float(mSeguro)
                if tarea.lower() in EmpleadoExterno.tareas:
                    newEmpleado = EmpleadoExterno(dni,nom,dir,tel,tarea,fIn,fFin,viatico,cObra,mSeguro)
                    self.addEmpleado(newEmpleado)
                else:
                    print('Error: Tarea no permitida')
            else:
                print('Error: No se pudo cargar el empleado externo')
        except ValueError:
            print('Error: No se pudo cargar el empleado externo')

    #Busca solo empleados contratados para incrementar sus horas trabajadas
    def searchEmpleadoC(self,dni):
        resultado = None
        if dni.isdigit():
            i = 0
            esta = False
            while i < len(self.__empleados) and not esta:
                if isinstance(self.__empleados[i],EmpleadoContratado) and dni == self.__empleados[i].getDNI():
                    esta = True
                    resultado = self.__empleados[i]
                else:
                    i += 1
            if not esta:
                print('El dni ingresado NO corresponde a un empleado contratado.')
        else: 
            print('Error: Dni incorrecto')
        return resultado

    #Calcula el monto total de una tarea no finalizada
    def totalTarea(self):
        menu = Menu()
        opciones = []
        i = 1
        for tarea in EmpleadoExterno.tareas:
            opciones.append('[{0}]- '.format(str(i))+ tarea)
            i+=1
        opciones.append('[0]- Volver al menu principal')
        menu.define_menu('TAREAS DISPONIBLES',opciones)
        menu.showMenu()
        op = menu.selectOption()
        while op != 0:
            miTarea = EmpleadoExterno.tareas[op-1]
            monto = 0.0
            fechaHoy = date.today()
            for empleado in self.__empleados:
                if isinstance(empleado,EmpleadoExterno):
                    tarea = empleado.getTarea()            
                    if miTarea == tarea and fechaHoy < empleado.getFechaFin():
                        monto += empleado.getMontoObra()
            #Imprimo resultados:
            header = '+' + '-' * 50 + '+' 
            print(header)
            print('|{0:^50}|'.format(miTarea.upper()))
            print(header)
            print('| Monto total [$]: {:32}|'.format(str(monto)))
            print(header)
            print('Nota: Solo se consideran las tareas que no han finalizado.\n')
            input('Presione ENTER para continuar...')
            menu.define_menu('TAREAS DISPONIBLES',opciones)
            menu.showMenu()
            op = menu.selectOption()

    #Muestro empleados que recibiran ayuda solidaria
    def listBeneficiarios(self):
        header = '+' + '-' * 50 + '+'
        print(header)
        print('|{:^50}|'.format('BENEFICIARIOS AYUDA SOLIDARIA'))
        print(header)  
        for empleado in self.__empleados:
            sueldo = empleado.calcSueldo()
            if sueldo < 25000:
                if isinstance(empleado,EmpleadoPlanta):
                    condicion = 'PLANTA'
                elif isinstance(empleado,EmpleadoContratado):
                    condicion = 'CONTRATADO'
                else:
                    condicion = 'EXTERNO'
                print('| DNI: {:44}|'.format(empleado.getDNI()))
                print('| Nombre: {:41}|'.format(empleado.getNom()))
                print('| Direccion: {:38}|'.format(empleado.getDir()))
                print('| Sueldo: {:41}|'.format(str(sueldo)))
                print('| Condicion: {:38}|'.format(condicion))
                print(header)

    #Listar todos los empleados con su sueldo
    def listarEmpleados(self):
        header = '+' + '-' * 50 + '+'
        print(header)
        print('|{:^50}|'.format('LISTA DE EMPLEADOS'))
        print(header) 
        for empleado in self.__empleados:
            sueldo = empleado.calcSueldo()
            print('| Nombre: {:41}|'.format(empleado.getNom()))
            print('| Telefono: {:39}|'.format(empleado.getTel()))
            print('| Sueldo: {:41}|'.format(str(sueldo)))
            print(header)