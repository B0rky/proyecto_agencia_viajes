from modelo import *
from argon2 import PasswordHasher
from modelo import *
ph = PasswordHasher()

def menu_usuario():
    while True:
        print("1 - Paquete Turistico y reservas\n"
              "2 - Opciones de usuario\n"
              "3 - cerrar sesión de usuario\n")
        
        operacion = int(input("Ingrese numero de opción: "))
        
        
        if operacion == 1:
           menu_reserva()
        elif operacion == 2:
            opciones_usuario()
            
        elif operacion == 3:
            break
        
        else:
            print("opción invalida")


def menu_reserva():
    while True: 
        print("Puedes realizar las siguientes opciones:\n"
                    "1 - Realizar Reserva\n"
                    "2 - Ver reserva\n"
                    "3 - Cancelar reserva\n"
                    "4 - Salir")
         
        opcion = int(input("Escriba el numero de la acción que desea realizar: "))

        if opcion == 1:
            print("1 - Ver precio total del paquete\n"
                  "2 - Salir\n")
            op = int(input("Ingrese numero de opción: "))
            
            if op == 1:
                PaqueteTuristico.mostrarPaquetes()
                destino = input("Ingrese nombre del destino que desea: ")
                paquete = PaqueteTuristico(destino, '', '', 0)
                paquete.VerPrecioTotal(destino)

                print("1 - Reservar\n"
                      "2 - Salir\n")
                
                op == int(input("Desea reservar el paqeute turistico?: "))
                
                if op == 1:
                    usuario = input('ingrese nombre de usuario: ')
                    contrasenia = input('ingrese contrasenia: ')
                    Reserva.CrearReserva(destino, usuario, contrasenia)

        elif opcion == 2:
            usuario = input('ingrese nombre de usuario: ')
            contrasenia = input('ingrese contrasenia: ')
            acceso = Usuario.AutorizarUsuario(usuario, contrasenia)
            if acceso == True:
                Reserva.VerReserva(usuario)
            else:
                print("No tiene reserva agendada")

        elif opcion == 3:
            usuario = input('ingrese usuario: ')
            contrasenia = input('ingrese contrasenia: ')
            acceso = Usuario.AutorizarUsuario(usuario, contrasenia)
            if acceso == True:
                Reserva.VerReserva(usuario)
                nombre_pt = input("Ingrese el nombre del paquete reservado que quiere cancelar: ")
                Reserva.CancelarReserva(usuario, nombre_pt)
            else:
                print("No tiene reserva agendada")
        
        elif opcion == 4:
            break
        
        else:
            print("opción erronea")
            
def opciones_usuario():
    pass



                    