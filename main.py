import sqlite3
import re
from errores import NombreError, ApellidoError, IdError, CorreoError, DniError, DescripcionError
import bcrypt
import json

name = ''
lastname = ''
dni = ''
mail = ''

global goLogin, dniok, nombreok, apellidook, correook
goLogin = False
dniok = False
nombreok = False
apellidook = False
correook = False


def get_info_by_dni(dni):
    try:
        # Connect to the database
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Execute a query to retrieve information based on DNI
        cursor.execute("SELECT dni, pasword,nombre, apellido, correo FROM usuarios WHERE dni=?", (dni,))

        # Fetch the result
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        return result

    except sqlite3.Error as e:
        print("Error connecting to database:", e)


# Example usage
dniLogin = ''  # Replace with the DNI you're searching for
def getInfo():
    global dni, name, lastname, mail
    info = get_info_by_dni(dniLogin)
    if info:
        dni=info[0]
        name = info[2]
        lastname = info[3]
        mail = info[4]
        print(dni,name,lastname,mail)
    else:
        print("No information found for the given DNI.")
    return dni,name,lastname,mail

"""
self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dniLogin,))
usuario = self.cursor.fetchone()
dni = usuario[0]
nombre = usuario[2]
apellido = usuario[3]
corre = usuario[4]
    contrasena_hasheada = usuario[1]  # La contraseña hasheada está en la segunda posición"""



"""
def process(self,username,password,window):
    print(username,password)
    self.register()
    self.loginWindow.close()"""

def registerInfo(self,name,lastname,dni,mail,password,window):
    pass
    #print(name,lastname,dni,mail,password)
    #return [name,lastname,dni,mail,password]
    #self.registerWindow.close()

def botonRegistro(self,name,lastname,dni,mail,password,window):
    #print(name,lastname,dni,mail,password)
    usuario = UsuarioBase()
    usuario.crear_usuario(dni,password,name,lastname,mail)

def botonLogin(self,dni,password,window):
    usuario = UsuarioBase()
    usuario.login_usuario(dni,password)


