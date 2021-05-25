from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    #Variable de clase
    tareas = ['carpinteria','electricidad','plomeria']
    #Atributos
    __tarea = ''
    __fechaIn = None
    __fechaFin = None
    __viatico = 0.0
    __costoObra = 0.0
    __montoSeguro = 0.0

    def __init__(self,dni,nom,dir,tel,tarea,fIn,fFin,viatico,cObra,mSeguro):
        super().__init__(dni,nom,dir,tel)
        self.__tarea = tarea
        self.__fechaIn = fIn
        self.__fechaFin = fFin
        self.__viatico = viatico
        self.__costoObra = cObra
        self.__montoSeguro = mSeguro

    def getTarea(self):
        return self.__tarea
    
    def getMontoObra(self):
        return self.__costoObra
    
    def getFechaFin(self):
        return self.__fechaFin
    
    def calcSueldo(self):
        sueldo = self.__costoObra - self.__viatico - self.__montoSeguro
        return sueldo