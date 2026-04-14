from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox
)

from dao.productoDAO import ProductoDAO

class ProductosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventario - Productos")
        self.setFixedSize(700, 400)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Marca", "Precio", "Cantidad", "Tamaño"])

        self.btnCargar = QPushButton("Cargar Productos")
        self.btnCargar.clicked.connect(self.cargarProductos)

        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        layout.addWidget(self.btnCargar)

        self.setLayout(layout)

        self.cargarProductos()

    def cargarProductos(self):
        try:
            with ProductoDAO() as dao:
                productos = dao.consultarProductos()

            self.tabla.setRowCount(len(productos))

            for fila, p in enumerate(productos):
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(p[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(p[1])))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(p[2])))
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(p[3])))
                self.tabla.setItem(fila, 4, QTableWidgetItem(str(p[4])))
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(p[5])))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar productos.\n{e}")