#------------Proyecto-----------
# Clase que nos permite gestionar los proyectos del sistema
class GestorSistema:
    '''
    Descripcion Clase:
    Esta clase se encarga de crear proyectos añadiéndolos a un usuario, además de eliminar los deseados y visualizarlos.

    Parámetros Clase:
    proyectos: Almacena los proyectos creados.

    Métodos clase:
    guardar_proyectos_json: Será llamada en las otras clases cuando se quieran guardar proyectos en un archivo json.
    cargar_proyectos_json: Será llamada cuando se quiera abrir el archivo json de los proyectos en modo lectura.
    add_proyecto: Encargado de añadir proyectos y asignárselos a un usuario.
    eliminar_proyecto: Encargado de eliminar los proyectos que se requieran.
    ver_proyecto: Encargado de ver los proyectos deseados en el archivo.
    '''
    # Método constructor que inicializa el diccionario self.proyectos
    def __init__(self):
        self.proyectos = {}
        self.usuario_base = UsuarioBase()

    # Encargada de escribir en el archivo que almacena los proyectos
    def guardar_proyectos_json(self, filename):
        # Abrimos el archivo json en modo escritura
        with open(filename, 'w') as json_file:
            # Añadimos a este el proyecto creado
            json.dump(self.proyectos, json_file, indent=4)

    # Encargada de abrir el archivo json de los proyectos en modo lectura
    def cargar_proyectos_json(self, filename):
        # Probamos a abrir el archivo
        try:
            # Abrimos el archivo en modo lectura
            with open(filename, 'r') as json_file:
                # Si existe el archivo lo guardamos el diccionario del archivo en el parámetro self.proyectos
                self.proyectos = json.load(json_file)
        # Si no existe el archivo salta el error FileNotFoundError
        except FileNotFoundError:
            # Si no existe, inicializamos self.proyectos como un diccionario vacío
            self.proyectos = {}

    def validar_descripcion(self, descripcion_proyecto):
        # Probamos a ver si la descripción es válida
        try:
            # Si la descripción contiene más de 80 caracteres
            if len(descripcion_proyecto) > 80:
                # Lanza el error DescripcionError
                raise DescripcionError
        # Si salta el error
        except DescripcionError as ex:
            # Imprimimos el error
            print(ex)
            descripcion_validada = False
            # Si la descripción es válida
        else:
            descripcion_validada = True
        return descripcion_validada

    # Método que crea proyectos y los almacena
    def add_proyecto(self,dni,nombre_proyecto,descripcion_proyecto):
        descripcion_validada=self.validar_descripcion(descripcion_proyecto)

        if descripcion_validada:
            # Llamamos al método que abre el archivo y carga los proyectos dentro de self.proyectos
            self.cargar_proyectos_json('proyectos.json')

            # Verificamos si el usuario existe en la base de datos
            self.usuario_base.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.usuario_base.cursor.fetchone()
            if not usuario:
                print("El usuario con ese DNI no existe.")
                return

            # Buscamos el número de proyectos creados para el usuario
            if dni in self.proyectos:
                id_max_proyecto = max(int(id) for id in self.proyectos[dni].keys())
            else:
                id_max_proyecto = 0

            # Guardamos el número de proyectos creados + 1 en id_proyecto, el cual será el id del proyecto
            id_proyecto = id_max_proyecto + 1

            # Añadimos el proyecto al diccionario self.proyectos donde key es el DNI del usuario y value es un
            # diccionario con los proyectos del usuario
            if dni not in self.proyectos:
                self.proyectos[dni] = {}

            self.proyectos[dni][id_proyecto] = {
                'nombre_proyecto': nombre_proyecto,
                'descripcion_proyecto': descripcion_proyecto,
                'tareas_proyecto': {}
            }

            # Guardamos el diccionario actualizado en el archivo proyectos.json llamando a la función correspondiente
            self.guardar_proyectos_json('proyectos.json')
        else:
            print('Credenciales invalidas')

    # Método que se encarga de eliminar proyectos existentes
    def eliminar_proyecto(self):
        # Cargamos los proyectos existentes en self.proyectos llamando a la función que los abre
        self.cargar_proyectos_json('proyectos.json')

        print("Proyectos existentes:")
        # Visualizamos todos los proyectos recorriendotodo el diccionario con un for key, value in .items()
        for dni, proyectos_usuario in self.proyectos.items():
            for id_proyecto, proyecto in proyectos_usuario.items():
                # Imprimimos los proyectos
                print(f"DNI: {dni}, ID: {id_proyecto}, Nombre: {proyecto['nombre_proyecto']}, Descripción: {proyecto['descripcion_proyecto']}")

        # Introducimos el DNI del usuario y el ID del proyecto que desea eliminar
        dni = input("Ingrese el DNI del usuario: ")
        id_a_eliminar = input("Ingrese el ID del proyecto que desea eliminar: ")

        # Si el DNI y el ID existen
        if dni in self.proyectos and id_a_eliminar in self.proyectos[dni]:
            # Eliminamos el proyecto cuyo id se ha introducido
            del self.proyectos[dni][id_a_eliminar]
            # Si el usuario no tiene más proyectos, eliminamos el DNI del diccionario
            if not self.proyectos[dni]:
                del self.proyectos[dni]
            print("Proyecto eliminado.")
            # Guardamos el diccionario actualizado en archivo json llamando a la función que guarda los proyectos
            self.guardar_proyectos_json('proyectos.json')
        # Si no existe
        else:
            # Imprimimos que no existe
            print("ID de proyecto o DNI no válido.")

    # Método que permite ver los proyectos
    def ver_proyecto(self):
        # Llamamos a la función cargar proyectos y cargamos los proyectos en self.proyectos
        self.cargar_proyectos_json('proyectos.json')
        print("Proyectos existentes:")
        # Visualizamos todos los proyectos recorriendotodo el diccionario con un for key, value in .items()
        for dni, proyectos_usuario in self.proyectos.items():
            for id_proyecto, proyecto in proyectos_usuario.items():
                # Imprimimos los proyectos
                print(f"DNI: {dni}, ID: {id_proyecto}, Nombre: {proyecto['nombre_proyecto']}, Descripción: {proyecto['descripcion_proyecto']}, Tareas: {proyecto['tareas_proyecto']}")



# -----------Usuario------------
class Usuario:
    def __init__(self, dni, contrasena, nombre, apellido, correo):
        self.dni = dni
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}"


