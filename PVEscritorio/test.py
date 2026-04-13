from dao.usuarioDAO import UsuarioDAO

with UsuarioDAO() as dao:
    users = dao.login("luis@gmail.com", "12345")

print(users)