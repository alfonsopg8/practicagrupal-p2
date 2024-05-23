import json
from flask import Flask, render_template, request, redirect, url_for
from usuario_interfaz import UsuarioBase
from errores import DniError
import sqlite3

app = Flask(__name__)
app.template_folder = ''

usuario_base = UsuarioBase()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    dni = request.form['dni']
    contrasena = request.form['contraseña']
    try:
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
        usuario = cursor.fetchone()
        if not usuario:
            raise DniError(dni)
    except DniError as ex:
        print(ex)
        return "DNI no encontrado."
    else:
        contrasena_hasheada = usuario[1]
        if usuario_base.validar_hasheo(contrasena, contrasena_hasheada):
            try:
                with open('proyectos.json', 'r') as json_file:
                    proyectos_data = json.load(json_file).get(dni, {})
                    proyectos = []
                    for key, value in proyectos_data.items():
                        proyecto = {
                            'id': key,
                            'nombre': value.get('nombre_proyecto', ''),
                            'descripcion': value.get('descripcion_proyecto', ''),
                            'tareas': list(value.get('tareas_proyecto', {}).values())
                        }
                        proyectos.append(proyecto)
            except FileNotFoundError:
                proyectos = []
            # También debes cargar las tareas aquí
            else:
                return render_template('dashboard.html', proyectos=proyectos)
        else:
            return "DNI o contraseña incorrectos."
    finally:
        conn.close()

@app.route('/dashboard')
def dashboard():
    proyectos = request.args.get('proyectos', [])
    return render_template('dashboard.html', proyectos=proyectos)

if __name__ == '__main__':
    # Ejecutar la app en el puerto 5000, accesible desde cualquier dispositivo en la misma red
    app.run(host='0.0.0.0',port = 5000)