class UsuarioBase:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS usuarios ('
            'dni TEXT UNIQUE, '
            'pasword TEXT NOT NULL,'
            'nombre TEXT, '
            'apellido TEXT,'
            'correo TEXT)'
        )
        self.conn.commit()

    def consultar_usuarios(self):
        self.cursor.execute('SELECT * FROM usuarios')
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
        '''self.cursor.execute('SELECT * FROM usuarios')
        usuarios = self.cursor.fetchall()
        df = pd.DataFrame(usuarios, columns=['DNI', 'Password', 'Nombre', 'Apellido', 'Correo'])
        print(df)'''

    # Función que hashea las contraseñas
    def hashear_contrasena(self, contrasena):
        # Con bcrypt.hashpw creamos un hash de la contraseña
        # contrasena.encode() convierte la contraseña a bytes
        # bcrypt.gensalt() añade un valor al hasheo de la contraseña para asegurar que nadie comparta contraseña
        contrasena_hasheada = bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
        return contrasena_hasheada

    # Función que comprueba si el hash coincide con la contraseña
    def validar_hasheo(self, contrasena, contrasena_hasheada):
        # bcrypt.checkpw() compara las contraseñas y devuelve True si coinciden o false si no
        # contrasena.encode() convierte la contraseña a bytes
        verificacion = bcrypt.checkpw(contrasena.encode(), contrasena_hasheada)
        return verificacion

    def validar_dni(self, dni):
        global dniok
        valido = r'[0-9]{8}[A-Z]'
        try:
            if not re.match(valido, dni):
                raise DniError(dni)
        except DniError as de:
            dni_validado = False
            print(de)
        else:
            dniok = True
            dni_validado = True

        return dni_validado

    def validar_nombre(self, nombre):
        global nombreok
        try:
            if not nombre.isalpha():
                raise NombreError(nombre)
        except NombreError as ne:
            print(ne)
            nombre_validado = False
        else:
            nombreok = True
            nombre_validado = True

        return nombre_validado

    def validar_apellidos(self, apellido):
        global apellidook
        try:
            if not apellido.isalpha():
                raise ApellidoError(apellido)
        except ApellidoError as ae:
            apellido_validado = False
            print(ae)
        else:
            apellidook = True
            apellido_validado = True

        return apellido_validado

    def validar_correo(self, correo):
        global correook
        valido = r'[a-zA-Z0-9._]+@[a-z]+\.[a-zA-Z]{2,}'
        try:
            if not re.match(valido, correo):
                raise CorreoError(correo)
        except CorreoError as ce:
            correo_validado = False
            print(ce)
        else:
            correook = True
            correo_validado = True

        return correo_validado

    def crear_usuario(self, dni, contrasena, nombre, apellido, correo):
        global goLogin
        dni_validado = self.validar_dni(dni)
        nombre_validado = self.validar_nombre(nombre)
        apellido_validado = self.validar_apellidos(apellido)
        correo_validado = self.validar_correo(correo)

        if dni_validado and nombre_validado and apellido_validado and correo_validado:
            goLogin = True
            contrasena_hasheada = self.hashear_contrasena(contrasena)
            self.cursor.execute(
                'INSERT INTO usuarios (dni, pasword,nombre, apellido, correo) VALUES (?, ?,?, ?, ?)',
                (dni, contrasena_hasheada, nombre, apellido, correo)
            )
            self.conn.commit()
            print("Usuario creado correctamente.")
            Usuario(dni, contrasena_hasheada, nombre, apellido, correo)

        else:
            goLogin = False
            print('ERROR!')

    def editar_usuario(self):
        dni = self.validar_dni(self.dniRegister.text())
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise DniError(dni)
        except DniError as ex:
            print(ex)
            return

        print('Para editar el Nombre introduzca el 1.')
        print('Para editar el Apellido introduzca el 2.')
        print('Para editar el correo introduzca el 3.')
        editar = int(input('Elige que quieres editar: '))

        if editar == 1:
            nombre = self.validar_nombre()
            self.cursor.execute('UPDATE usuarios SET nombre = ? WHERE dni = ?', (nombre, dni))
            self.conn.commit()
        elif editar == 2:
            apellido = self.validar_apellidos()
            self.cursor.execute('UPDATE usuarios SET apellido = ? WHERE dni = ?', (apellido, dni))
            self.conn.commit()
        elif editar == 3:
            correo = self.validar_correo()
            self.cursor.execute('UPDATE usuarios SET correo = ? WHERE dni = ?', (correo, dni))
            self.conn.commit()

        print("Usuario editado correctamente.")

    def eliminar_usuario(self):
        dni = self.validar_dni(self.dniRegister.text())
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise DniError(dni)
        except DniError as ex:
            print(ex)
            return

        self.cursor.execute('DELETE FROM usuarios WHERE dni = ?', (dni,))
        self.conn.commit()
        print(f"Usuario con DNI {dni}, eliminado correctamente.")

    def login_usuario(self, dni, contrasena):
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise DniError(dni)
        except DniError as ex:
            print(ex)
        else:
            contrasena_hasheada = usuario[1]  # La contraseña hasheada está en la segunda posición
            if self.validar_hasheo(contrasena, contrasena_hasheada):
                print(
                    f"Bienvenido {usuario[2]} {usuario[3]}")  # Asumiendo que nombre y apellido están en las posiciones 2 y 3
                usuario_login = Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])
                print(usuario_login)
                dni = usuario_login.dni
                nombre = usuario_login.nombre
                apellido = usuario_login.apellido
                correo = usuario_login.correo

            else:
                print("Contraseña incorrecta")

        return dni, nombre, apellido, correo