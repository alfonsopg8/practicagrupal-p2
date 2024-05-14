import sqlite3
import json
import pandas as pd
from errores import IdError, DescripcionError
from clase_proyecto import Proyecto
from usuario_2 import UsuarioBase  # Asegúrate de que este es el nombre correcto del archivo donde está la clase UsuarioBase

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

    # Método que crea proyectos y los almacena
    def add_proyecto(self):
        # Llamamos al método que abre el archivo y carga los proyectos dentro de self.proyectos
        self.cargar_proyectos_json('proyectos.json')

        # Pide DNI del usuario
        dni = input("Ingrese el DNI del usuario para añadir proyecto: ")

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

        # Pedimos el nombre del proyecto
        nombre_proyecto = input("Ingrese el nombre del proyecto: ")
        # Bucle que comprueba que la descripción sea correcta, si no es así, que la vuelva a pedir
        while True:
            descripcion_proyecto = input("Ingrese una pequeña descripción del proyecto (80 palabras máximo): ")
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
                # Continua el bucle
                continue
            # Si la descripción es válida
            else:
                # Salimos del bucle
                break

        # Creamos un proyecto con los parámetros previamente comprobados
        nuevo_proyecto = Proyecto(id_proyecto, dni, nombre_proyecto, descripcion_proyecto)
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

gestor = GestorSistema()
gestor.ver_proyecto()