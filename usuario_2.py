import sqlite3
import re
from errores import NombreError, ApellidoError, IdError, CorreoError, DniError
import bcrypt
import pandas as pd

class Usuario:
    def __init__(self, dni, contrasena,nombre, apellido, correo):
        self.dni = dni
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}"

class UsuarioBase:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS usuarios ('
            'dni TEXT UNIQUE, '
            'pasword TEXT NOT NULL,'
            'nombre TEXT, '
            'apellido TEXT, '
            'correo TEXT)'
        )
        self.conn.commit()

    def consultar_usuarios(self):
        self.cursor.execute('SELECT * FROM usuarios')
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
        '''self.cursor.execute('SELECT * FROM usuarios')
        usuarios = self.cursor.fetchall()
        df = pd.DataFrame(usuarios, columns=['DNI', 'Password', 'Nombre', 'Apellido', 'Correo'])
        print(df)'''

    # Función que hashea las contraseñas
    def hashear_contrasena(self,contrasena):
        # Con bcrypt.hashpw creamos un hash de la contraseña
        # contrasena.encode() convierte la contraseña a bytes
        # bcrypt.gensalt() añade un valor al hasheo de la contraseña para asegurar que nadie comparta contraseña
        contrasena_hasheada = bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
        return contrasena_hasheada

    # Función que comprueba si el hash coincide con la contraseña
    def validar_hasheo(self, contrasena, contrasena_hasheada):
        # bcrypt.checkpw() compara las contraseñas y devuelve True si coinciden o false si no
        # contrasena.encode() convierte la contraseña a bytes
        verificacion = bcrypt.checkpw(contrasena.encode(), contrasena_hasheada)
        return verificacion
    def validar_dni(self):
        while True:
            valido = r'[0-9]{8}[A-Z]'
            try:
                dni = input("Dni: ")
                if not re.match(valido, dni):
                    raise DniError(dni)
            except DniError as de:
                print(de)
                continue
            else:
                break
        return dni

    def validar_nombre(self):
        while True:
            try:
                nombre = input("Nombre: ")
                if not nombre.isalpha():
                    raise NombreError(nombre)
            except NombreError as ne:
                print(ne)
                continue
            else:
                break
        return nombre

    def validar_apellidos(self):
        while True:
            try:
                apellido = input("Apellido: ")
                if not apellido.isalpha():
                    raise ApellidoError(apellido)
            except ApellidoError as ae:
                print(ae)
                continue
            else:
                break

        return apellido
    def validar_correo(self):
        while True:
            valido = r'[a-zA-Z0-9._]+@[a-z]+\.[a-zA-Z]{2,}'
            try:
                correo = input("Correo: ")
                if not re.match(valido, correo):
                    raise CorreoError(correo)
            except CorreoError as ce:
                print(ce)
                continue
            else:
                break

        return correo

    def crear_usuario(self):
        dni = self.validar_dni()
        contrasena = input("Introduce tu contraseña: ")
        contrasena_hasheada = self.hashear_contrasena(contrasena)
        nombre = self.validar_nombre()
        apellido = self.validar_apellidos()
        correo = self.validar_correo()

        self.cursor.execute(
            'INSERT INTO usuarios (dni, pasword,nombre, apellido, correo) VALUES (?, ?,?, ?, ?)',
            (dni, contrasena_hasheada,nombre, apellido, correo)
        )
        self.conn.commit()
        print("Usuario creado correctamente.")
        Usuario(dni, contrasena_hasheada,nombre, apellido,correo)

    def editar_usuario(self):
        dni = input("Ingrese el DNI del usuario a editar: ")
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise DniError(dni)
        except DniError as ex:
            print(ex)
            return

        print('Para editar el Nombre introduzca el 1.')
        print('Para editar el Apellido introduzca el 2.')
        print('Para editar el correo introduzca el 3.')
        editar = int(input('Elige que quieres editar: '))

        if editar == 1:
            nombre = self.validar_nombre()
            self.cursor.execute('UPDATE usuarios SET nombre = ? WHERE dni = ?', (nombre, dni))
            self.conn.commit()
        elif editar == 2:
            apellido = self.validar_apellidos()
            self.cursor.execute('UPDATE usuarios SET apellido = ? WHERE dni = ?', (apellido, dni))
            self.conn.commit()
        elif editar == 3:
            correo = self.validar_correo()
            self.cursor.execute('UPDATE usuarios SET correo = ? WHERE dni = ?', (correo, dni))
            self.conn.commit()

        print("Usuario editado correctamente.")

    def eliminar_usuario(self):
        dni = input("Ingrese el Dni del usuario a eliminar: ")
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise DniError(dni)
        except DniError as ex:
            print(ex)
            return

        self.cursor.execute('DELETE FROM usuarios WHERE dni = ?', (dni,))
        self.conn.commit()
        print(f"Usuario con DNI {dni}, eliminado correctamente.")

'''usuario = UsuarioBase()
usuario.consultar_usuarios()'''