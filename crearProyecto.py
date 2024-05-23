import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_crearProyectoScreen(object):
    """
        Clase que representa la interfaz gráfica para la creación de proyectos.

        Methods
        -------
        crearProyectofuncion()
            Añade el proyecto al sistema y muestra la pantalla principal.
        goBack()
            Navega de regreso a la pantalla principal.
        setupUi(crearProyectoScreen)
            Configura la interfaz gráfica de la pantalla de creación de proyectos.
        retranslateUi(crearProyectoScreen)
            Traduce y establece el texto de los elementos de la interfaz.
        """
    def crearProyectofuncion(self):
        """
                Añade un nuevo proyecto al sistema utilizando la información proporcionada por el usuario.
                Luego, navega a la pantalla principal del sistema.
                """
        import main
        from main import GestorSistema
        from mainScreen import Ui_mainScreen
        if len(self.descripcionProyectoCreado.text()) > 80:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 500px;min-height: 100px;}")
            msg.setText("La descripción del proyecto supera los 80 caracteres")
            msg.exec_()
        else:
            proyecto = GestorSistema()
            proyecto.add_proyecto(main.dni,self.nombreProyectoCreado.text(), self.descripcionProyectoCreado.text())
            self.main_window = QtWidgets.QMainWindow()
            self.ui_mainScreen = Ui_mainScreen()
            self.ui_mainScreen.setupUi(self.main_window)
            self.main_window.show()
            self.crear_proyecto.close()
    def goBack(self):
        """
               Navega de regreso a la pantalla principal sin realizar ninguna acción adicional.
               """
        from mainScreen import Ui_mainScreen
        self.main_window = QtWidgets.QMainWindow()
        self.ui_mainScreen = Ui_mainScreen()
        self.ui_mainScreen.setupUi(self.main_window)
        self.main_window.show()
        self.crear_proyecto.close()
    def setupUi(self, crearProyectoScreen):
        """
                Configura la interfaz gráfica de la pantalla de creación de proyectos.

                Parameters
                ----------
                crearProyectoScreen : QtWidgets.QWidget
                    El widget que representa la pantalla de creación de proyectos.
                """
        self.crear_proyecto = crearProyectoScreen
        crearProyectoScreen.setObjectName("crearProyectoScreen")
        crearProyectoScreen.resize(1100, 829)
        self.widget = QtWidgets.QWidget(crearProyectoScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1101, 831))
        self.widget.setStyleSheet("background-color: #fff;")
        self.widget.setObjectName("widget")
        self.goBackButtonCrearProyecto = QtWidgets.QPushButton(self.widget)
        self.goBackButtonCrearProyecto.setGeometry(QtCore.QRect(40, 760, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goBackButtonCrearProyecto.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow-97-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBackButtonCrearProyecto.setIcon(icon)
        self.goBackButtonCrearProyecto.setIconSize(QtCore.QSize(30, 30))
        self.goBackButtonCrearProyecto.setObjectName("goBackButtonCrearProyecto")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(110, 210, 883, 426))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMinimumSize(QtCore.QSize(221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.nombreProyectoCreado = QtWidgets.QLineEdit(self.widget1)
        self.nombreProyectoCreado.setMinimumSize(QtCore.QSize(530, 30))
        self.nombreProyectoCreado.setObjectName("nombreProyectoCreado")
        self.gridLayout.addWidget(self.nombreProyectoCreado, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setMinimumSize(QtCore.QSize(471, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.descripcionProyectoCreado = QtWidgets.QLineEdit(self.widget1)
        self.descripcionProyectoCreado.setMinimumSize(QtCore.QSize(881, 251))
        self.descripcionProyectoCreado.setInputMask("")
        self.descripcionProyectoCreado.setText("")
        self.descripcionProyectoCreado.setObjectName("descripcionProyectoCreado")
        self.gridLayout.addWidget(self.descripcionProyectoCreado, 3, 0, 1, 2)
        self.crearProyectoButtonCrear = QtWidgets.QPushButton(self.widget)
        self.crearProyectoButtonCrear.setGeometry(QtCore.QRect(500, 650, 93, 40))
        self.crearProyectoButtonCrear.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crearProyectoButtonCrear.setFont(font)
        self.crearProyectoButtonCrear.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.crearProyectoButtonCrear.setObjectName("crearProyectoButtonCrear")

        self.retranslateUi(crearProyectoScreen)
        QtCore.QMetaObject.connectSlotsByName(crearProyectoScreen)

        #------------------------------------------------------------------------------

        self.goBackButtonCrearProyecto.clicked.connect(self.goBack)
        self.crearProyectoButtonCrear.clicked.connect(self.crearProyectofuncion)
        #------------------------------------------------------------------------------

    def retranslateUi(self, crearProyectoScreen):
        """
               Traduce y establece el texto de los elementos de la interfaz.

               Parameters
               ----------
               crearProyectoScreen : QtWidgets.QWidget
                   El widget que representa la pantalla de creación de proyectos.
               """
        _translate = QtCore.QCoreApplication.translate
        crearProyectoScreen.setWindowTitle(_translate("crearProyectoScreen", "Form"))
        self.goBackButtonCrearProyecto.setText(_translate("crearProyectoScreen", "Go Back"))
        self.label.setText(_translate("crearProyectoScreen", "Crear Proyecto"))
        self.label_2.setText(_translate("crearProyectoScreen", "Nombre del Proyecto: "))
        self.nombreProyectoCreado.setPlaceholderText(_translate("crearProyectoScreen", "Nombre"))
        self.label_3.setText(_translate("crearProyectoScreen", "Descripcion del Proyecto (max. 80 palabras): "))
        self.descripcionProyectoCreado.setPlaceholderText(_translate("crearProyectoScreen", "Descripcion corta"))
        self.crearProyectoButtonCrear.setText(_translate("crearProyectoScreen", "Crear"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_crearProyectoScreen()
    crear_proyecto = QtWidgets.QMainWindow()
    ui.setupUi(crear_proyecto)
    crear_proyecto.show()
    sys.exit(app.exec_())