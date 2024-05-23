from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main

class Ui_Form(object):
    """
    Clase para la interfaz de usuario de la ventana de edición de datos.
    """

    def botonActualizar(self):
        """
        Maneja el evento de clic en el botón de actualizar.

        Realiza las siguientes acciones:
        1. Importa las clases necesarias para la actualización y navegación de la interfaz.
        2. Crea una instancia de `UsuarioBase` para editar el usuario con los datos proporcionados.
        3. Configura y muestra la nueva ventana principal.
        4. Cierra la ventana de edición.
        """
        from mainScreen import Ui_mainScreen
        from main import UsuarioBase
        from loginScreen import Ui_loginScreen

        # Edición del usuario con los datos proporcionados
        editar = UsuarioBase()
        editar.editar_usuario(main.dni, self.cambiarNombre.text(), self.cambiarApellido.text(), self.cambiarCorreo.text())
        # Configuración de la nueva ventana principal
        self.mainScreen = QtWidgets.QMainWindow()
        self.ui_main = Ui_mainScreen()
        self.ui_main.setupUi(self.mainScreen)
        self.login_window = QtWidgets.QMainWindow()
        self.ui_register = Ui_loginScreen()
        self.ui_register.setupUi(self.login_window)
        self.login_window.show()
        self.editar.close()


    def setupUi(self, Form):
        """
        Configura la interfaz de usuario de la ventana de edición de datos.

        Parameters
        ----------
        Form : QtWidgets.QMainWindow
            Ventana principal de la aplicación.
        """
        self.editar = Form
        """
        Configura la interfaz de usuario de la ventana de edición de datos.

        Parameters
        ----------
        Form : QtWidgets.QMainWindow
            Ventana principal de la aplicación.
        """
        Form.setObjectName("Form")
        Form.resize(903, 588)

        # Configuración del widget principal
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 881, 561))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")

        # Configuración del título
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(340, 50, 171, 51))
        self.label.setMinimumSize(QtCore.QSize(171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Configuración del botón de actualizar
        self.actualizarButton = QtWidgets.QPushButton(self.widget)
        self.actualizarButton.setGeometry(QtCore.QRect(370, 390, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actualizarButton.setFont(font)
        self.actualizarButton.setCheckable(True)
        self.actualizarButton.setObjectName("actualizarButton")

        # Configuración del widget secundario
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(80, 190, 721, 191))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Configuración de etiquetas y campos de entrada
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cambiarNombre = QtWidgets.QLineEdit(self.widget1)
        self.cambiarNombre.setPlaceholderText("")
        self.cambiarNombre.setObjectName("cambiarNombre")
        self.gridLayout.addWidget(self.cambiarNombre, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cambiarApellido = QtWidgets.QLineEdit(self.widget1)
        self.cambiarApellido.setObjectName("cambiarApellido")
        self.gridLayout.addWidget(self.cambiarApellido, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.cambiarCorreo = QtWidgets.QLineEdit(self.widget1)
        self.cambiarCorreo.setObjectName("cambiarCorreo")
        self.gridLayout.addWidget(self.cambiarCorreo, 2, 1, 1, 1)

        # Traducción de elementos
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Conexión de eventos
        self.actualizarButton.clicked.connect(self.botonActualizar)

    def retranslateUi(self, Form):
        """
        Traduce los textos en la interfaz de usuario.

        Parameters
        ----------
        Form : QtWidgets.QMainWindow
            Ventana principal de la aplicación.
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Editar Datos"))
        self.actualizarButton.setText(_translate("Form", "Actualizar"))
        self.label_2.setText(_translate("Form", "Nuevo Nombre:"))
        self.label_3.setText(_translate("Form", "Nuevo Apellido:"))
        self.label_4.setText(_translate("Form", "Nuevo Correo:"))

help(Ui_Form())

if __name__ == "__main__":
    # Configuración de la aplicación y ejecución
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    login = QtWidgets.QMainWindow()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
