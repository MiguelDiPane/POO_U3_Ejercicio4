from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    #Atributos
    __sueldoBasico = 0.0
    __antiguedad = 0

    def __init__(self,dni,nom,dir,tel,basico,ant):
        super().__init__(dni,nom,dir,tel)
        self.__sueldoBasico = basico
        self.__antiguedad = ant

    #Ficha empleado de planta
    def showEmpleado(self):
        super().showEmpleado()
        print('| Condicion: {:38}|'.format('PLANTA'))
        print('| Sueldo basico [$]: {:30}|'.format(str(self.__sueldoBasico)))
        print('| Antiguedad: {:37}|'.format(str(self.__antiguedad)))

    def calcSueldo(self):
        sueldo = self.__sueldoBasico * (1 + 0.01*self.__antiguedad)
        sueldo = round(sueldo,2)
        return sueldo

    def getTipo(self):
        return 'planta'