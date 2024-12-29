from modelo import *

def menu_destino():
    while True:
        print("menu destinos")
        print("1. agregar destino")
        print("2. modificar destino")
        print("3. eliminar destino")
        print("4. mostrar destinos")
        print("5. Salir")
        op = int(input("ingrese numero de opción: "))

        if op == 1:
            nombre = input("ingrese nombre del detino: ")
            descripcion = input("ingrese descripcion del destino: ")
            actividades = input("ingrese actividades: ")
            costo = int(input("ingrese costo del destino: "))
            Destino(nombre, descripcion, actividades, costo).AgregarDestino()
            print("Destino agregado correctamente")
        
        elif op == 2:
            objetivo = input("Escriba el nombre del destino que desea modificar: ")
            nombre = input("ingrese nombre del detino: ")
            descripcion = input("ingrese descripcion del destino: ")
            actividades = input("ingrese actividades: ")
            costo = int(input("ingrese costo del destino: "))
            Destino.LlamarModificación(objetivo, nombre, descripcion, actividades, costo)
            print("Destino modificado correctamente ")

        elif op == 3:
            nombre = input("ingrese nombre: ")
            Destino.LlamarEliminación(nombre)

        elif op == 4:
            Destino.MostrarDestinos()
        
        elif op == 5:
            break


def menu_paquete():

    print("menu destinos")
    print("1. agregar paquete")
    print("2. eliminar paquete")
    print("3. mostrar paquetes")

    op = int(input("ingrese opción"))

    if op ==1:
        nombre = input("ingrese nombre del paquete: ")
        fecha_inicio = input("ingrese fecha de inicio en el formato yy-mm-dd: ")
        fecha_termino = input("ingrese fecha de termino en el formato yy-mm-dd: ")
        PaqueteTuristico(nombre, fecha_inicio, fecha_termino).AgregarPaquete()

    elif op ==2:
        nombre = input("ingrese nombre del paquete: ")
        PaqueteTuristico.LlamarEliminación(nombre)

    elif op ==3:
        PaqueteTuristico.mostrarPaquetes()
            

            


 
