class Producto:
    def __init__(self, id_producto, nombre, precio, marca, cantidad, tamano):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.cantidad = cantidad
        self.tamano = tamano

    def __str__(self):
        print("id_producto\tnombre\tprecio\tmarca\tcantidad\ttamano")
        str = f"{self.id_producto}\t'{self.nombre}'\t{self.precio}\t'{self.marca}'\t{self.cantidad}\t'{self.tamano}'"
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
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, value):
        if value < 0 or value is None:
            raise ValueError("El precio no puede ser negativo ni estar vacío.")
        self._precio = value
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, value):
        if not value:
            raise ValueError("La marca no puede estar vacía.")
        self._marca = value
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, value):
        if value < 0 or value is None:
            raise ValueError("La cantidad no puede ser negativa ni estar vacía.")
        self._cantidad = value
    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self, value):
        if not value:
            raise ValueError("El tamaño no puede estar vacío.")
        self._tamano = value
    
    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "marca": self.marca,
            "cantidad": self.cantidad,
            "tamano": self.tamano
        }