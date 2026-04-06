class Usuario:
    def __init__(self, id_usuario, nombre, correo, password, rol, activo = True ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.rol = rol
        self.activo = activo

    def __str__(self):
        print("id_usuario\tnombre\tcorreo\trol\tactivo")
        str = f"{self.id_usuario}\t'{self.nombre}'\t'{self.correo}'\t'{self.rol}'\t{self.activo}"
        return str
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, value):
        if not value:
            raise ValueError("El correo no puede estar vacío.")
        self._correo = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("La contraseña no puede estar vacía.")
        self._password = value

    @property
    def rol(self):
        return self._rol
    @rol.setter
    def rol(self, value):
        if not value:
            raise ValueError("El rol no puede estar vacío.")
        self._rol = value

    @property
    def activo(self):
        return self._activo
    @activo.setter
    def activo(self, value):
        if not isinstance(value, bool):
            raise ValueError("El estado de activo debe ser un valor booleano.")
        self._activo = value

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
            "rol": self.rol,
            "activo": self.activo
        }
    