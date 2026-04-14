from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox
)

from dao.ventaDAO import VentaDAO

class VentasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventas")
        self.setFixedSize(900, 450)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels([
            "ID Venta", "ID Detalle", "Cliente", "Producto",
            "Cantidad", "Método Pago", "Total", "Subtotal"
        ])

        self.btnCargar = QPushButton("Cargar Ventas")
        self.btnCargar.clicked.connect(self.cargarVentas)

        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        layout.addWidget(self.btnCargar)

        self.setLayout(layout)

        self.cargarVentas()

    def cargarVentas(self):
        try:
            with VentaDAO() as dao:
                ventas = dao.consultarVentas()

            self.tabla.setRowCount(len(ventas))

            for fila, v in enumerate(ventas):
                # Ajusta según tu SELECT en consultarVentas()
                # v = (id_venta, id_detalle, total, metodo_pago, cliente, nombre_producto, precio, cantidad, tamano, subtotal)

                self.tabla.setItem(fila, 0, QTableWidgetItem(str(v[0])))  # id_venta
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(v[1])))  # id_detalle
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(v[4])))  # cliente
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(v[5])))  # producto
                self.tabla.setItem(fila, 4, QTableWidgetItem(str(v[7])))  # cantidad
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(v[3])))  # metodo_pago
                self.tabla.setItem(fila, 6, QTableWidgetItem(str(v[2])))  # total
                self.tabla.setItem(fila, 7, QTableWidgetItem(str(v[9])))  # subtotal

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar ventas.\n{e}")