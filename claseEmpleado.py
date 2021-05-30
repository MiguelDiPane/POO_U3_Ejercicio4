import abc
from abc import ABC

class Empleado:
    #Atributos
    _dni = ''
    _nombre = ''
    _direccion = ''
    _telefono = ''

    def __init__(self,dni,nom,dir,tel):
        self._dni = dni
        self._nombre = nom
        self._direccion = dir
        self._telefono = tel
        
    def getDNI(self):
        return self._dni
    def getDir(self):
        return self._direccion
    def getNom(self):
        return self._nombre
    def getTel(self):
        return self._telefono

    #Ficha empleado
    def showEmpleado(self):
        print('| DNI: {:44}|'.format(self._dni))
        print('| Nombre: {:41}|'.format(self._nombre))
        print('| Direccion: {:38}|'.format(self._direccion))
        print('| Telefono: {:39}|'.format(self._telefono))

    @abc.abstractmethod
    def calcSueldo(self):
        pass

    @abc.abstractmethod
    def getTipo(self):
        pass
    