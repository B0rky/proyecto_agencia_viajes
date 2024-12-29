from conexion import cursor
from argon2 import PasswordHasher 
import smtplib
from email.mime.text import MIMEText

ph = PasswordHasher()

# Tabla Destino
class Destino:
    def __init__(self, nombre, descripcion, actividades_disponibles, costo):
        self.__nombre = nombre 
        self.__descripcion = descripcion 
        self.__actividades_disponibles = actividades_disponibles
        self.__costo = costo
        
    def AgregarDestino(self):
        try:
            insert_qry = "INSERT INTO Destino(nombre, descripcion, actividades, costo) values (?, ?, ?, ?)"
            values_qry = self.__nombre, self.__descripcion, self.__actividades_disponibles, self.__costo
            cursor.execute(insert_qry, values_qry)
            cursor.commit()
            print("Se agregó un destino correctamente")
        except Exception as error:
            print(error)
            
    @staticmethod
    def __ModificarDestino(objetivo, nombre, descripcion, actividades, costo):
        try:
            update_qry = "UPDATE Destino set nombre = ?, descripcion = ?, actividades = ?, costo = ? where nombre = ?"
            values_qry = nombre, descripcion, actividades, costo
            cursor.execute(update_qry, values_qry, objetivo)
            cursor.commit()
            print(f"""Destino modificado exitosamente
                  nombre: {nombre}
                  descripcion: {descripcion}
                  actividades: {actividades}
                  costo: {costo}""")
            
        except Exception as error:
            print(error)
    
    @staticmethod
    def __EliminarDestino(nombre_destino):
        try:
            delete_qry = "DELETE FROM Destino where nombre = ?"
            cursor.execute(delete_qry, nombre_destino)
            cursor.commit()
            print(f"Destino {nombre_destino} eliminado exitosamente")
        except Exception as error:
            print(error)
    
    @staticmethod        
    def MostrarDestinos():
        try:
            select_qry = "SELECT * FROM Destino"
            cursor.execute(select_qry)
            data = cursor.fetchall()
            for i in data:
                print(f"""
                       || nombre: {i[1]}
                      descripcion: {i[2]}
                      actividades disponibles: {i[3]}
                      costo: {i[4]}
                      """)
        except Exception as error:
            print(error)
    
    # llamado de métodos privados - Seguridad
    @staticmethod
    def LlamarEliminación(nombre_destino):
        Destino.__EliminarDestino(nombre_destino)
    
    @staticmethod
    def LlamarModificación(nombre, descripcion, actividades, costo):
        Destino.__ModificarDestino(nombre, descripcion, actividades, costo)

# Tabla Paquete Turístico       
class PaqueteTuristico:
    def __init__(self, nombre_paquete, fecha_inicio, fecha_termino):
        self.__nombre_paquete = nombre_paquete
        self.__fecha_inicio = fecha_inicio 
        self.__fecha_termino = fecha_termino
       
    @staticmethod
    def mostrarPaquetes():
        try:
            select_qry = "SELECT nombre_paquete, fecha_inicio, fecha_termino FROM PaqueteTuristico"
            cursor.execute(select_qry)
            data = cursor.fetchall()
            for i in data:
                print(i)
            
            
        except Exception as error:
            print("No se pudo obtener los paquetes", error)
 
    # ADMINISTRADOR    
    def AgregarPaquete(self):
        try:
            insert_qry = "INSERT INTO PaqueteTuristico(nombre_paquete, fecha_inicio, fecha_termino) values (?, ?, ?)"
            values_qry = self.__nombre_paquete ,self.__fecha_inicio, self.__fecha_termino
            cursor.execute(insert_qry, values_qry)
            cursor.commit()
            print("Paquete turistico agregado exitosamente")
        except Exception as error:
            print(error)
            
    @staticmethod
    def __EliminarPaquete(nombre_pt):
        try:
            delete_qry = "DELETE FROM PaqueteTuristico where nombre_paquete = ?"
            cursor.execute(delete_qry, nombre_pt)
            cursor.commit()
            print("Paquete turistico eliminado exitosamente")
        except Exception as error:
            print(error)

    @staticmethod
    def ObtenerId(nombre_pt):
        try:
            select_qry = f"SELECT * FROM PaqueteTuristico where nombre_paquete = '{nombre_pt}'"
            cursor.execute(select_qry)
            data = cursor.fetchall()
            id_paquete = data[0]
            return id_paquete
            
        except Exception as error:
            print(error)
    
    def VerPrecioTotal(self, nombre_pt): # Se llama a través de un objeto vacio de almacenamiento volatil - funciona :D
        try:
            select_qry = "SELECT * FROM vista_detalle_paquete where nombre_paquete = ?"
            cursor.execute(select_qry, nombre_pt)
            data = cursor.fetchall()
            self.precio_final = data[4]
            print(f'nombre paquete: {data[0]} \n'
                  f'fecha de inicio: {data[1]} \n'
                  f'fecha de termino: {data[2]} \n'
                  f'destinos: {data[3]} \n'
                  f'precio final: {data[4]} \n')
            return self.precio_final
        except Exception as error:
            print(error)
    
    # Llamado de métodos privados 
    @staticmethod
    def LlamarEliminación(nombre_pt):
        PaqueteTuristico.__EliminarPaquete(nombre_pt)
    
