from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    #Atributos
    __sueldoBasico = 0.0
    __antiguedad = 0

    def __init__(self,dni,nom,dir,tel,basico,ant):
        super().__init__(dni,nom,dir,tel)
        self.__sueldoBasico = basico
        self.__antiguedad = ant
    
    def calcSueldo(self):
        sueldo = self.__sueldoBasico * (1 + 0.01*self.__antiguedad)
        sueldo = round(sueldo,2)
        return sueldo