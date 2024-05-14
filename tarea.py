import json


class EstadoTarea:
    pendiente = 'Pendiente'
    en_curso = 'En curso'
    completada = 'Completada'


class Tarea:
    '''
    Esta clase representa una tarea con un ID, título, descripción y estado.
    Permite eliminar y cambiar el estado de una tarea en un archivo JSON.
    '''

    def __init__(self, id_tarea, titulo, descripcion):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoTarea.pendiente

    def eliminar_tarea(self, dni, id_proyecto):
        # Abrimos el archivo JSON
        try:
            with open('proyectos.json', 'r') as json_file:
                # Guardamos el diccionario del JSON en el atributo proyectos
                proyectos = json.load(json_file)
        except FileNotFoundError:
            print("Archivo de proyectos no encontrado.")
            return

        # Verificamos si el DNI del usuario y el ID del proyecto existen en el diccionario
        if dni in proyectos and str(id_proyecto) in proyectos[dni]:
            # Verificamos si la tarea existe en el proyecto
            if str(self.id_tarea) in proyectos[dni][str(id_proyecto)]['tareas_proyecto']:
                # Eliminamos la tarea
                del proyectos[dni][str(id_proyecto)]['tareas_proyecto'][str(self.id_tarea)]

                # Guardamos los cambios en el archivo JSON
                with open('proyectos.json', 'w') as json_file:
                    json.dump(proyectos, json_file, indent=4)

                print(f"Tarea con ID {self.id_tarea} eliminada correctamente.")
            else:
                print(f"Tarea con ID {self.id_tarea} no encontrada.")
        else:
            print("Proyecto o usuario no encontrado.")

    def cambiar_estado(self, dni, id_proyecto):
        # Abrimos el archivo JSON
        try:
            with open('proyectos.json', 'r') as json_file:
                # Guardamos el diccionario del JSON en el atributo proyectos
                proyectos = json.load(json_file)
        except FileNotFoundError:
            print("Archivo de proyectos no encontrado.")
            return

        # Verificamos si el DNI del usuario y el ID del proyecto existen en el diccionario
        if dni in proyectos and str(id_proyecto) in proyectos[dni]:
            # Verificamos si la tarea existe en el proyecto
            if str(self.id_tarea) in proyectos[dni][str(id_proyecto)]['tareas_proyecto']:
                # Cambiamos el estado de la tarea
                estado_actual = proyectos[dni][str(id_proyecto)]['tareas_proyecto'][str(self.id_tarea)]['estado']
                if estado_actual == EstadoTarea.pendiente:
                    proyectos[dni][str(id_proyecto)]['tareas_proyecto'][str(self.id_tarea)][
                        'estado'] = EstadoTarea.en_curso
                else:
                    proyectos[dni][str(id_proyecto)]['tareas_proyecto'][str(self.id_tarea)][
                        'estado'] = EstadoTarea.completada

                # Guardamos los cambios en el archivo JSON
                with open('proyectos.json', 'w') as json_file:
                    json.dump(proyectos, json_file, indent=4)

                print(f"Estado de la tarea con ID {self.id_tarea} cambiado correctamente.")
            else:
                print(f"Tarea con ID {self.id_tarea} no encontrada.")
        else:
            print("Proyecto o usuario no encontrado.")

    def __str__(self):
        return f'Id: {self.id_tarea}, {self.titulo}: {self.descripcion}. {self.estado}.'

