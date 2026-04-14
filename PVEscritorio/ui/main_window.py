from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from utils.session import Session

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS - Menú Principal")
        self.setFixedSize(400, 300)

        self.lblUser = QLabel(f"Bienvenido: {Session.nombre} | Rol: {Session.rol}")

        self.btnProductos = QPushButton("Inventario / Productos")
        self.btnVentas = QPushButton("Ventas")
        self.btnCerrarSesion = QPushButton("Cerrar Sesión")

        self.btnProductos.clicked.connect(self.abrir_productos)
        self.btnVentas.clicked.connect(self.abrir_ventas)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

        layout = QVBoxLayout()
        layout.addWidget(self.lblUser)
        layout.addWidget(self.btnProductos)
        layout.addWidget(self.btnVentas)
        layout.addWidget(self.btnCerrarSesion)

        self.setLayout(layout)

    def abrir_productos(self):
        if Session.rol != "Admin":
            QMessageBox.warning(self, "Acceso Denegado", "Solo Admin puede modificar productos.")
            return

        from ui.productos_window import ProductosWindow
        self.winProductos = ProductosWindow()
        self.winProductos.show()

    def abrir_ventas(self):
        from ui.ventas_window import VentasWindow
        self.winVentas = VentasWindow()
        self.winVentas.show()

    def cerrar_sesion(self):
        Session.cerrar_sesion()
        from ui.loguin_window import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()