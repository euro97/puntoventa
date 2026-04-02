class Producto:
    def __init__(self, nombre,precio,marca,cantidad,tamano):
        self._nombre = nombre  
        self._precio = precio
        self._marca = marca
        self._cantidad = cantidad
        self._tamano = tamano

    @property
    def nombre(self):
        """Nombre del producto"""
        
        return self._nombre
    
    @property
    def precio(self):
        """Precio del producto"""
        return self._precio
    
    @property
    def marca(self):
        """Marca del producto"""
        return self._marca
    
    @property
    def cantidad(self):
        """Cantidad del producto"""
        return self._cantidad
    
    @property
    def tamano(self):
        """tamano del producto"""
        return self._tamano

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Setter: Modifica el valor con validación"""
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre no puede estar vacío.")

    @precio.setter
    def precio(self, nuevo_precio):
        """Setter: Modifica el valor con validación"""
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede estar vacío.")

    @marca.setter
    def marca(self, nuevo_marca):
        """Setter: Modifica el valor con validación"""
        if len(nuevo_marca) > 0:
            self._marca = nuevo_marca
        else:
            print("Error: La marca no puede estar vacío.")

    @cantidad.setter
    def cantidad(self, nuevo_cantidad):
        """Setter: Modifica el valor con validación"""
        if nuevo_cantidad > 0:
            self._cantidad = nuevo_cantidad
        else:
            print("Error: La Cantidad no puede estar vacía.")

    @tamano.setter
    def tamano(self, nuevo_tamano):
        """Setter: Modifica el valor con validación"""
        if len(nuevo_tamano) > 0:
            self._tamano = nuevo_tamano
        else:
            print("Error: El tamaño no puede estar vacío.")

    def __str__(self):
        return f"{self.nombre}, {self.precio}, {self.marca}, {self.cantidad}, {self.tamano}"