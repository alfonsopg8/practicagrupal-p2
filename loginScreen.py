from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import main
from registerScreen import Ui_registerScreen
from main import botonLogin
from errores import DniError
import sqlite3

class Ui_loginScreen(object):
    #-----------------My functions-----------------
    def register(self):
        self.register_window = QtWidgets.QMainWindow()
        self.ui_register = Ui_registerScreen()
        self.ui_register.setupUi(self.register_window)
        self.register_window.show()
        self.loginWindow.close()

    def sendBotonLogin(self):
        from mainScreen import Ui_mainScreen
        from main import UsuarioBase
        usuariodb = UsuarioBase()
        try:
            usuariodb.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (self.dniLogin.text(),))
            usuario = usuariodb.cursor.fetchone()
            if not usuario:
                raise DniError(self.dniLogin.text())
        except DniError as ex:
            print(ex)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 500px;min-height: 100px;}")
            msg.setText("Credenciales invalidas o Usuario inexistente")
            msg.exec_()  # Correct use of exec_() to show the message box
        else:
            print('else')
            main.botonLogin(self, self.dniLogin.text(), self.contrasenaLogin.text(), self.loginWindow)
            main.dniLogin = self.dniLogin.text()
            main.getInfo()
            self.goMainScreen()

    def goMainScreen(self):
        from mainScreen import Ui_mainScreen
        self.mainScreen = QtWidgets.QMainWindow()
        self.ui_main = Ui_mainScreen()
        self.ui_main.setupUi(self.mainScreen)
        self.mainScreen.show()
        self.loginWindow.close()



    #----------------------------------------------
    def setupUi(self, LoginWindow):
        self.loginWindow = LoginWindow
        LoginWindow.setObjectName("loginScreen")
        LoginWindow.resize(900, 800)
        LoginWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 861, 741))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 801, 691))
        self.label.setStyleSheet("border-image: url(wallpaperMountain.jpg);\n"
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
        self.label_3.setGeometry(QtCore.QRect(320, 100, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(90, 233, 235, 1);")
        self.label_3.setObjectName("label_3")
        self.dniLogin = QtWidgets.QLineEdit(self.widget)
        self.dniLogin.setGeometry(QtCore.QRect(160, 250, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dniLogin.setFont(font)
        self.dniLogin.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.dniLogin.setObjectName("dniLogin")
        self.contrasenaLogin = QtWidgets.QLineEdit(self.widget)
        self.contrasenaLogin.setGeometry(QtCore.QRect(160, 360, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contrasenaLogin.setFont(font)
        self.contrasenaLogin.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 4px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,255);\n"
"padding-bottom: 7px;")
        self.contrasenaLogin.setObjectName("contrasenaLogin")
        self.contrasenaLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setGeometry(QtCore.QRect(160, 480, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#loginButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#loginButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.registerButtonLogin = QtWidgets.QPushButton(self.widget)
        self.registerButtonLogin.setGeometry(QtCore.QRect(590, 550, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registerButtonLogin.setFont(font)
        self.registerButtonLogin.setStyleSheet("QPushButton#registerButtonLogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#registerButtonLogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 167, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#registerButtonLogin:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.registerButtonLogin.setObjectName("registerButtonLogin")
        font = QtGui.QFont()
        font.setPointSize(10)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # -----------------My Code-----------------
        self.registerButtonLogin.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.sendBotonLogin)
        #self.loginButton.clicked.connect(self.goMainScreen)
        # ------------------------------------------


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label_3.setText(_translate("LoginWindow", "Log In"))
        self.dniLogin.setPlaceholderText(_translate("LoginWindow", "DNI del Usuario"))
        self.contrasenaLogin.setPlaceholderText(_translate("LoginWindow", "Contraseña"))
        self.loginButton.setText(_translate("LoginWindow", "Log In"))
        self.registerButtonLogin.setText(_translate("LoginWindow", "Register"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_loginScreen()
    login = QtWidgets.QMainWindow()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())