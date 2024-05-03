

class EstadoTarea:
    pendiente = 'Pendiente'
    en_curso = 'En curso'
    completada = 'Completada'

class Tarea:
    def __init__(self, id_tarea = int, titulo = str, descripcion = str, estado = str):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def EditarTarea(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

    def CambiarEstado(self, estado):
        self.estado = estado

    def __str__(self):
        return f'Id: {self.id_tarea}, {self.titulo}: {self.descripcion}. {self.estado}.'

tarea1 = Tarea(24, 'Tarea 1', 'Realizar la Tarea1', EstadoTarea.pendiente)
tarea1.CambiarEstado(EstadoTarea.en_curso)
tarea1.EditarTarea('Tarea2', 'Sí')
print(tarea1)


