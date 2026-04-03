class Ventas:
    def __init__(self, id_venta, fecha, total, metodo_pago, cliente, id_usuario):
        self.id_venta = id_venta
        self.fecha = fecha
        self.total = total
        self.metodo_pago = metodo_pago
        self.cliente = cliente
        self.id_usuario = id_usuario

    @property
    def id_venta(self):
        return self._id_venta
    @id_venta.setter
    def id_venta(self, value):
        if isinstance(value, int) and value > 0:
            self._id_venta = value
        else:            
            raise ValueError("El id_venta debe ser un entero positivo.")
    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._fecha = value
        else:
            raise ValueError("La fecha debe ser una cadena no vacía.")
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._total = value
        else:
            raise ValueError("El total debe ser un número no negativo.")
    @property
    def metodo_pago(self):
        return self._metodo_pago
    @metodo_pago.setter
    def metodo_pago(self, value):
        if value in ['Efectivo', 'Tarjeta', 'Transferencia']:
            self._metodo_pago = value
        else:
            raise ValueError("El método de pago debe ser 'Efectivo', 'Tarjeta' o 'Transferencia'.")
    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._cliente = value
        else:
            raise ValueError("El cliente debe ser una cadena no vacía.")
    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, value):
        if isinstance(value, int) and value > 0:
            self._id_usuario = value
        else:            
            raise ValueError("El id_usuario debe ser un entero positivo.")
    def __str__(self):
        return f"{self.id_venta}, {self.fecha}, {self.total}, {self.metodo_pago}, {self.cliente}, {self.id_usuario}"

