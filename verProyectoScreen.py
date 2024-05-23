import sys
import json
import main

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_verProyecto(object):
    """
        A class to manage the UI of viewing a project in the application.

        Methods
        -------
        completadoTarea()
            Marks a task as completed.
        encursoTarea()
            Marks a task as in progress.
        pendienteTarea()
            Marks a task as pending.
        goBack()
            Navigates back to the main screen.
        irAdelanteProyecto()
            Navigates to the next project.
        irAtrasProyecto()
            Navigates to the previous project.
        irAdelanteTarea()
            Navigates to the next task.
        irAtrasTarea()
            Navigates to the previous task.
        setupUi(verProyecto)
            Sets up the UI elements for viewing a project.
        retranslateUi(verProyecto)
            Translates the UI elements for internationalization.
        """
    def completadoTarea(self):
        """
                Marks a task as completed by changing its status.

                Imports
                -------
                from main import Tarea
                    Tarea: Class that handles task operations.

                Notes
                -----
                Calls the cambiar_completada() method on an instance of Tarea.
                """
        from main import Tarea
        tarea = Tarea()
        tarea.cambiar_completada()

    def encursoTarea(self):
        """
                Marks a task as in progress by changing its status.

                Imports
                -------
                from main import Tarea
                    Tarea: Class that handles task operations.

                Notes
                -----
                Calls the cambiar_en_curso() method on an instance of Tarea.
                """
        from main import Tarea
        tarea = Tarea()
        tarea.cambiar_en_curso()

    def pendienteTarea(self):
        """
        Marks a task as pending by changing its status.

        Imports
        -------
        from main import Tarea
            Tarea: Class that handles task operations.

        Notes
        -----
        Calls the cambiar_pendiente() method on an instance of Tarea.
        """
        from main import Tarea
        tarea = Tarea()
        tarea.cambiar_pendiente()

    def goBack(self):
        """
        Navigates back to the main screen of the application.

        Imports
        -------
        from mainScreen import Ui_mainScreen
            Ui_mainScreen: Class that handles the UI of the main screen.

        Notes
        -----
        Sets up and shows the main screen UI, then closes the current project view.
        """
        from mainScreen import Ui_mainScreen
        self.main_window = QtWidgets.QMainWindow()
        self.ui_mainScreen = Ui_mainScreen()
        self.ui_mainScreen.setupUi(self.main_window)
        self.main_window.show()
        self.ver_proyecto.close()

    def irAdelanteProyecto(self):
        """
        Navigates to the next project in the list.

        Imports
        -------
        from main import GestorSistema
            GestorSistema: Class that handles system operations.
        import main
            Accesses global variables and methods from the main module.

        Notes
        -----
        Updates the project view and task view to the next project, handling the index appropriately.
        """
        from main import GestorSistema
        import main
        proyecto = GestorSistema()
        main.boton_tareas = 0
        with open('proyectos.json', 'r') as json_file:
            # Cargamos el diccionario desde el archivo JSON
            proyectos = json.load(json_file)
        if len(proyectos[main.dni])<=(main.boton_proyecto):
            main.boton_proyecto=0

        main.boton_proyecto += 1
        proyecto.ver_proyecto(main.dni)
        proyecto.ver_tareas(main.dni)
        self.ver_proyecto.close()
        # Crear una nueva instancia de la ventana
        self.nueva_ventana = QtWidgets.QMainWindow()
        self.nuevo_ui = Ui_verProyecto()
        self.nuevo_ui.setupUi(self.nueva_ventana)
        self.nueva_ventana.show()

    def irAtrasProyecto(self):
        """
                Navigates to the previous project in the list.

                Imports
                -------
                from main import GestorSistema
                    GestorSistema: Class that handles system operations.
                import main
                    Accesses global variables and methods from the main module.

                Notes
                -----
                Updates the project view and task view to the previous project, handling the index appropriately.
                """
        from main import GestorSistema
        import main
        proyecto = GestorSistema()
        with open('proyectos.json', 'r') as json_file:
            # Cargamos el diccionario desde el archivo JSON
            proyectos = json.load(json_file)
        if (main.boton_proyecto)==1:
            main.boton_proyecto=len(proyectos[main.dni])+1
        main.boton_proyecto -= 1
        proyecto.ver_proyecto(main.dni)
        proyecto.ver_tareas(main.dni)
        self.ver_proyecto.close()
        main.boton_tareas=0
        # Crear una nueva instancia de la ventana
        self.nueva_ventana = QtWidgets.QMainWindow()
        self.nuevo_ui = Ui_verProyecto()
        self.nuevo_ui.setupUi(self.nueva_ventana)
        self.nueva_ventana.show()

    def irAdelanteTarea(self):
        """
                Navigates to the next task in the project.

                Imports
                -------
                from main import GestorSistema
                    GestorSistema: Class that handles system operations.
                import main
                    Accesses global variables and methods from the main module.

                Notes
                -----
                Updates the task view to the next task, handling the index appropriately.
                """
        from main import GestorSistema
        import main
        tarea = GestorSistema()
        with open('proyectos.json', 'r') as json_file:
            # Cargamos el diccionario desde el archivo JSON
            proyectos = json.load(json_file)
        if len(proyectos[main.dni][str(main.idproyecto)]['tareas_proyecto'])-1 <= (main.boton_tareas):
            main.boton_tareas = -1
        main.boton_tareas += 1
        tarea.ver_proyecto(main.dni)
        tarea.ver_tareas(main.dni)
        self.ver_proyecto.close()
        # Crear una nueva instancia de la ventana
        self.nueva_ventana = QtWidgets.QMainWindow()
        self.nuevo_ui = Ui_verProyecto()
        self.nuevo_ui.setupUi(self.nueva_ventana)
        self.nueva_ventana.show()

    def irAtrasTarea(self):
        """
                Navigates to the previous task in the project.

                Imports
                -------
                from main import GestorSistema
                    GestorSistema: Class that handles system operations.
                import main
                    Accesses global variables and methods from the main module.

                Notes
                -----
                Updates the task view to the previous task, handling the index appropriately.
                """
        from main import GestorSistema
        import main
        tarea = GestorSistema()
        with open('proyectos.json', 'r') as json_file:
            # Cargamos el diccionario desde el archivo JSON
            proyectos = json.load(json_file)
        if (main.boton_tareas)==0:
            main.boton_tareas=len(proyectos[main.dni][str(main.idproyecto)]['tareas_proyecto'])

        main.boton_tareas -= 1
        tarea.ver_proyecto(main.dni)
        tarea.ver_tareas(main.dni)
        self.ver_proyecto.close()
        # Crear una nueva instancia de la ventana
        self.nueva_ventana = QtWidgets.QMainWindow()
        self.nuevo_ui = Ui_verProyecto()
        self.nuevo_ui.setupUi(self.nueva_ventana)
        self.nueva_ventana.show()

    def setupUi(self, verProyecto):
        """
                Sets up the UI elements for viewing a project.

                Parameters
                ----------
                verProyecto : QMainWindow
                    The main window instance for viewing a project.

                Notes
                -----
                Initializes the UI elements and connects the signals to the respective slots.
                """
        self.ver_proyecto = verProyecto
        verProyecto.setObjectName("verProyecto")
        verProyecto.resize(1145, 853)
        self.widget = QtWidgets.QWidget(verProyecto)
        self.widget.setGeometry(QtCore.QRect(20, 20, 1111, 821))
        self.widget.setObjectName("widget")
        self.atrasButtonProyecto = QtWidgets.QPushButton(self.widget)
        self.atrasButtonProyecto.setGeometry(QtCore.QRect(180, 170, 51, 41))
        self.atrasButtonProyecto.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow-97-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atrasButtonProyecto.setIcon(icon)
        self.atrasButtonProyecto.setIconSize(QtCore.QSize(40, 40))
        self.atrasButtonProyecto.setObjectName("atrasButtonProyecto")
        self.adelanteButtonProyecto = QtWidgets.QPushButton(self.widget)
        self.adelanteButtonProyecto.setGeometry(QtCore.QRect(860, 170, 51, 41))
        self.adelanteButtonProyecto.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("arrow-32-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adelanteButtonProyecto.setIcon(icon1)
        self.adelanteButtonProyecto.setIconSize(QtCore.QSize(40, 40))
        self.adelanteButtonProyecto.setObjectName("adelanteButtonProyecto")
        self.atrasButtonTarea = QtWidgets.QPushButton(self.widget)
        self.atrasButtonTarea.setGeometry(QtCore.QRect(180, 550, 51, 41))
        self.atrasButtonTarea.setText("")
        self.atrasButtonTarea.setIcon(icon)
        self.atrasButtonTarea.setIconSize(QtCore.QSize(40, 40))
        self.atrasButtonTarea.setObjectName("atrasButtonTarea")
        self.adelanteButtonTarea = QtWidgets.QPushButton(self.widget)
        self.adelanteButtonTarea.setGeometry(QtCore.QRect(860, 550, 51, 41))
        self.adelanteButtonTarea.setText("")
        self.adelanteButtonTarea.setIcon(icon1)
        self.adelanteButtonTarea.setIconSize(QtCore.QSize(40, 40))
        self.adelanteButtonTarea.setObjectName("adelanteButtonTarea")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 450, 611, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.idVerTarea = QtWidgets.QLineEdit(self.layoutWidget)
        self.idVerTarea.setMinimumSize(QtCore.QSize(101, 22))
        self.idVerTarea.setMaximumSize(QtCore.QSize(101, 22))
        self.idVerTarea.setObjectName("idVerTarea")
        self.horizontalLayout_6.addWidget(self.idVerTarea)
        self.goBackButtonVerProyecto = QtWidgets.QPushButton(self.widget)
        self.goBackButtonVerProyecto.setGeometry(QtCore.QRect(10, 770, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goBackButtonVerProyecto.setFont(font)
        self.goBackButtonVerProyecto.setIcon(icon)
        self.goBackButtonVerProyecto.setIconSize(QtCore.QSize(30, 30))
        self.goBackButtonVerProyecto.setObjectName("goBackButtonVerProyecto")
        self.completadoButtonTarea = QtWidgets.QPushButton(self.widget)
        self.completadoButtonTarea.setGeometry(QtCore.QRect(860, 620, 93, 28))
        self.completadoButtonTarea.setStyleSheet("background-color: rgb(132, 217, 132);")
        self.completadoButtonTarea.setObjectName("completadoButtonTarea")
        self.encursoButtonTarea = QtWidgets.QPushButton(self.widget)
        self.encursoButtonTarea.setGeometry(QtCore.QRect(860, 650, 93, 28))
        self.encursoButtonTarea.setStyleSheet("background-color: rgb(250, 255, 190);")
        self.encursoButtonTarea.setObjectName("encursoButtonTarea")
        self.pendienteButtonTarea = QtWidgets.QPushButton(self.widget)
        self.pendienteButtonTarea.setGeometry(QtCore.QRect(860, 680, 93, 28))
        self.pendienteButtonTarea.setStyleSheet("background-color: rgb(255, 147, 133);")
        self.pendienteButtonTarea.setObjectName("pendienteButtonTarea")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(240, 0, 615, 388))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.idVerProyecto = QtWidgets.QLineEdit(self.widget1)
        self.idVerProyecto.setMinimumSize(QtCore.QSize(101, 22))
        self.idVerProyecto.setMaximumSize(QtCore.QSize(101, 22))
        self.idVerProyecto.setObjectName("idVerProyecto")
        self.horizontalLayout.addWidget(self.idVerProyecto)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.nombreVerProyecto = QtWidgets.QLineEdit(self.widget1)
        self.nombreVerProyecto.setMinimumSize(QtCore.QSize(400, 22))
        self.nombreVerProyecto.setMaximumSize(QtCore.QSize(10000000, 22))
        self.nombreVerProyecto.setObjectName("nombreVerProyecto")
        self.horizontalLayout_2.addWidget(self.nombreVerProyecto)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.descripcionVerProyecto = QtWidgets.QLineEdit(self.widget1)
        self.descripcionVerProyecto.setMinimumSize(QtCore.QSize(600, 200))
        self.descripcionVerProyecto.setMaximumSize(QtCore.QSize(7000, 5000))
        self.descripcionVerProyecto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descripcionVerProyecto.setObjectName("descripcionVerProyecto")
        self.verticalLayout.addWidget(self.descripcionVerProyecto)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.widget2 = QtWidgets.QWidget(self.widget)
        self.widget2.setGeometry(QtCore.QRect(251, 411, 576, 35))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem6 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.widget3 = QtWidgets.QWidget(self.widget)
        self.widget3.setGeometry(QtCore.QRect(252, 491, 611, 30))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.nombreVerTarea = QtWidgets.QLineEdit(self.widget3)
        self.nombreVerTarea.setMinimumSize(QtCore.QSize(400, 22))
        self.nombreVerTarea.setMaximumSize(QtCore.QSize(10000000, 22))
        self.nombreVerTarea.setObjectName("nombreVerTarea")
        self.horizontalLayout_7.addWidget(self.nombreVerTarea)
        self.descripcionVerTarea = QtWidgets.QLineEdit(self.widget)
        self.descripcionVerTarea.setGeometry(QtCore.QRect(250, 560, 600, 200))
        self.descripcionVerTarea.setMinimumSize(QtCore.QSize(600, 200))
        self.descripcionVerTarea.setMaximumSize(QtCore.QSize(7000, 100))
        self.descripcionVerTarea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descripcionVerTarea.setObjectName("descripcionVerTarea")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(253, 529, 124, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(verProyecto)
        QtCore.QMetaObject.connectSlotsByName(verProyecto)

        #-----------------------------------------


        self.adelanteButtonProyecto.clicked.connect(self.irAdelanteProyecto)

        self.atrasButtonProyecto.clicked.connect(self.irAtrasProyecto)

        self.goBackButtonVerProyecto.clicked.connect(self.goBack)

        self.adelanteButtonTarea.clicked.connect(self.irAdelanteTarea)

        self.atrasButtonTarea.clicked.connect(self.irAtrasTarea)

        self.completadoButtonTarea.clicked.connect(self.completadoTarea)
        self.encursoButtonTarea.clicked.connect(self.encursoTarea)
        self.pendienteButtonTarea.clicked.connect(self.pendienteTarea)
        #-----------------------------------------

    def retranslateUi(self, verProyecto):
        """
                        Traduce y establece el texto de los elementos de la interfaz.

                        Parameters
                        ----------
                        verProyecto : QtWidgets.QWidget
                            El widget que representa la pantalla de visualización de proyecto.
                        """
        _translate = QtCore.QCoreApplication.translate
        verProyecto.setWindowTitle(_translate("verProyecto", "Form"))
        self.label_7.setText(_translate("verProyecto", "ID:"))
        self.idVerTarea.setText(_translate("verProyecto", main.idtarea))
        self.goBackButtonVerProyecto.setText(_translate("verProyecto", "Go Back"))
        self.completadoButtonTarea.setText(_translate("verProyecto", "Completado"))
        self.encursoButtonTarea.setText(_translate("verProyecto", "En curso"))
        self.pendienteButtonTarea.setText(_translate("verProyecto", "Pendiente"))
        self.label.setText(_translate("verProyecto", "Ver Proyectos"))
        self.label_2.setText(_translate("verProyecto", "ID:"))
        self.idVerProyecto.setText(_translate("verProyecto", main.idproyecto))
        self.label_3.setText(_translate("verProyecto", "Nombre:"))
        self.nombreVerProyecto.setText(_translate("verProyecto", main.nombre_proyecto))
        self.label_4.setText(_translate("verProyecto", "Descripcion:"))
        self.descripcionVerProyecto.setText(_translate("verProyecto", main.descripcion_proyecto))
        self.label_6.setText(_translate("verProyecto", "Ver Tareas del Proyectos"))
        self.label_8.setText(_translate("verProyecto", "Nombre:"))
        self.nombreVerTarea.setText(_translate("verProyecto", main.nombre_tarea))
        self.label_9.setText(_translate("verProyecto", "Descripcion:"))
        self.descripcionVerTarea.setText(_translate("verProyecto", main.descripcion_tarea))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_verProyecto()
    ver_proyecto = QtWidgets.QMainWindow()
    ui.setupUi(ver_proyecto)
    ver_proyecto.show()