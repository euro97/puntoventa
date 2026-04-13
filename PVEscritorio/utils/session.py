# utils/session.py

class Session:
    id_usuario = None
    nombre = None
    rol = None

    @classmethod
    def iniciar_sesion(cls, id_usuario, nombre, rol):
        cls.id_usuario = id_usuario
        cls.nombre = nombre
        cls.rol = rol

    @classmethod
    def cerrar_sesion(cls):
        cls.id_usuario = None
        cls.nombre = None
        cls.rol = None

    @classmethod
    def esta_logueado(cls):
        return cls.id_usuario is not None