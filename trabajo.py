import pandas as pd
import numpy as np
from errores import NombreError,ApellidoError,IdError,CorreoError
import re


class Usuario:
    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}"


class UsuarioBase:
    lista_usuarios = []
    def __init__(self):
        pass

    def crear_usuario(self):
        try:
            base_usuario = pd.read_csv('usuario_base.csv')
            num_usuarios = len(base_usuario) +2
        except FileNotFoundError:
            num_usuarios = 1

        id = num_usuarios
        print(f'Tu id es {id}')
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

        nuevo_usuario = pd.DataFrame({
            "ID": [id],
            "Nombre": [nombre],
            "Apellido": [apellido],
            "Correo": [correo]
            })
        if id==1:
            nuevo_usuario.to_csv('usuario_base.csv', mode='w', header=True, index=False)
        else:
            nuevo_usuario.to_csv('usuario_base.csv', mode='a', header=False, index=False)


    def editar_usuario(self):
        base_usuario = pd.read_csv('usuario_base.csv')
        while True:
            id_usuario = int(input("Ingrese el ID del usuario a editar: "))
            try:
                if id_usuario <= 0 or id_usuario > len(base_usuario) + 2:
                    raise IdError
            except IdError as ex:
                print(ex)
                continue
            else:
                print('Para editar el Nombre introduzca el 1.')
                print('Para editar el Apellido introduzca el 2.')
                print('Para editar el correo introduzca el 3.')
                editar = int(input('Elige que quieres editar: '))
                if editar == 1:
                    while True:
                        try:
                            nombre = input("Nuevo nombre: ")
                            if not nombre.isalpha():
                                raise NombreError(nombre)
                        except NombreError as ne:
                            print(ne)
                            continue
                        else:
                            base_usuario.loc[base_usuario['ID'] == id_usuario, 'Nombre'] = nombre
                            break
                elif editar == 2:
                    while True:
                        try:
                            apellido = input("Nuevo Apellido: ")
                            if not apellido.isalpha():
                                raise ApellidoError(apellido)
                        except ApellidoError as ae:
                            print(ae)
                            continue
                        else:
                            base_usuario.loc[base_usuario['ID'] == id_usuario, 'Apellido'] = apellido
                            break
                elif editar == 3:
                    while True:
                        valido = r'[a-zA-Z0-9._]+@[a-z]+\.[a-zA-Z]{2,}'
                        try:
                            correo = input("Nuevo correo: ")
                            if not re.match(valido, correo):
                                raise CorreoError(correo)
                        except CorreoError as ce:
                            print(ce)
                            continue
                        else:
                            base_usuario.loc[base_usuario['ID'] == id_usuario, 'Correo'] = correo
                            break
                base_usuario.to_csv('usuario_base.csv', index=False)
                break

    def eliminar_usuario(self):
        base_usuario = pd.read_csv('usuario_base.csv')
        while True:
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            try:
                if id_usuario <=0 or id_usuario > len(base_usuario)+2:
                    raise IdError
            except IdError as ex:
                print(ex)
                continue
            else:
                #base_usuario = base_usuario[base_usuario['ID'] != id_usuario]
                base_usuario.drop(base_usuario[base_usuario['ID'] == id_usuario].index, inplace=True)
                base_usuario.to_csv('usuario_base.csv', index=False)
                print(f"Usuario con ID {id_usuario}, eliminado correctamente.")
                break

    '''@classmethod
    def añadir_usuario(cls,id,nombre,apellido,correo):
        cls.lista_usuarios.append(Usuario(id, nombre, apellido, correo))'''

base= UsuarioBase()
base.editar_usuario()

