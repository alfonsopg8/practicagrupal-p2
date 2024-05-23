from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main
from PyQt5.QtWidgets import QMessageBox
eliminado = False

class Ui_mainScreen(object):
    """
    Elimina un usuario de la base de datos y redirige a la pantalla de inicio de sesión.

    Importa los módulos necesarios, muestra una confirmación para eliminar la cuenta,
    y si es confirmado, elimina el usuario usando `UsuarioBase`. Luego, cierra la ventana
    principal y abre la ventana de inicio de sesión.

    Dependencies:
    - main: Module containing global variables, including `dni` of the user.
    - UsuarioBase: Class for user operations in the database.
    - Ui_loginScreen: Class for the login screen UI.
    - QtWidgets.QMainWindow: PyQt5 class for main window operations.

    Side-effects:
    - Modifies the global variable `eliminado`.

    Note:
    - The function `confirmacion_eliminarCuenta` is called to get user confirmation.
    """
    def eliminarUsuario(self):
        from main import UsuarioBase
        from loginScreen import Ui_loginScreen
        global eliminado
        self.confirmacion_eliminarCuenta()
        if eliminado:
            eliminar = UsuarioBase()
            eliminar.eliminar_usuario(main.dni)
            self.main_window.close()
            self.login_window = QtWidgets.QMainWindow()
            self.ui_register = Ui_loginScreen()
            self.ui_register.setupUi(self.login_window)
            self.login_window.show()

    def confirmacion_eliminarCuenta(self):
        """
        Muestra una ventana de confirmación para la eliminación de la cuenta del usuario.

        Crea un cuadro de mensaje con opciones "Yes" y "No" para que el usuario confirme la
        eliminación de su cuenta. Si el usuario confirma, modifica la variable global `eliminado`
        a `True`, de lo contrario, a `False`.

        Side-effects:
        - Modifies the global variable `eliminado`.

        Note:
        - Utiliza `QMessageBox` de PyQt5 para mostrar el cuadro de mensaje.
        """
        global eliminado

        # Create message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Confirma la eliminación')
        msg_box.setText('¿Seguro que desea eliminar su cuenta?')

        # Add Yes and No buttons
        yes_button = msg_box.addButton(QMessageBox.Yes)
        no_button = msg_box.addButton(QMessageBox.No)

        # Set default button (optional)
        msg_box.setDefaultButton(no_button)

        # Show message box
        msg_box.exec_()

        # Check which button was clicked
        if msg_box.clickedButton() == yes_button:
            eliminado = True
        else:
            eliminado = False
        print(eliminado)

    def abrirEstadisticas(self):
        """
        Abre la ventana de estadísticas.

        Importa el módulo `EstadisticasApp` y muestra la ventana de estadísticas.
        """
        from estadisticas import EstadisticasApp
        self.estadisticas_window = EstadisticasApp()
        self.estadisticas_window.show()

    def abrirEditarDatos(self):
        """
        Abre la ventana para editar datos del usuario.

        Importa el módulo `Ui_Form` y muestra la ventana de edición de datos.
        Cierra la ventana principal actual.
        """
        from editarDatosScreen import Ui_Form
        self.editar_dato = QtWidgets.QMainWindow()
        self.ui_editarDato = Ui_Form()
        self.ui_editarDato.setupUi(self.editar_dato)
        self.editar_dato.show()
        self.main_window.close()

    def goVerProyecto(self):
        """
        Abre la ventana para ver proyectos.

        Importa el módulo `Ui_verProyecto` y muestra la ventana de ver proyectos.
        Cierra la ventana principal actual.
        """
        from verProyectoScreen import Ui_verProyecto
        self.ver_proyecto = QtWidgets.QMainWindow()
        self.ui_verProyecto = Ui_verProyecto()
        self.ui_verProyecto.setupUi(self.ver_proyecto)
        self.ver_proyecto.show()
        self.main_window.close()
    def goCrearProyecto(self):
        """
        Abre la ventana para crear un nuevo proyecto.

        Importa el módulo `Ui_crearProyectoScreen` y muestra la ventana de creación de proyectos.
        Cierra la ventana principal actual.
        """
        from crearProyecto import Ui_crearProyectoScreen
        self.crear_proyecto = QtWidgets.QMainWindow()
        self.ui_crearProyecto = Ui_crearProyectoScreen()
        self.ui_crearProyecto.setupUi(self.crear_proyecto)
        self.crear_proyecto.show()
        self.main_window.close()

    def goCrearTarea(self):
        """
        Abre la ventana para crear una nueva tarea.

        Importa el módulo `Ui_crearTareaScreen` y muestra la ventana de creación de tareas.
        Cierra la ventana principal actual.
        """
        from crearTareaScreen import Ui_crearTareaScreen
        self.crear_tarea = QtWidgets.QMainWindow()
        self.ui_crearTarea = Ui_crearTareaScreen()
        self.ui_crearTarea.setupUi(self.crear_tarea)
        self.crear_tarea.show()
        self.main_window.close()
    def setupUi(self, mainScreen):
        """
        Configura la interfaz de usuario para la pantalla principal.

        Establece la geometría, el estilo y los widgets de la ventana principal `mainScreen`.
        También define las conexiones de los botones a sus respectivas funciones.

        Parameters
        ----------
        mainScreen : QtWidgets.QMainWindow
            La ventana principal de la aplicación.
        """
        self.main_window = mainScreen
        mainScreen.setObjectName("mainScreen")
        mainScreen.resize(1099, 850)
        mainScreen.setMinimumSize(QtCore.QSize(1099, 850))
        mainScreen.setStyleSheet("background-color: #fff;")
        self.splitter = QtWidgets.QSplitter(mainScreen)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1101, 851))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(278, 850))
        self.menu_widget.setMaximumSize(QtCore.QSize(292, 851))
        self.menu_widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.menu_widget.setObjectName("menu_widget")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 241, 571))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox{\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab{\n"
"    padding-left: 5px;\n"
"    text-align: left;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#toolBox::tab:selected{\n"
"    background-color: #2d9cdb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#toolbox QPushButton{\n"
"    padding: 5px 0px 5px 20px;\n"
"    text-align: left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton::hover{\n"
"    background-color: #85C1E9;\n"
"}\n"
"#toolBox QPushButton::checked{\n"
"    background-color: #4398D8;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 241, 463))
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(70, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.toolBox.addItem(self.page, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 241, 463))
        self.page_5.setObjectName("page_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verProyectoButton = QtWidgets.QPushButton(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.verProyectoButton.setFont(font)
        self.verProyectoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("project-128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verProyectoButton.setIcon(icon)
        self.verProyectoButton.setCheckable(True)
        self.verProyectoButton.setChecked(False)
        self.verProyectoButton.setObjectName("verProyectoButton")
        self.verticalLayout_4.addWidget(self.verProyectoButton)
        self.crearProyectoButton = QtWidgets.QPushButton(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crearProyectoButton.setFont(font)
        self.crearProyectoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("edit-property-128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crearProyectoButton.setIcon(icon1)
        self.crearProyectoButton.setCheckable(True)
        self.crearProyectoButton.setObjectName("crearProyectoButton")
        self.verticalLayout_4.addWidget(self.crearProyectoButton)
        self.crearTareaButton = QtWidgets.QPushButton(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crearTareaButton.setFont(font)
        self.crearTareaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("add-list-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crearTareaButton.setIcon(icon2)
        self.crearTareaButton.setCheckable(False)
        self.crearTareaButton.setObjectName("crearTareaButton")
        self.verticalLayout_4.addWidget(self.crearTareaButton)
        spacerItem = QtWidgets.QSpacerItem(20, 393, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolBox.addItem(self.page_5, icon, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 241, 463))
        self.page_6.setObjectName("page_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toDoButton = QtWidgets.QPushButton(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toDoButton.setFont(font)
        self.toDoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("check-mark-2-128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toDoButton.setIcon(icon3)
        self.toDoButton.setCheckable(True)
        self.toDoButton.setObjectName("toDoButton")
        self.verticalLayout_3.addWidget(self.toDoButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 455, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.toolBox.addItem(self.page_6, icon3, "")
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setEnabled(True)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.search_widget = QtWidgets.QWidget(self.main_widget)
        self.search_widget.setStyleSheet("#search_widget{\n"
"    background-color: #ABB2B9;\n"
"}")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_Button = QtWidgets.QPushButton(self.search_widget)
        self.menu_Button.setEnabled(True)
        self.menu_Button.setMinimumSize(QtCore.QSize(40, 40))
        self.menu_Button.setMaximumSize(QtCore.QSize(40, 40))
        self.menu_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("menu-4-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Button.setIcon(icon4)
        self.menu_Button.setIconSize(QtCore.QSize(30, 30))
        self.menu_Button.setCheckable(True)
        self.menu_Button.setObjectName("menu_Button")
        self.horizontalLayout_3.addWidget(self.menu_Button)
        spacerItem2 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.user_label = QtWidgets.QLabel(self.search_widget)
        self.user_label.setMinimumSize(QtCore.QSize(30, 30))
        self.user_label.setMaximumSize(QtCore.QSize(30, 30))
        self.user_label.setStyleSheet("#user_label{\n"
"    background-color: #fff;\n"
"    border: 1px solid #F2F4F4;\n"
"    padding: 5px 5px;\n"
"    border-radius: 15%;\n"
"}")
        self.user_label.setText("")
        self.user_label.setPixmap(QtGui.QPixmap("contacts-128.ico"))
        self.user_label.setScaledContents(True)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout_3.addWidget(self.user_label)
        self.gridLayout.addWidget(self.search_widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget = QtWidgets.QWidget(self.tab_5)
        self.widget.setGeometry(QtCore.QRect(20, 20, 751, 381))
        self.widget.setMinimumSize(QtCore.QSize(751, 381))
        self.widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(50, 50, 0, 50)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(470, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.inputApellido = QtWidgets.QLabel(self.widget)
        self.inputApellido.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputApellido.setFont(font)
        self.inputApellido.setObjectName("inputApellido")
        self.horizontalLayout_2.addWidget(self.inputApellido)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(470, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inputNombre = QtWidgets.QLabel(self.widget)
        self.inputNombre.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputNombre.setFont(font)
        self.inputNombre.setObjectName("inputNombre")
        self.horizontalLayout.addWidget(self.inputNombre)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(470, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.inputDNI = QtWidgets.QLabel(self.widget)
        self.inputDNI.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputDNI.setFont(font)
        self.inputDNI.setObjectName("inputDNI")
        self.horizontalLayout_4.addWidget(self.inputDNI)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(470, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.inputCorreo = QtWidgets.QLabel(self.widget)
        self.inputCorreo.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputCorreo.setFont(font)
        self.inputCorreo.setObjectName("inputCorreo")
        self.horizontalLayout_5.addWidget(self.inputCorreo)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.estadisticasButton = QtWidgets.QPushButton(self.tab_5)
        self.estadisticasButton.setGeometry(QtCore.QRect(280, 550, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.estadisticasButton.setFont(font)
        self.estadisticasButton.setStyleSheet("background-color: #06162d;\n"
"color: #fff;")
        self.estadisticasButton.setObjectName("estadisticasButton")
        self.editarDatosButton = QtWidgets.QPushButton(self.tab_5)
        self.editarDatosButton.setGeometry(QtCore.QRect(620, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editarDatosButton.setFont(font)
        self.editarDatosButton.setStyleSheet("background-color: #04162a;\n"
"color: #fff;")
        self.editarDatosButton.setObjectName("editarDatosButton")
        self.eliminarUsuarioButton = QtWidgets.QPushButton(self.tab_5)
        self.eliminarUsuarioButton.setGeometry(QtCore.QRect(20, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eliminarUsuarioButton.setFont(font)
        self.eliminarUsuarioButton.setStyleSheet("background-color: #04162a;\n"
"color: #fff;")
        self.eliminarUsuarioButton.setObjectName("eliminarUsuarioButton")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(mainScreen)
        self.toolBox.setCurrentIndex(0)
        self.menu_Button.toggled['bool'].connect(self.menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainScreen)


        #----------------------------------------
        self.crearProyectoButton.clicked.connect(self.goCrearProyecto)
        self.crearTareaButton.clicked.connect(self.goCrearTarea)
        self.verProyectoButton.clicked.connect(self.goVerProyecto)
        self.estadisticasButton.clicked.connect(self.abrirEstadisticas)
        self.editarDatosButton.clicked.connect(self.abrirEditarDatos)
        self.eliminarUsuarioButton.clicked.connect(self.eliminarUsuario)

        #----------------------------------------

    def retranslateUi(self, mainScreen):
        """
        Retraduce la interfaz de usuario, estableciendo los textos de los widgets.

        Parameters
        ----------
        mainScreen : QtWidgets.QMainWindow
            La ventana principal de la aplicación.
        """
        _translate = QtCore.QCoreApplication.translate
        mainScreen.setWindowTitle(_translate("mainScreen", "Form"))
        self.pushButton.setText(_translate("mainScreen", "Account"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("mainScreen", "Página"))
        self.verProyectoButton.setText(_translate("mainScreen", "Ver Proyecto"))
        self.crearProyectoButton.setText(_translate("mainScreen", "Crear Proyecto"))
        self.crearTareaButton.setText(_translate("mainScreen", "Crear Tarea"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("mainScreen", "Proyecto"))
        self.toDoButton.setText(_translate("mainScreen", "To Do"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("mainScreen", "To Do"))
        self.label_2.setText(_translate("mainScreen", "Apellido: "))
        self.inputApellido.setText(_translate("mainScreen", main.lastname))
        self.label.setText(_translate("mainScreen", "Nombre: "))
        self.inputNombre.setText(_translate("mainScreen", main.name))
        self.label_3.setText(_translate("mainScreen", "DNI: "))
        self.inputDNI.setText(_translate("mainScreen", main.dni))
        self.label_5.setText(_translate("mainScreen", "Correo: "))
        self.inputCorreo.setText(_translate("mainScreen", main.mail))
        self.estadisticasButton.setText(_translate("mainScreen", "Estadísticas"))
        self.editarDatosButton.setText(_translate("mainScreen", "Editar Datos"))
        self.eliminarUsuarioButton.setText(_translate("mainScreen", "Eliminar Usuario"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("mainScreen", "Página"))

help(Ui_mainScreen())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_mainScreen()
    main_window = QtWidgets.QMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
