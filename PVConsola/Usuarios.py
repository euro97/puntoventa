class Usuarios:
    def __init__(self, nombre, correo, password, rol):
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.rol = rol

    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self, value):
        if isinstance(value, int) and value > 0:
            self._id_usuario = value
        else:            
            raise ValueError("El id_usuario debe ser un entero positivo.")

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._correo = value
        else:
            raise ValueError("El correo debe ser una cadena no vacía.")

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._password = value
        else:
            raise ValueError("La contraseña debe ser una cadena no vacía.")

    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, value):
        if value in ['Admin', 'Cajero']:
            self._rol = value
        else:
            raise ValueError("El rol debe ser 'Admin' o 'Cajero'.")

    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, value):
        if isinstance(value, bool):
            self._activo = value
        else:
            raise ValueError("El valor de activo debe ser un booleano.")

    def __str__(self):
        return f"{self.id_usuario}, {self.nombre}, {self.correo}, {self.rol}, {self.activo}"
    

