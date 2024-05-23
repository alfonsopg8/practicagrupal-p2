<font size="10"><div align="center"><b>GESTOR TAREAS</b></div></font>
**Integrantes:** Paulino Sanchiz, Alejandro López, Taron Sargsyan, Alfonso Paya y
Manuel García.\
\
**Resumen:** Para nuestro proyecto final, hemos decidido desarrollar un gestor de
tareas. Este sistema permite a los usuarios gestionar proyectos y las tareas asociadas a
ellos de manera eficiente y organizada. El gestor de tareas es una aplicación diseñada
para facilitar la gestión de proyectos y las tareas.\
**Funcionalidades Principales:**
1. Gestión de Proyectos:\
• Añadir Proyectos: Los usuarios pueden crear nuevos proyectos y
asignarlos a sus cuentas.\
• Eliminar Proyectos: Los usuarios pueden eliminar proyectos que ya no
son necesarios.\
• Visualizar Proyectos: Los usuarios pueden ver los detalles de sus
proyectos, incluyendo las tareas asociadas.
2. Gestión de Tareas:\
• Visualizar Tareas: Los usuarios pueden ver las tareas dentro de un
proyecto específico y su estado actual.\
• Añadir Tareas: Los usuarios pueden añadir nuevas tareas a sus
proyectos.\
• Eliminar Tareas: Los usuarios pueden eliminar tareas que ya no son
relevantes.\
• Estados de Tareas:\
• Las tareas pueden tener uno de los tres estados siguientes:\
• Pendiente: La tarea aún no ha comenzado.\
• En Curso: La tarea está actualmente en progreso.\
• Completada: La tarea se ha terminado.\
\
**Compilación:** Para la compilación de nuestro proyecto encontramos, en primer lugar,
un txt, el cual es requisitos. Este txt contiene todas las librerías que contiene el
proyecto, que al ser ejecutado las instalará. Además de esto encontramos diversos
archivos .py, donde ha sido desarrollado el proyecto. Para la ejecución principal del
programa encontraremos ‘loginScreen.py’, al ejecutar este .py todo el programa
entrará en funcionamiento. Si no tenemos usuario lo podremos crear en ‘registrer’,
que guardará la información en una base de datos, ‘usuarios.db’. Después de registrar
el usuario, se iniciará la sesión. En este punto, empieza el gestor de tareas. Dentro se
encontra una página principal, donde aparece la información del usuario, junto unos
botones para editarlo y eliminarlo. En esta página también encontramos la
visualización/progreso del usuario, el cual se representa en gráficas. Para crear y
visualizar tareas y proyectos lo encontraremos a la parte izquierda de la pantalla.
Todo los proyectos y tareas guardados, serán almacenados en un json. Por último,
tenemos un archivo ‘api.py’ el cual nos permite visualizar nuestros proyectos desde
cualquier lugar y en cualquier dispositivo
