from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    #Variable de clase
    valorHora = 800 #valor de la hora trabajada
    #Atributos
    __fechaIn = None #fechas de inicio y fin del contrato
    __fechaFin = None
    __cantHoras = 0 #Cantidad de horas trabajadas

    def __init__(self,dni,nom,dir,tel,fIn,fFin,CantH):
        super().__init__(dni,nom,dir,tel)
        self.__fechaIn = fIn
        self.__fechaFin = fFin
        self.__cantHoras = CantH
    
    #Ficha empleado contratado
    def showEmpleado(self):
        header = '+' + '-' * 50 + '+'
        print(header)
        print('|{:^50}|'.format('EMPLEADO'))
        print(header)
        print('| DNI: {:44}|'.format(self._dni))
        print('| Nombre: {:41}|'.format(self._nombre))
        print('| Direccion: {:38}|'.format(self._direccion))
        print('| Telefono: {:39}|'.format(self._telefono))
        print(header)
        print('| Condicion: {:38}|'.format('CONTRATADO'))
        print('| Valor hora: {:37}|'.format(str(self.valorHora)))
        print('| Inicio contrato: {:32}|'.format(str(self.__fechaIn)))
        print('| Fin contrato: {:35}|'.format(str(self.__fechaFin)))
        print('| Horas trabajadas: {:31}|'.format(str(self.__cantHoras)))
        print(header)
    
    def addHoras(self,horas):
        try:
            horas = int(horas)
            self.__cantHoras += horas
            print('Horas agregadas correctamente!')
        except ValueError:
            print('Error: La cantidad de horas debe ser un entero.')
    
    def calcSueldo(self):
        sueldo = self.__cantHoras * self.valorHora
        return sueldo
