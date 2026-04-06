class detalleVenta:
    def __init__(self, idDetalleVenta, idVenta, idProducto, cantidad, precioUnitario):
        self.idDetalleVenta = idDetalleVenta
        self.idVenta = idVenta
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario

    def __str__(self):
        print(f"DetalleVenta ID\tVenta ID\tProducto ID\tCantidad\tPrecio Unitario")
        str = f"{self.idDetalleVenta}\t{self.idVenta}\t{self.idProducto}\t{self.cantidad}\t{self.precioUnitario}"
        return str
    
    def to_dict(self):
        return {
            "idDetalleVenta": self.idDetalleVenta,
            "idVenta": self.idVenta,
            "idProducto": self.idProducto,
            "cantidad": self.cantidad,
            "precioUnitario": self.precioUnitario
        }
    @property
    def idDetalleVenta(self):
        return self._idDetalleVenta
    @idDetalleVenta.setter
    def idDetalleVenta(self, value):
        if value < 0:
            raise ValueError("El ID de detalle de venta no puede ser negativo.")
        self._idDetalleVenta = value
    @property
    def idVenta(self):
        return self._idVenta
    @idVenta.setter
    def idVenta(self, value):
        if value < 0:
            raise ValueError("El ID de venta no puede ser negativo.")
        self._idVenta = value
    @property
    def idProducto(self):
        return self._idProducto
    @idProducto.setter
    def idProducto(self, value):
        if value < 0:
            raise ValueError("El ID de producto no puede ser negativo.")
        self._idProducto = value
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, value):
        if not isinstance(value, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if value <= 0:
            raise ValueError("La cantidad debe ser un número mayor a cero.")
        self._cantidad = value
    @property
    def precioUnitario(self):
        return self._precioUnitario
    @precioUnitario.setter
    def precioUnitario(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El precio unitario debe ser un número.")
        if value <= 0:
            raise ValueError("El precio unitario debe ser un número mayor a cero.")
        self._precioUnitario = value

    