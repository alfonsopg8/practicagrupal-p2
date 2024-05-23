from errores import NombreError, ApellidoError, CorreoError, DniError, DescripcionError,TituloError,ContrasenaLoginError
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import bcrypt
import json
import re

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
contrasenyaok = False

# Funciones get into by dni y get info, para a partir de el dni del login, conseguir la
# informacion restante del usuario. Necesario para uso correcto de interfaz
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
    return dni,name,lastname,mail


def botonRegistro(self,name,lastname,dni,mail,password,window):
    usuario = UsuarioBase()
    usuario.crear_usuario(dni,password,name,lastname,mail)

def botonLogin(self,dni,password,window):
    usuario = UsuarioBase()
    usuario.login_usuario(dni,password)

class UsuarioBase:
    '''
        Clase para la gestión de usuarios en la base de datos

        Métodos
        -------
        __init__()
            Inicializa la conexión a la base de datos y crea la tabla de usuarios si no existe.

        consultar_usuarios()
            Consulta todos los usuarios en la base de datos.

        hashear_contrasena(contrasena)
            Hashea la contraseña proporcionada.

        validar_hasheo(contrasena, contrasena_hasheada)
            Valida si el hash coincide con la contraseña proporcionada.

        validar_dni(dni)
            Valida el formato del DNI.

        validar_nombre(nombre)
            Valida el formato del nombre.

        validar_apellidos(apellido)
            Valida el formato del apellido.

        validar_correo(correo)
            Valida el formato del correo electrónico.

        crear_usuario(dni, contrasena, nombre, apellido, correo)
            Crea un nuevo usuario en la base de datos.

        editar_usuario(dni, nombre, apellido, correo)
            Edita la información de un usuario existente.

        eliminar_usuario(dni)
            Elimina un usuario de la base de datos.

        login_usuario(dni, contrasena)
            Inicia sesión con las credenciales proporcionadas.
        '''

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

    # Función que hashea las contraseñas
    def hashear_contrasena(self, contrasena):
        '''
                Hashea la contraseña proporcionada.

                Parameters
                ----------
                contrasena : str
                    Contraseña a ser hasheada.

                Returns
                -------
                bytes
                    Contraseña hasheada.
                '''
        # Con bcrypt.hashpw creamos un hash de la contraseña
        # contrasena.encode() convierte la contraseña a bytes
        # bcrypt.gensalt() añade un valor al hasheo de la contraseña para asegurar que nadie comparta contraseña
        contrasena_hasheada = bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
        return contrasena_hasheada

    # Función que comprueba si el hash coincide con la contraseña
    def validar_hasheo(self, contrasena, contrasena_hasheada):
        '''
                Valida si el hash coincide con la contraseña proporcionada.

                Parameters
                ----------
                contrasena : str
                    Contraseña en texto plano.
                contrasena_hasheada : bytes
                    Contraseña hasheada.

                Returns
                -------
                bool
                    True si coinciden, False en caso contrario.
                '''
        # bcrypt.checkpw() compara las contraseñas y devuelve True si coinciden o false si no
        # contrasena.encode() convierte la contraseña a bytes
        verificacion = bcrypt.checkpw(contrasena.encode(), contrasena_hasheada)
        return verificacion

    def validar_dni(self, dni):
        '''
                Valida el formato del DNI.

                Parameters
                ----------
                dni : str
                    DNI a validar.

                Returns
                -------
                bool
                    True si el DNI es válido, False en caso contrario.
                '''
        global dniok
        # Expresion regular para validar dni
        valido = r'[0-9]{8}[A-Z]'
        try:
            if not re.match(valido, dni):
                raise DniError(dni)
        except DniError as de:
            dni_validado = False
        else:
            dniok = True
            dni_validado = True

        return dni_validado

    def validar_nombre(self, nombre):
        '''
                Valida el formato del nombre.

                Parameters
                ----------
                nombre : str
                    Nombre a validar.

                Returns
                -------
                bool
                    True si el nombre es válido, False en caso contrario.
                '''
        global nombreok
        try:
            if not nombre.isalpha():
                raise NombreError(nombre)
        except NombreError as ne:
            nombre_validado = False
        else:
            nombreok = True
            nombre_validado = True

        return nombre_validado

    def validar_apellidos(self, apellido):
        '''
                Valida el formato del apellido.

                Parameters
                ----------
                apellido : str
                    Apellido a validar.

                Returns
                -------
                bool
                    True si el apellido es válido, False en caso contrario.
                '''
        global apellidook
        try:
            if not apellido.isalpha():
                raise ApellidoError(apellido)
        except ApellidoError as ae:
            apellido_validado = False
        else:
            apellidook = True
            apellido_validado = True

        return apellido_validado

    def validar_correo(self, correo):
        '''
                Valida el formato del correo electrónico.

                Parameters
                ----------
                correo : str
                    Correo electrónico a validar.

                Returns
                -------
                bool
                    True si el correo es válido, False en caso contrario.
                '''
        global correook
        valido = r'[a-zA-Z0-9._]+@[a-z]+\.[a-zA-Z]{2,}'
        try:
            if not re.match(valido, correo):
                raise CorreoError(correo)
        except CorreoError as ce:
            correo_validado = False
        else:
            correook = True
            correo_validado = True

        return correo_validado

    def crear_usuario(self, dni, contrasena, nombre, apellido, correo):
        '''
                Crea un nuevo usuario en la base de datos.

                Parameters
                ----------
                dni : str
                    DNI del usuario.
                contrasena : str
                    Contraseña del usuario.
                nombre : str
                    Nombre del usuario.
                apellido : str
                    Apellido del usuario.
                correo : str
                    Correo electrónico del usuario.
                '''
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
        else:
            goLogin = False

    def editar_usuario(self, dni, nombre, apellido, correo):
        '''
                Edita la información de un usuario existente.

                Parameters
                ----------
                dni : str
                    DNI del usuario.
                nombre : str
                    Nuevo nombre del usuario.
                apellido : str
                    Nuevo apellido del usuario.
                correo : str
                    Nuevo correo electrónico del usuario.
                '''
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

    def eliminar_usuario(self, dni):
        '''
                Elimina un usuario de la base de datos.

                Parameters
                ----------
                dni : str
                    DNI del usuario a eliminar.
                '''
        self.cursor.execute('DELETE FROM usuarios WHERE dni = ?', (dni,))
        self.conn.commit()

    def login_usuario(self, dni, contrasena):
        '''
                Inicia sesión con las credenciales proporcionadas.

                Parameters
                ----------
                dni : str
                    DNI del usuario.
                contrasena : str
                    Contraseña del usuario.

                Returns
                -------
                bool
                    True si el inicio de sesión es exitoso, False en caso contrario.
                '''
        global contrasenyaok
        self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
        usuario = self.cursor.fetchone()
        try:
            contrasena_hasheada = usuario[1]
            # La contraseña hasheada está en la segunda posición
            if not self.validar_hasheo(contrasena, contrasena_hasheada):
                raise ContrasenaLoginError(contrasena)
        except ContrasenaLoginError:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 500px;min-height: 100px;}")
            msg.setText("Contraseña incorrecta!")
            msg.exec_()
            contrasenyaok = False
        else:
            contrasenyaok = True

        finally:
            self.cursor.close()
            self.conn.close()

