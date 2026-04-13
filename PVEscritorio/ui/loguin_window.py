from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt

from dao.usuarioDAO import UsuarioDAO
from utils.session import Session


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login para Punto de venta")
        self.setFixedSize(350, 250)

        # Titulo
        self.lblTitulo = QLabel("Iniciar Sesión")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Correo
        self.lblCorreo = QLabel("Correo:")
        self.txtCorreo = QLineEdit()
        self.txtCorreo.setPlaceholderText("correo@gmail.com")

        # Password
        self.lblPassword = QLabel("Contraseña:")
        self.txtPassword = QLineEdit()
        self.txtPassword.setPlaceholderText("Contraseña")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        # Boton
        self.btnLogin = QPushButton("Ingresar")
        self.btnLogin.clicked.connect(self.login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.lblTitulo)
        layout.addWidget(self.lblCorreo)
        layout.addWidget(self.txtCorreo)
        layout.addWidget(self.lblPassword)
        layout.addWidget(self.txtPassword)
        layout.addWidget(self.btnLogin)

        self.setLayout(layout)

    def login(self):
        correo = self.txtCorreo.text().strip()
        password = self.txtPassword.text().strip()

        if correo == "" or password == "":
            QMessageBox.warning(self, "Error", "Debes llenar todos los campos")
            return

        with UsuarioDAO() as dao:
            user = dao.login(correo, password)

        if user:
            # user = (id_usuario, nombre, rol)
            Session.iniciar_sesion(user[0], user[1], user[2])

            QMessageBox.information(self, "Correcto", f"Bienvenido {user[1]}")

            # Abrir ventana principal
            from ui.main_window import MainWindow
            self.main = MainWindow()
            self.main.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")