# Tabla Usuario
class Usuario:
    def __init__(self, nombre, usuario, correo, contrasenia):
        self.__nombre = nombre 
        self.__usuario = usuario 
        self.__correo = correo
        self.__contrasenia = contrasenia
    
    
    def AgregarUsuario(self):
        try:
            insert_qry = "insert into Cliente (nombre, usuario, correo, contrasenia) values (?, ?, ?, ?)"
            cursor.execute(insert_qry, self.__nombre, self.__usuario, self.__correo, ph.hash(self.__contrasenia))
            cursor.commit()
            print(f'usuario {self.__usuario} agregado correctamente')
            print(f'en unos segundos llegará la confirmación a tu correo')
            
            msg = MIMEText('Gracias por inscribirte en la agencia de viajes de MauleSoft\n'
                           'Si no haz sido tu, puedes contactarnos a eduardo.buegueno09@inacapmail.cl')
            msg['Subject'] = 'Registro completo'
            msg['From'] = 'eduardo.bugueno09@inacapmail.cl'
            msg['To'] = f'{self.__correo}'
            
            with smtplib.SMTP('smtp.office365.com', 587) as server:
                server.starttls()
                server.login('eduardo.bugueno09@inacapmail.cl', 'Chacoman2005.10')
                server.sendmail(msg['From'], msg['To'], msg.as_string())
            
            print('Revisa tu correo')
            
        except Exception as error:
            print(error)
        
    @staticmethod
    def AutorizarUsuario(usuario, contraseña):
        try:
            select_qry = "SELECT contrasenia FROM Cliente where usuario = ?"
            cursor.execute(select_qry, usuario)
            data = cursor.fetchone()
            acceso = False
            if data:
                try:
                    ph.verify(data[0], contraseña)
                    print("sesión iniciada")
                    acceso = True
                    return acceso
                
                except Exception as e:
                    print("error ", e)
            else:
                print("usuario no encontrado")
                return acceso
        except Exception as e:
            print(f"error{e}")
            
    @staticmethod
    def ObtenerIdUsuario(usuario):
        try:
            select_qry = "SELECT id_cliente FROM Cliente where usuario = ?"
            cursor.execute(select_qry, usuario)
            data = cursor.fetchall()
            if data:
                id = data[0]
                return id
            else:
                print('No existe usuario o hubo un problema')
        except Exception as error:
            print(error)

# Tabla Reserva
class Reserva: 
    @staticmethod
    def CrearReserva(nombre_pt, usuario, contraseña):
        try:
            acceso = Usuario.AutorizarUsuario(usuario, contraseña)
            
            if acceso == True:
                id_paquete = PaqueteTuristico.ObtenerId(nombre_pt)
                id_usuario = Usuario.ObtenerIdUsuario(usuario)
                insert_qry = "insert into Reserva (id_cliente, id_paquete_turistico, fecha_reserva, estado) values (?, ?, GETDATE(), 1)"
                value_qry = id_usuario, id_paquete
                cursor.execute(insert_qry, value_qry)
                cursor.commit()
                print('Reserva creada con exito')
            else:
                print('No se pudo realizar la reserva, introducir credenciales correctas')

        except Exception as error:
            print(error)
    
    @staticmethod
    def VerReserva(usuario):
        try:
            select_qry = "SELECT * from vista_reserva where usuario = ?  "
            cursor.execute(select_qry, usuario)
            data = cursor.fetchall()
            for i in data:
                print(f"nombre cliente: {i[0]}\n"
                      f"correo cliente: {i[2]}\n"
                      f"fecha inicio: {i[3]}\n"
                      f"fecha termino: {i[4]}\n")

        except Exception as error:
            print("No se pudo obtener la reserva",error)
    
    @staticmethod
    def CancelarReserva(usuario, nombre_pt):
        try:
            id_usuario = Usuario.ObtenerIdUsuario(usuario)
            id_pt = PaqueteTuristico.ObtenerId(nombre_pt)
            data =  id_usuario, id_pt
            
            print("\nSeguro que desea cancelar las reservas?")
            opc = int(input(
                "\n1 - Para si\n" 
                "Cualquier numero - Para no\n"
                "Escriba numero de opcion: "))
            
            if opc == 1:
                delete_qry = "DELETE FROM Reserva WHERE id_usuario = ? AND id_paquete_turistico = ?"
                cursor.execute(delete_qry, data)
                cursor.commit()
                print("Se ha eliminado correctamente la reserva")
                
            else:
                print("Hasta luego")
            
        except Exception as error:
            print("No se pudo eliminar la reserva", error)

#Metodos:
#   DESTINO
#   nuevo_destino = Destino(nombre, descripcion, actividades_disponibles, costo)
#   nuevo_destino.AgregarDestino()
#
#   Destino.MostrarDestinos() - estático
#   Destino.LlamarEliminación(nombre_destino) - estático  
#   Destino.LlamarModificación(nombre, descripcion, actividades, costo)
#
#   PAQUETE TURISTICO
#   nuevo_paquete = PaqueteTuristico(destino, fecha_inicio, fecha_fin, precio, diponibilidad)
#   nuevo_paquete.AgregarPaquete()
#   
#   PaqueteTuristico.LlamarEliminación(nombre_pt)
#   PaqueteTuristico.VerDisponibilidad()
#   PaqueteTuristico.mostrarPaquetes()
#   PaqueteTuristico.ObtenerId(nombre_pt)
#   PaqueteTuristico.VerPrecioTotal(self, nombre_pt) - Objeto vacio almacena precio final para la compra
#   
#   RESERVA
#   Reserva.CrearReserva(nombre_pt, usuario, contraseña)
#   Reserva.VerReserva(usuario)
#   Reserva.CancelarReserva(usuario, nombre_pt)
#   
#   USUARIO
#   Usuario(nombre, usuario, correo, contrasenia)
#   Usuario.AgregarUsuario()
#   
#   Usuario.AutorizarUsuario(usuario, contraseña)
#   Usuario.ObtenerIdUsuario(usuario)
#   