#------------Proyecto-----------
# Clase que nos permite gestionar los proyectos del sistema
class GestorSistema:
    '''
    Descripcion Clase:
    Esta clase se encarga de crear proyectos añadiéndolos a un usuario, además de visualizarlos junto
    a sus tareas.

    Parámetros Clase:
    proyectos: Almacena los proyectos creados.

    Métodos clase:
    init: Inicializa el atributo self.proyectos
    guardar_proyectos_json: Será llamada en las otras clases cuando se quieran guardar proyectos en un archivo json.
    cargar_proyectos_json: Será llamada cuando se quiera abrir el archivo json de los proyectos en modo lectura.
    validar_descripcion: Valida la Descripcion y comprueba que sea valida.
    add_proyecto: Encargado de añadir proyectos y asignárselos a un usuario.
    ver_proyecto: Encargado de ver los proyectos deseados en el archivo.
    ver_tareas: Encargado de visualizar las tareas deseados
    '''
    def __init__(self):
        self.proyectos = {}
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
        '''
                Valida la descripción del proyecto.

                Parámetros
                ----------
                descripcion_proyecto : str
                    Descripción del proyecto a validar.

                Devuelve
                -------
                bool
                    True si la descripción es válida, False en caso contrario.
                '''
        # Probamos a ver si la descripción es válida
        try:
            # Si la descripción contiene más de 80 caracteres
            if len(descripcion_proyecto) > 80:
                # Lanza el error DescripcionError
                raise DescripcionError
        # Si salta el error
        except DescripcionError as ex:
            # Imprimimos el error
            descripcion_validada = False
            # Si la descripción es válida
        else:
            descripcion_validada = True
        return descripcion_validada

    # Método que crea proyectos y los almacena
    def add_proyecto(self,dni,nombre_proyecto,descripcion_proyecto):
        '''
                Añade un proyecto a un usuario.

                Parámetros
                ----------
                dni : str
                    DNI del usuario.
                nombre_proyecto : str
                    Nombre del proyecto.
                descripcion_proyecto : str
                    Descripción del proyecto.
                '''
        descripcion_validada=self.validar_descripcion(descripcion_proyecto)

        if descripcion_validada:
            # Llamamos al método que abre el archivo y carga los proyectos dentro de self.proyectos
            self.cargar_proyectos_json('proyectos.json')

            # Verificamos si el usuario existe en la base de datos
            usuariodb = UsuarioBase()
            usuariodb.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = usuariodb.cursor.fetchone()
            if not usuario:
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

    # Método que permite ver los proyectos
    def ver_proyecto(self, dni):
        '''
                Muestra la información de un proyecto específico de un usuario.

                Parámetros
                ----------
                dni : str
                    DNI del usuario.
                '''
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
        nombre_proyecto = proyectos_usuario[idproyecto]['nombre_proyecto']
        descripcion_proyecto = proyectos_usuario[idproyecto]['descripcion_proyecto']


    def ver_tareas(self,dni):
        '''
                Muestra la información de las tareas de un proyecto específico de un usuario.

                Parámetros
                ----------
                dni : str
                    DNI del usuario.
                '''
        global boton_tareas
        global boton_proyecto
        global idtarea
        global nombre_tarea
        global descripcion_tarea
        global estado_tarea


        with open('proyectos.json', 'r') as json_file:
            proyectos = json.load(json_file)
        proyectos_usuario = proyectos.get(dni, {})
        idtarea = str(boton_tareas + 1)
        if proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'] != {}:
            nombre_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['titulo']
            descripcion_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['descripcion']
            estado_tarea = proyectos_usuario[str(boton_proyecto)]['tareas_proyecto'][idtarea]['estado']
        else:
            nombre_tarea = 'No tienes tareas'
            descripcion_tarea = 'No tienes tareas'
            estado_tarea = 'pendiente'


