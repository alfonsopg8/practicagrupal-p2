import json
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import main

class Estadisticas:
    @staticmethod
    def estadisticas(dni):
        with open('proyectos.json', 'r') as json_file:
            proyectos = json.load(json_file)

        proyectos_usuario = proyectos.get(dni, {})

        # Inicializa contadores y listas para los gráficos
        proyectos_finalizados = 0
        proyectos_totales = 0
        tareas_estado = {"completada": 0, "en curso": 0, "pendiente": 0}
        tareas_por_proyecto = []

        for id_proyecto, proyecto in proyectos_usuario.items():
            proyectos_totales += 1
            tareas = proyecto["tareas_proyecto"]
            tareas_por_proyecto.append(len(tareas))

            if tareas:
                completado = all(tarea["estado"] == "completada" for tarea in tareas.values())
                if completado:
                    proyectos_finalizados += 1

            for tarea_id, tarea_data in tareas.items():
                estado = tarea_data["estado"]
                if estado in tareas_estado:
                    tareas_estado[estado] += 1

        # Configura los datos para los gráficos
        proyectos_labels = ['Finalizado', 'No Finalizado']
        proyectos_counts = [proyectos_finalizados, proyectos_totales - proyectos_finalizados]

        tareas_labels = list(tareas_estado.keys())
        tareas_counts = list(tareas_estado.values())

        # Crea los gráficos con estilo
        fig, ax = plt.subplots(2, 2, figsize=(14, 14))
        fig.patch.set_facecolor('white')

        # Función para agregar marco y fondo a los ejes
        def set_frame(ax, color):
            ax.set_facecolor(color)
            for spine in ax.spines.values():
                spine.set_edgecolor('black')
                spine.set_linewidth(1.5)

        # Gráfico de barras del estado de los proyectos
        sns.barplot(x=proyectos_labels, y=proyectos_counts, hue=proyectos_labels, palette='viridis', ax=ax[0, 0], dodge=False, legend=False)
        ax[0, 0].set_title('Estado de los Proyectos')
        ax[0, 0].set_xlabel('Estado')
        ax[0, 0].set_ylabel('Número de Proyectos')
        set_frame(ax[0, 0], '#ffffff')  # Fondo blanco

        # Gráfico de barras del estado de las tareas
        sns.barplot(x=tareas_labels, y=tareas_counts, hue=tareas_labels, palette='viridis', ax=ax[0, 1], dodge=False, legend=False)
        ax[0, 1].set_title('Estado de las Tareas')
        ax[0, 1].set_xlabel('Estado')
        ax[0, 1].set_ylabel('Número de Tareas')
        set_frame(ax[0, 1], '#ffffff')  # Fondo blanco

        # Gráfico de dona de la distribución de tareas
        ax[1, 0].pie(tareas_counts, labels=tareas_labels, autopct='%1.1f%%', colors=sns.color_palette('viridis'), wedgeprops=dict(width=0.3))
        ax[1, 0].set_title('Distribución de las Tareas')
        set_frame(ax[1, 0], '#ffffff')  # Fondo blanco

        # Gráfico de barras del número de tareas por proyecto
        proyectos_indices = [f'Proyecto {i+1}' for i in range(proyectos_totales)]
        sns.barplot(x=proyectos_indices, y=tareas_por_proyecto, hue=proyectos_indices, palette='viridis', ax=ax[1, 1], dodge=False, legend=False)
        ax[1, 1].set_title('Número de Tareas por Proyecto')
        ax[1, 1].set_xlabel('Proyectos')
        ax[1, 1].set_ylabel('Número de Tareas')
        ax[1, 1].tick_params(axis='x', rotation=45)
        set_frame(ax[1, 1], '#ffffff')  # Fondo blanco

        return fig

class EstadisticasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estadísticas de Proyectos")
        self.showMaximized()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.show_statistics()  # Llama directamente a la función para mostrar las estadísticas

    def show_statistics(self):
        fig = Estadisticas.estadisticas(main.dni)
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EstadisticasApp()
    window.show()
    sys.exit(app.exec_())
