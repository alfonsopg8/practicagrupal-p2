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