class Tarea:
    '''
        Descripcion Clase:
        Esta clase se encarga de gestionar el estado de las tareas.

        Métodos clase:
        cambiar_estado: Cambia el estado de una tarea.
        cambiar_pendiente: Cambia el estado de una tarea a "pendiente".
        cambiar_en_curso: Cambia el estado de una tarea a "en curso".
        cambiar_completada: Cambia el estado de una tarea a "completada".
    '''
    def cambiar_pendiente(self):
        ''' Cambia el estado de una tarea a "pendiente". '''
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
        ''' Cambia el estado de una tarea a "en curso". '''
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
        ''' Cambia el estado de una tarea a "completada". '''
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
    Esta clase será la encargada de añadir tareas al proyecto

    Métodos Clase:
    verificar_titulo: Verifica si el título es válido.
    verificar_descripcion: Verifica si la descripción es válida.
    agregar_tarea: Encargado de agregar tareas al proyecto deseado almacenándolas en un archivo json.
    '''
    def verificar_titulo(self, titulo):
        '''
                Verifica si el título de una tarea es válido.

                Parámetros
                ----------
                titulo : str
                    Título de la tarea a verificar.

                Devuelve
                -------
                bool
                    True si el título es válido, False en caso contrario.
                '''
        # Probamos a escribir el título
        try:
            if not titulo:
                # Lanzamos el error TituloError
                raise TituloError("El título no puede estar vacío")
        # Si el error salta
        except TituloError as te:
            # Imprimimos error
            titulo_verificado = False
        # Si el título es válido
        else:
            titulo_verificado = True
        return titulo_verificado

    def verificar_descripcion(self, descripcion):
        '''
                Verifica si la descripción de una tarea es válida.

                Parámetros
                ----------
                descripción : str
                    Descripción de la tarea a verificar.

                Devuelve
                -------
                bool
                    True si la descripción es válida, False en caso contrario.
                '''
        try:
            if len(descripcion) > 80:
                # Se lanza el error DescripcionError
                raise DescripcionError("La descripción no puede exceder los 80 caracteres")
        # Si el error salta
        except DescripcionError as de:
            # Imprimimos el error
            descripcion_validada = False
        # Si la descripción es correcta
        else:
            descripcion_validada = True
        return descripcion_validada

    # Método encargado de añadir tareas al proyecto
    def agregar_tarea(self, dni, id_proyecto, nombre, descripcion):
        '''
                Agrega una tarea a un proyecto.

                Parámetros
                ----------
                dni : str
                    DNI del usuario.
                id_proyecto : int
                    ID del proyecto al que se añadirá la tarea.
                nombre : str
                    Nombre de la tarea.
                descripcion : str
                    Descripción de la tarea.
                '''
        try:
            with open('proyectos.json', 'r') as json_file:
                # Cargamos el diccionario desde el archivo JSON
                proyectos = json.load(json_file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return
        except Exception as e:
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

            except Exception as e:
                print(f"Error inesperado al escribir el archivo: {e}")
        else:
            print("Nombre o descripción no válidos")

help(UsuarioBase())