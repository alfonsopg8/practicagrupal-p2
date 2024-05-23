from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import main
from main import botonRegistro
from errores import UsuarioError



class Ui_registerScreen(object):
    """
    Clase para la pantalla de registro en una aplicación PyQt5.
    """

    #-----------------Mis funciones------------------
    def sendInfo(self):
        """
        Guarda la información de registro en las variables del módulo principal.
        """
        main.name = self.nombreUsuarioRegister.text()
        main.surname = self.apellidoUsuarioRegister.text()
        main.dni = self.dniRegister.text()
        main.email = self.correoRegister.text()
        main.password = self.passwordRegister.text()

    def sendBotonRegistro(self):
        """
        Llama a la función botonRegistro del módulo main con los datos de registro.
        """
        botonRegistro(self, self.nombreUsuarioRegister.text(), self.apellidoUsuarioRegister.text(),
                      self.dniRegister.text(), self.correoRegister.text(), self.passwordRegister.text(),
                      self.registerWindow)

    def goLogin(self):
        """
        Verifica la existencia del usuario en la base de datos antes de registrar.

        Si el usuario ya existe, muestra un mensaje de error.
        """
        from loginScreen import Ui_loginScreen
        import main
        from main import UsuarioBase
        usuariodb = UsuarioBase()
        try:
            # Ejecuta la consulta para verificar si el usuario ya existe en la base de datos
            usuariodb.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (self.dniRegister.text(),))
            usuario = usuariodb.cursor.fetchone()
            if usuario:
                raise UsuarioError(self.dniRegister.text())
        except UsuarioError as ex:
            # Maneja la excepción si el usuario ya existe
            print(ex)
            self.ventana_error()
        else:
            # Registra el usuario si no existe y muestra la pantalla de inicio de sesión
            self.sendBotonRegistro()
            if main.goLogin:
                self.login_window = QtWidgets.QMainWindow()
                self.ui_register = Ui_loginScreen()
                self.ui_register.setupUi(self.login_window)
                self.login_window.show()
                self.registerWindow.close()
            else:
                self.ventana_error()
        finally:
            # Cierra el cursor y la conexión a la base de datos
            usuariodb.cursor.close()
            usuariodb.conn.close()

    def ventana_error(self):
        """
        Muestra un mensaje de error si las credenciales son inválidas.
        """
        import main
        if not main.goLogin:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 500px;min-height: 100px;}")
            msg.setText("Credenciales inválidas, revíselas")
            x = msg.exec_()

    #-----------------------------------------------
    def setupUi(self, RegisterWindow):
        """
               Configura la interfaz de usuario de la pantalla de registro.

               Parameters
               ----------
               RegisterWindow : QMainWindow
                   La ventana principal para configurar la UI.
        """
        self.registerWindow = RegisterWindow
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(1063, 825)
        RegisterWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        RegisterWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 10, 861, 741))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 801, 691))
        self.label.setStyleSheet("border-image: url(wallpaperMountain.jpg);\n"
"border-image: url(wallpaperMountainRegister.jpg);\n"
"border-radius: 40px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 781, 651))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius: 30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(90, 233, 235, 1);")
        self.label_3.setObjectName("label_3")
        self.nombreUsuarioRegister = QtWidgets.QLineEdit(self.widget)
        self.nombreUsuarioRegister.setGeometry(QtCore.QRect(160, 180, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nombreUsuarioRegister.setFont(font)
        self.nombreUsuarioRegister.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.nombreUsuarioRegister.setObjectName("nombreUsuarioRegister")
        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setGeometry(QtCore.QRect(160, 550, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton#registerButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#registerButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#registerButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.passwordRegister = QtWidgets.QLineEdit(self.widget)
        self.passwordRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRegister.setGeometry(QtCore.QRect(160, 460, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordRegister.setFont(font)
        self.passwordRegister.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.passwordRegister.setObjectName("passwordRegister")
        self.correoRegister = QtWidgets.QLineEdit(self.widget)
        self.correoRegister.setGeometry(QtCore.QRect(160, 390, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.correoRegister.setFont(font)
        self.correoRegister.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.correoRegister.setText("")
        self.correoRegister.setCursorPosition(0)
        self.correoRegister.setObjectName("correoRegister")
        self.dniRegister = QtWidgets.QLineEdit(self.widget)
        self.dniRegister.setGeometry(QtCore.QRect(160, 320, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dniRegister.setFont(font)
        self.dniRegister.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.dniRegister.setText("")
        self.dniRegister.setObjectName("dniRegister")
        self.apellidoUsuarioRegister = QtWidgets.QLineEdit(self.widget)
        self.apellidoUsuarioRegister.setGeometry(QtCore.QRect(160, 250, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.apellidoUsuarioRegister.setFont(font)
        self.apellidoUsuarioRegister.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.apellidoUsuarioRegister.setText("")
        self.apellidoUsuarioRegister.setObjectName("apellidoUsuarioRegister")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)
        # -----------------My Code-----------------
        # Conecta la señal "clicked" del botón de registro a la función sendInfo.
        self.registerButton.clicked.connect(self.sendInfo)
        # Conecta la señal "clicked" del botón de registro a la función goLogin.
        self.registerButton.clicked.connect(self.goLogin)


        # ------------------------------------------


    def retranslateUi(self, RegisterWindow):
        """
           Traduce y establece el texto de los elementos de la interfaz de usuario.

           Parameters
           ----------
           RegisterWindow : QMainWindow
               La ventana principal para configurar la UI.
           """
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.label_3.setText(_translate("RegisterWindow", "Register"))
        self.nombreUsuarioRegister.setPlaceholderText(_translate("RegisterWindow", "Nombre del Usuario"))
        self.registerButton.setText(_translate("RegisterWindow", "Register"))
        self.passwordRegister.setPlaceholderText(_translate("RegisterWindow", "Contraseña"))
        self.correoRegister.setPlaceholderText(_translate("RegisterWindow", "Correo"))
        self.dniRegister.setPlaceholderText(_translate("RegisterWindow", "DNI"))
        self.apellidoUsuarioRegister.setPlaceholderText(_translate("RegisterWindow", "Apellidos del Usuario"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_registerScreen()
    register_window = QtWidgets.QMainWindow()
    ui.setupUi(register_window)
    register_window.show()
    sys.exit(app.exec_())