import sqlite3
import re

import main
from errores import NombreError, ApellidoError, IdError, CorreoError, DniError, DescripcionError, ProyectoNoEncontradoError, TituloError
import bcrypt
import json

boton_proyecto = 0
boton_tareas = 0

name = ''
lastname = ''
dni = ''
mail = ''

idproyecto = ''
nombre_proyecto = ''
descripcion_proyecto = ''

idtarea = ''
nombre_tarea = ''
descripcion_tarea = ''
estado_tarea = ''

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
    def ver_proyecto(self, dni):
        global boton_proyecto
        global idproyecto
        global nombre_proyecto
        global descripcion_proyecto

        # Cargamos los proyectos desde proyectos.json
        with open('proyectos.json', 'r') as json_file:
            proyectos = json.load(json_file)

        # Extraemos los proyectos del usuario especificado por el dni
        proyectos_usuario = proyectos.get(dni, {})
        #cantidad_proyectos = len(proyectos_usuario)

        idproyecto = str(boton_proyecto)
        #cantidad_tareas = len(proyectos_usuario[idproyecto]['tareas_proyecto'])
        nombre_proyecto = proyectos_usuario[idproyecto]['nombre_proyecto']
        descripcion_proyecto = proyectos_usuario[idproyecto]['descripcion_proyecto']
        print(idproyecto, nombre_proyecto, descripcion_proyecto)



        print('-----------')
    def ver_tareas(self,dni):
        global boton_tareas
        global boton_proyecto
        global idtarea
        global nombre_tarea
        global descripcion_tarea
        global estado_tarea

        print(boton_proyecto)

        with open('proyectos.json', 'r') as json_file:
            proyectos = json.load(json_file)
        proyectos_usuario = proyectos.get(dni, {})
        idtarea = str(boton_tareas + 1)
        print()
        if proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'] != {}:
            nombre_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['titulo']
            descripcion_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['descripcion']
            estado_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['estado']
            print(idtarea, nombre_tarea, descripcion_tarea, estado_tarea)
        else:
            nombre_tarea = 'No tienes tareas'
            descripcion_tarea = 'No tienes tareas'
            estado_tarea = 'pendiente'
            print(idtarea, nombre_tarea, descripcion_tarea, estado_tarea)

class Tarea:
    def cambiar_pendiente(self):
        global idtarea
        global idproyecto
        global dni

        # Abrimos el archivo
        with open('proyectos.json', 'r') as json_file:
            # Guardamos el diccionario perteneciente al json en el atributo proyectos
            proyectos = json.load(json_file)

        proyectos[dni][idproyecto]['tareas_proyecto'][idtarea]['estado'] = "pendiente"

        # Abrimos el archivo json en modo escritura
        with open('proyectos.json', 'w') as json_file:
            # Guardamos en él, el diccionario proyectos actualizado
            json.dump(proyectos, json_file, indent=4)

    def cambiar_en_curso(self):
        global idtarea
        global idproyecto
        global dni

        # Abrimos el archivo
        with open('proyectos.json', 'r') as json_file:
            # Guardamos el diccionario perteneciente al json en el atributo proyectos
            proyectos = json.load(json_file)

        proyectos[dni][idproyecto]['tareas_proyecto'][idtarea]['estado'] = "en curso"

        # Abrimos el archivo json en modo escritura
        with open('proyectos.json', 'w') as json_file:
            # Guardamos en él, el diccionario proyectos actualizado
            json.dump(proyectos, json_file, indent=4)

    def cambiar_completada(self):
        global idtarea
        global idproyecto
        global dni

        # Abrimos el archivo
        with open('proyectos.json', 'r') as json_file:
            # Guardamos el diccionario perteneciente al json en el atributo proyectos
            proyectos = json.load(json_file)

        proyectos[dni][idproyecto]['tareas_proyecto'][idtarea]['estado'] = "completada"

        # Abrimos el archivo json en modo escritura
        with open('proyectos.json', 'w') as json_file:
            # Guardamos en él, el diccionario proyectos actualizado
            json.dump(proyectos, json_file, indent=4)

    def __str__(self):
        return f'Id: {self.id_tarea}, {self.titulo}: {self.descripcion}. {self.estado}.'


