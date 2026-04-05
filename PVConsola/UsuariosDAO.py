import database as db

def consultarUsuarios():
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM Usuarios order by id_usuario;")
    result = cursor.fetchall()
    db.close(dbconnect)
    return result

def buscaUsuario(nombre):
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE unaccent(nombre) ILIKE unaccent(%s);", (f"%{nombre}%",))
    result = cursor.fetchall()
    db.close(dbconnect)
    return result

def agregarUsuario(usuario):
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("""
                INSERT INTO Usuarios (nombre, correo, rol, password)
                VALUES (%s, %s, %s, %s)
            """, (usuario.nombre, usuario.correo, usuario.rol, usuario.password))
    dbconnect.commit()
    db.close(dbconnect)
    return "Agregado"

def modificarUsuario():
    per = consultarUsuarios()
    for i in per:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres editar: \n")
    print("1. Nombre \n2. Correo \n3. Rol (Admin o Cajero) \n4. Password \n5. Activo (True o False)")
    campo = int(input("Campo a editar: \n"))
    valor = input("Dame el nuevo valor: \n")

    columnas={
        1: "nombre",
        2: "correo",
        3: "rol",
        4: "password",
        5: "activo"

    }

    if campo not in columnas:
        print("No existe el campo")
        return
    columna = columnas[campo]

    dbconnect = db.connect()
    cursor = dbconnect.cursor()

    cursor.execute(f"UPDATE Usuarios SET {columna} = %s WHERE id_usuario = %s;",(valor,resp))
    dbconnect.commit()
    db.close(dbconnect)
    print("Usuario actualizado")

def eliminarUsuario():
    per = consultarUsuarios()
    for i in per:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres eliminar: \n")
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id_usuario = %s;", (resp,))
    dbconnect.commit()
    db.close(dbconnect)
    print("Usuario eliminado")

