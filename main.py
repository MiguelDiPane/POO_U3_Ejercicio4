import csv
from claseManejadorEmpleados import ManejadorEmpleados
from claseMenu import Menu

def leerArchivo(nomArchivo,manejador):
    archivo = open(nomArchivo)
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            if nomArchivo == 'planta.csv':
                manejador.crearEmpleadoPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]) 
            elif nomArchivo == 'contratados.csv':
                manejador.crearEmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            elif nomArchivo == 'externos.csv':
                manejador.crearEmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])                        
    archivo.close()

if __name__ == '__main__':
    #Cantidad de los empleados en archivos: 45
    try:
        cant = input('Ingrese cantidad TOTAL de empleados (45): ')
        empleados = ManejadorEmpleados(int(cant))
        leerArchivo('planta.csv',empleados)
        leerArchivo('contratados.csv',empleados)
        leerArchivo('externos.csv',empleados)
        
        miMenu = Menu()
        miMenu.define_menu('Menu de opciones',['[1]- Registrar horas','[2]- Monto total de tarea','[3]- Lista beneficiarios ayuda','[4]- Calcular sueldos','[0]- Salir'])
        miMenu.showMenu()
        op = miMenu.selectOption() 
        while op != 0:
            #Registrar horas:
            if op == 1:
                dni = input('Ingrese DNI de empleado contratado: ')
                empC = empleados.searchEmpleadoC(dni)
                if empC != None:
                    empC.showEmpleado()
                    horas = input('Ingrese horas trabajadas: ')
                    empC.addHoras(horas)
                    empC.showEmpleado()
                input('Presione ENTER para continuar...')
            #Total de tarea
            elif op == 2:
                empleados.totalTarea()
            #Ayuda
            elif op == 3:
                empleados.listBeneficiarios()
                input('Presione ENTER para continuar...')
            #Calcular sueldo
            elif op == 4:
                empleados.listarEmpleados()
                input('Presione ENTER para continuar...')

            miMenu.showMenu()
            op = miMenu.selectOption() 
    except ValueError:
        print('La cantidad de empleados debe ser un entero')



