class NombreError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El nombre no puede contener carácteres, símbolos o números.'

class ApellidoError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El apellido no puede contener carácteres, símbolos o números.'

class IdError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El ID no existe.'

class CorreoError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El correo debe tener forma -@-.-.'

class DescripcionError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self):
        return 'La descrición no puede superar los 80 caracteres.'

class ProyectoNoEncontradoError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El proyecto no existe'

class TituloError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El título no puede contener carácteres, símbolos o números.'

class DniError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El formato del dni es incorrecto '

class ProyectoNoEncontradoError(Exception):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def __str__(self):
        return 'El proyecto no existe'