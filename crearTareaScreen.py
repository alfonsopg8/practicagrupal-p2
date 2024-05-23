from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox


class Ui_crearTareaScreen(object):
    """
       Clase que representa la interfaz gráfica para la creación de tareas en un proyecto.

       Methods
       -------
       crearTareafuncion()
           Añade una nueva tarea al proyecto y muestra la pantalla principal.
       goBack()
           Navega de regreso a la pantalla principal.
       setupUi(crearTareaScreen)
           Configura la interfaz gráfica de la pantalla de creación de tareas.
       retranslateUi(crearTareaScreen)
           Traduce y establece el texto de los elementos de la interfaz.
       """
    def crearTareafuncion(self):
        """
                Añade una nueva tarea al proyecto utilizando la información proporcionada por el usuario.
                Luego, navega a la pantalla principal del sistema.
                """
        import main
        from main import Proyecto
        from mainScreen import Ui_mainScreen
        if len(self.descripcionTarea.text()) > 80:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 500px;min-height: 100px;}")
            msg.setText("La descripción de la tarea supera los 80 caracteres")
            msg.exec_()
        else:
            tarea = Proyecto()
            tarea.agregar_tarea(main.dni,self.idProyecto.text(),self.nombreTarea.text(), self.descripcionTarea.text())
            self.main_window = QtWidgets.QMainWindow()
            self.ui_mainScreen = Ui_mainScreen()
            self.ui_mainScreen.setupUi(self.main_window)
            self.main_window.show()
            self.crear_tarea.close()


    def goBack(self):
        """
               Navega de regreso a la pantalla principal sin realizar ninguna acción adicional.
               """
        from mainScreen import Ui_mainScreen
        self.main_window = QtWidgets.QMainWindow()
        self.ui_mainScreen = Ui_mainScreen()
        self.ui_mainScreen.setupUi(self.main_window)
        self.main_window.show()
        self.crear_tarea.close()
    def setupUi(self, crearTareaScreen):
        """
                Configura la interfaz gráfica de la pantalla de creación de tareas.

                Parameters
                ----------
                crearTareaScreen : QtWidgets.QWidget
                    El widget que representa la pantalla de creación de tareas.
                """
        self.crear_tarea = crearTareaScreen
        crearTareaScreen.setObjectName("crearTareaScreen")
        crearTareaScreen.resize(1146, 855)
        self.widget = QtWidgets.QWidget(crearTareaScreen)
        self.widget.setGeometry(QtCore.QRect(10, 40, 1111, 821))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 1069, 463))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.descripcionTarea = QtWidgets.QLineEdit(self.layoutWidget)
        self.descripcionTarea.setMinimumSize(QtCore.QSize(881, 251))
        self.descripcionTarea.setStyleSheet("")
        self.descripcionTarea.setInputMask("")
        self.descripcionTarea.setText("")
        self.descripcionTarea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descripcionTarea.setDragEnabled(False)
        self.descripcionTarea.setObjectName("descripcionTarea")
        self.gridLayout.addWidget(self.descripcionTarea, 6, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(471, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.idProyecto = QtWidgets.QLineEdit(self.layoutWidget)
        self.idProyecto.setMinimumSize(QtCore.QSize(530, 30))
        self.idProyecto.setObjectName("idProyecto")
        self.gridLayout.addWidget(self.idProyecto, 2, 1, 1, 1)
        self.nombreTarea = QtWidgets.QLineEdit(self.layoutWidget)
        self.nombreTarea.setMinimumSize(QtCore.QSize(530, 30))
        self.nombreTarea.setObjectName("nombreTarea")
        self.gridLayout.addWidget(self.nombreTarea, 3, 1, 1, 1)
        self.agregarButtonTarea = QtWidgets.QPushButton(self.widget)
        self.agregarButtonTarea.setGeometry(QtCore.QRect(480, 640, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.agregarButtonTarea.setFont(font)
        self.agregarButtonTarea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.agregarButtonTarea.setObjectName("agregarButtonTarea")
        self.goBackButtonCrearTarea = QtWidgets.QPushButton(self.widget)
        self.goBackButtonCrearTarea.setGeometry(QtCore.QRect(20, 760, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goBackButtonCrearTarea.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow-97-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBackButtonCrearTarea.setIcon(icon)
        self.goBackButtonCrearTarea.setIconSize(QtCore.QSize(30, 30))
        self.goBackButtonCrearTarea.setObjectName("goBackButtonCrearTarea")

        self.retranslateUi(crearTareaScreen)
        QtCore.QMetaObject.connectSlotsByName(crearTareaScreen)


        #-------------------------------------------------

        self.agregarButtonTarea.clicked.connect(self.crearTareafuncion)
        self.goBackButtonCrearTarea.clicked.connect(self.goBack)

        #-------------------------------------------------


    def retranslateUi(self, crearTareaScreen):
        """
                Traduce y establece el texto de los elementos de la interfaz.

                Parameters
                ----------
                crearTareaScreen : QtWidgets.QWidget
                    El widget que representa la pantalla de creación de tareas.
                """
        _translate = QtCore.QCoreApplication.translate
        crearTareaScreen.setWindowTitle(_translate("crearTareaScreen", "Form"))
        self.descripcionTarea.setPlaceholderText(_translate("crearTareaScreen", "Descripcion corta"))
        self.label_4.setText(_translate("crearTareaScreen", "Descripcion de la Tarea (max. 80 palabras): "))
        self.label.setText(_translate("crearTareaScreen", "Agregar Tarea a un Proyecto"))
        self.label_5.setText(_translate("crearTareaScreen", "Nombre de la Tarea:"))
        self.label_3.setText(_translate("crearTareaScreen", "ID del Proyecto: "))
        self.idProyecto.setPlaceholderText(_translate("crearTareaScreen", "ID del Proyecto"))
        self.nombreTarea.setPlaceholderText(_translate("crearTareaScreen", "Nombre de la Tarea"))
        self.agregarButtonTarea.setText(_translate("crearTareaScreen", "Agregar"))
        self.goBackButtonCrearTarea.setText(_translate("crearTareaScreen", "Go Back"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_crearTareaScreen()
    crear_tarea = QtWidgets.QMainWindow()
    ui.setupUi(crear_tarea)
    crear_tarea.show()
    sys.exit(app.exec_())