from interfaz_administrador import *
from interfaz_usuario import *

while True:
    print("═══════════════════════════════════════════════════════════")
    print("           SISTEMA DE ADMINISTRACIÓN PRINCIPAL             ")
    print("═══════════════════════════════════════════════════════════")
    print("🔹 1  |  opciones destino")
    print("🔹 2  |  opciones paquete") 
    print("🔹 3  |  opciones cliente")
    print("🔹 5  |  salir")
    print("═══════════════════════════════════════════════════════════")

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opcion = int(input("elija una opción (1-3): "))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    if opcion == 1:
        menu_destino() 

    elif opcion == 2:
        menu_paquete()

    elif opcion == 3:
        menu_usuario()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.\n")