class Venta:
    def __init__(self, id_venta, fecha, total, metodo_pago, cliente, id_usuario):
        self.id_venta = id_venta
        self.fecha = fecha
        self.total = total
        self.metodo_pago = metodo_pago
        self.cliente = cliente
        self.id_usuario = id_usuario

    def __str__(self):
        print(f"Venta ID\tfecha\t\tTotal\tMétodo de Pago\tCliente\tID Usuario")
        str = f"{self.id_venta}\t{self.fecha}\t{self.total}\t{self.metodo_pago}\t{self.cliente}\t{self.id_usuario}"
        return str
    
    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "total": self.total,
            "metodo_pago": self.metodo_pago,
            "cliente": self.cliente,
            "id_usuario": self.id_usuario
        }

    @property
    def id_venta(self):
        return self._id_venta
    @id_venta.setter
    def id_venta(self, value):
        if value < 0:
            raise ValueError("El ID de venta no puede ser negativo.")
        self._id_venta = value
    
    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("La fecha debe ser una cadena de texto y no estar vacía.")
        self._fecha = value
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El total debe ser un número y superar cero.")
        if value <= 0:
            raise ValueError("El total debe ser un número positivo.")
        self._total = value
    @property
    def metodo_pago(self):
        return self._metodo_pago
    @metodo_pago.setter
    def metodo_pago(self, value):
        if not isinstance(value, str):
            raise ValueError("El método de pago debe ser una cadena de texto.")
        values = ["Efectivo", "Tarjeta", "Transferencia"]
        if value not in values:
            raise ValueError(f"El método de pago debe ser uno de los siguientes: {', '.join(values)}.")
        value.capitalize()
        self._metodo_pago = value


    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, value):
        if not isinstance(value, str):
            raise ValueError("El cliente debe ser una cadena de texto.")
        self._cliente = value
    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, value):
        if value < 0:
            raise ValueError("El ID de usuario no puede ser negativo.")
        self._id_usuario = value    
    
