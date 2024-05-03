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
        while True:
            try:
                id = int(input("ID: "))
                if id < 100 or id > 999:
                    raise IdError(id)
            except IdError as ie:
                print(ie)
                continue
            else:
                break
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

        #self.añadir_usuario(id,nombre,apellido,correo)

        nuevo_usuario = pd.DataFrame({
            "ID": [id],
            "Nombre": [nombre],
            "Apellido": [apellido],
            "Correo": [correo]
            })
        nuevo_usuario.to_csv('usuario_base.csv', mode='a', header=True, index=False)
        return self.lista_usuarios

    def editar_usuario(self,id_usuario):
        base_usuario = pd.read_csv('usuario_base.csv')

        print('El ID no se puede editar.')
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

    def eliminar_usuario(self,id_usuario):
        base_usuario = pd.read_csv('usuario_base.csv')
        #base_usuario = base_usuario[base_usuario['ID'] != id_usuario]
        base_usuario.drop(base_usuario[base_usuario['ID'] == id_usuario].index, inplace=True)
        base_usuario.to_csv('usuario_base.csv', index=False)
        print(f"Usuario con ID {id_usuario}, eliminado correctamente.")

    '''@classmethod
    def añadir_usuario(cls,id,nombre,apellido,correo):
        cls.lista_usuarios.append(Usuario(id, nombre, apellido, correo))'''

base= UsuarioBase()
base.editar_usuario(123)