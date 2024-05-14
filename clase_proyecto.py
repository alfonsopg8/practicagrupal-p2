import json
from errores import ProyectoNoEncontradoError, TituloError, DescripcionError

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
    def __init__(self, id_proyecto, dni , nombre, descripcion):
        self.id_proyecto = id_proyecto
        self.dni = dni
        self.nombre = nombre
        self.descripcion = descripcion
        # Creamos una lista vacía llamada tareas donde almacenaremos las tareas del proyecto
        self.tareas = []

    # Método encargado de añadir tareas al proyecto
    def agregar_tarea(self):
        # Probamos a abrir el archivo json que almacena los proyectos
        try:
            # Abrimos el archivo
            with open('proyectos.json', 'r') as json_file:
                # Si este se abre, guardamos el diccionario perteneciente al json en el atributo proyectos
                proyectos = json.load(json_file)
        # Si no existe el archivo, salta el error
        except FileNotFoundError:
            # Creamos un diccionario vacío
            proyectos = {}

        # Inicializamos id a 1, por si no existen tareas creadas en el proyecto
        id = 1
        # Verificamos si el DNI y el ID del proyecto existen en el diccionario
        if self.dni in proyectos and str(self.id_proyecto) in proyectos[self.dni]:
            # Guardamos el respectivo proyecto en la variable proyecto_actual
            proyecto_actual = proyectos[self.dni][str(self.id_proyecto)]
            # Si la fila 'tareas_proyecto' se encuentra en el proyecto
            if "tareas_proyecto" in proyecto_actual:
                # id es el número de la tarea máxima encontrada en el diccionario + 1
                id = max((int(key) for key in proyecto_actual['tareas_proyecto'].keys()), default=0) + 1

        # Vamos a pedir los atributos de la tarea y a comprobarlos
        # Bucle que comprueba que el título es válido, sino lo vuelve a pedir
        while True:
            # Probamos a escribir el título
            try:
                titulo = input("Titulo: ")
                # Si el título está vacío
                if not titulo:
                    # Lanzamos el error TituloError
                    raise TituloError("El título no puede estar vacío")
            # Si el error salta
            except TituloError as te:
                # Imprimimos error
                print(te)
                # Continuamos con el bucle
                continue
            # Si el título es válido
            else:
                # Salimos del bucle
                break
        # Bucle que comprueba que la descripción es válida, sino la vuelve a pedir
        while True:
            # Probamos a introducir descripción
            try:
                descripcion = input("Descripcion: ")
                # Si la descripción contiene más de 80 caracteres
                if len(descripcion) > 80:
                    # Se lanza el error DescripcionError

                    raise DescripcionError("La descripción no puede exceder los 80 caracteres")
            # Si el error salta
            except DescripcionError as de:
                # Imprimimos el error
                print(de)
                # Continuamos con el bucle
                continue
            # Si la descripción es correcta
            else:
                # Salimos del bucle
                break

        # Estado de la tarea
        estado = 'pendiente'

        # Creamos un diccionario para la nueva tarea
        nueva_tarea = {
            'id': id,
            'titulo': titulo,
            'descripcion': descripcion,
            'estado': estado
        }

        # Si el DNI del usuario existe en el diccionario
        if self.dni in proyectos:
            # Si el proyecto existe dentro del DNI del usuario
            if str(self.id_proyecto) in proyectos[self.dni]:
                # Y si existe pero no existen tareas
                if 'tareas_proyecto' not in proyectos[self.dni][str(self.id_proyecto)]:
                    # Creamos el diccionario tareas dentro de su proyecto
                    proyectos[self.dni][str(self.id_proyecto)]['tareas_proyecto'] = {}
                # Añadimos la nueva tarea al repertorio de tareas del proyecto
                proyectos[self.dni][str(self.id_proyecto)]['tareas_proyecto'][id] = nueva_tarea
            else:
                # Imprimimos que no existe el proyecto
                print("Proyecto no encontrado")
                return
        else:
            # Imprimimos que no existe el usuario
            print("Usuario no encontrado")
            return

        # Abrimos el archivo json en modo escritura
        with open('proyectos.json', 'w') as json_file:
            # Guardamos en él, el diccionario proyectos actualizado
            json.dump(proyectos, json_file, indent=4)

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
                    print(f"ID: {id_tarea}, Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}")
            else:
                print("No hay tareas en este proyecto.")
        else:
            print("Proyecto o usuario no encontrado.")

class Tarea:
    def __init__(self, id, titulo, descripcion, estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado


proyecto1 = Proyecto(1,'56987847I' ,'Proyecto 1','agsdgdasd')
proyecto1.agregar_tarea()

