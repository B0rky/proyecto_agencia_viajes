from interfaz_usuario import *
import getpass

while True:
    print("═══════════════════════════════════════════════════════════")
    print("  BIENVENIDO AL PORTAL DE USUARIOS  ")
    print("═══════════════════════════════════════════════════════════")
    print("  1 - Iniciar Sesión ")
    print("  2 - Crear Cuenta Nueva")
    print("  3 - Salir del Portal")
    print("═══════════════════════════════════════════════════════════")
    opcion = int(input("ingrese una opción: "))

    try:
        if opcion == 1:
            usuario = input("ingrese nombre de usuario: ")
            contrasenia = getpass.getpass("ingrese contrasenia: ")
            acceso = Usuario.AutorizarUsuario(usuario, contrasenia)
            if acceso == True:
                print("Acceso concedido")
                menu_usuario()
            
        elif opcion == 2:
            nombre = input("Ingrese su nombre completo: ")
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            correo = input("Ingrese su correo: ")
            contrasenia = getpass.getpass("ingrese su contraseña: ")
            usuario = Usuario(nombre, nombre_usuario, correo, contrasenia)
            usuario.AgregarUsuario()
            
        elif opcion == 3:
            break

        else:
            print("opción incorrecta")
    except Exception as error:
        print("ocurrio un error: ", error)