class Proyecto:
    '''
    Descripcion Clase:
    Esta clase se encargará de permitir que la clase GestorSistema pueda llamarla para crear proyectos.
    Además, será la encargada de añadir tareas al proyecto, además de visualizarlas

    Parametros Clase:
    id_proyecto: Identificador del proyecto, lo hace diferente del resto
    id_usuario: Identificador del usuario al que se le ha asignado el proyecto
    nombre: Nombre del proyecto
    descripcion: Descripcion del proyecto, de que trata

    Métodos Clase:
    __init__: Inicializa los parametros comentados anteriormente permitiendo la creacion de un proyecto al llamarla en
    la clase GestorSistema.
    agregar_tarea: Encargado de agregar tareas al proyecto desado almacenandolas en un archivo json
    mostrar_tarea: Encargado de mostrar las tarea que tiene un proyecto
    '''

    # Constructor de la clase, inicializa los parametros
    def __init__(self):
        self.tareas = []

    def verificar_titulo(self, titulo):
        # Probamos a escribir el título
        try:
            if not titulo:
                # Lanzamos el error TituloError
                raise TituloError("El título no puede estar vacío")
        # Si el error salta
        except TituloError as te:
            # Imprimimos error
            print(te)
            titulo_verificado = False
        # Si el título es válido
        else:
            titulo_verificado = True
        return titulo_verificado

    def verificar_descripcion(self, descripcion):
        try:
            if len(descripcion) > 80:
                # Se lanza el error DescripcionError
                raise DescripcionError("La descripción no puede exceder los 80 caracteres")
        # Si el error salta
        except DescripcionError as de:
            # Imprimimos el error
            print(de)
            descripcion_validada = False
        # Si la descripción es correcta
        else:
            descripcion_validada = True
        return descripcion_validada

    # Método encargado de añadir tareas al proyecto
    def agregar_tarea(self, dni, id_proyecto, nombre, descripcion):
        try:
            with open('proyectos.json', 'r') as json_file:
                # Cargamos el diccionario desde el archivo JSON
                proyectos = json.load(json_file)
        except FileNotFoundError:
            print("Archivo proyectos.json no encontrado")
            return
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON")
            return
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")
            return

        # Verificamos si el DNI y el ID del proyecto existen en el diccionario
        if dni in proyectos and str(id_proyecto) in proyectos[dni]:
            proyecto_actual = proyectos[dni][str(id_proyecto)]

            # Inicializamos el ID de la tarea
            if "tareas_proyecto" in proyecto_actual:
                id_tarea = max((int(key) for key in proyecto_actual["tareas_proyecto"].keys()), default=0) + 1
            else:
                proyecto_actual["tareas_proyecto"] = {}
                id_tarea = 1
        else:
            print("Usuario o proyecto no encontrado")
            return

        # Validamos el nombre y la descripción
        titulo_verificado= self.verificar_titulo(nombre)
        descripcion_validada = self.verificar_descripcion(descripcion)
        estado = 'pendiente'

        if descripcion_validada:
            nueva_tarea = {
                'id': id_tarea,
                'titulo': nombre,
                'descripcion': descripcion,
                'estado': estado
            }

            # Añadimos la nueva tarea al proyecto
            proyecto_actual["tareas_proyecto"][str(id_tarea)] = nueva_tarea

            try:
                # Guardamos el diccionario actualizado en el archivo JSON
                with open('proyectos.json', 'w') as json_file:
                    json.dump(proyectos, json_file, indent=4)

                print("Tarea agregada correctamente")
            except Exception as e:
                print(f"Error inesperado al escribir el archivo: {e}")
        else:
            print("Nombre o descripción no válidos")

    # Método que nos permite visualizar las tareas del proyecto
    def mostrar_tarea(self):
        # Probamos a abrir el archivo json en modo lectura
        try:
            with open('proyectos.json', 'r') as json_file:
                # Guardamos el diccionario del json en el atributo proyectos
                proyectos = json.load(json_file)
        except FileNotFoundError:
            print("Archivo de proyectos no encontrado.")
            return

        # Verificamos si el DNI del usuario y el ID del proyecto existen
        if self.dni in proyectos and str(self.id_proyecto) in proyectos[self.dni]:
            # Obtenemos las tareas del proyecto
            tareas = proyectos[self.dni][str(self.id_proyecto)].get('tareas_proyecto', {})
            # Si hay tareas, las imprimimos
            if tareas:
                print(f'Tareas del proyecto {self.id_proyecto}:')
                for id_tarea, tarea in tareas.items():
                    print(
                        f"ID: {id_tarea}, Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}")
            else:
                print("No hay tareas en este proyecto.")
        else:
            print("Proyecto o usuario no encontrado.")


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

    def editar_usuario(self, dni, nombre, apellido, correo):
        nombre_validado = self.validar_nombre(nombre)
        apellido_validado = self.validar_apellidos(apellido)
        correo_validado = self.validar_correo(correo)

        if nombre_validado and apellido_validado and correo_validado:
            self.cursor.execute('UPDATE usuarios SET nombre = ? WHERE dni = ?', (nombre, dni))
            self.conn.commit()
            self.cursor.execute('UPDATE usuarios SET apellido = ? WHERE dni = ?', (apellido, dni))
            self.conn.commit()
            self.cursor.execute('UPDATE usuarios SET correo = ? WHERE dni = ?', (correo, dni))
            self.conn.commit()
            print("Usuario editado correctamente.")

    def eliminar_usuario(self, dni):

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