

class EstadoTarea:
    pendiente = 'Pendiente'
    en_curso = 'En curso'
    completada = 'Completada'

class Tarea:
    def __init__(self, id_tarea = int, titulo = str, descripcion = str, estimacion_coste = int):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.estimacion_coste = estimacion_coste
        self.estado = EstadoTarea.pendiente
        self.subtareas = {}

    def EditarTarea(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

    def AsignarUsuario(self, usuario):
        self.usuario = usuario
        self.estado = EstadoTarea.en_curso

    def AnyadirSubtarea(self, subt):
        self.subtareas[subt] = EstadoTarea.en_curso

    def CambiarEstado(self, subt, estado):
        self.subtareas[subt] = estado
        for i in range(len(self.subtareas)):
            if self.subtareas[i] != EstadoTarea.completada:
                pass
        self.estado = EstadoTarea.completada

    def __str__(self):
        return f'Id: {self.id_tarea}, {self.titulo}: {self.descripcion}. {self.estado}.'


