import database as db


def consultarProductos():
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM Productos order by id;")
    result = cursor.fetchall()
    db.close(dbconnect)
    return result


def buscaProducto(producto):
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM Productos WHERE unaccent(nombre) ILIKE unaccent(%s);", (f"%{producto}%",))
    result = cursor.fetchall()
    db.close(dbconnect)
    return result   

def agregarProducto(producto):
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("""
                INSERT INTO Productos (nombre, precio, marca, cantidad, tamano)
                VALUES (%s, %s, %s, %s, %s)
            """, (producto.nombre, producto.precio, producto.marca, producto.cantidad, producto.tamano))
    dbconnect.commit()
    db.close(dbconnect)
    return "Agregado"  

def modificarProducto():
    pro = consultarProductos()
    for i in pro:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres editar: \n")
    print("1. Nombre \n2. Precio \n3. Marca \n4. Cantidad \n5. Tamaño")
    campo = int(input("Campo a editar: \n"))
    valor = input("Dame el nuevo valor: \n")

    columnas={
        1: "nombre",
        2: "precio",
        3: "marca",
        4: "cantidad",
        5: "tamano"
    }

    if campo not in columnas:
        print("No existe el campo")
        return
    columna = columnas[campo]

    dbconnect = db.connect()
    cursor = dbconnect.cursor()

    cursor.execute(f"UPDATE productos SET {columna} = %s WHERE id = %s;",(valor,resp))
    dbconnect.commit()
    db.close(dbconnect)
    print("Producto actualizado")



def eliminarProducto():
    print("No se recomienda eliminar, se recomienda mantener la cantidad en 0")
    pro = consultarProductos()
    for i in pro:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres eliminar: \n")
    confirma = input("Seguro que deseas eliminarlo? s/n:\n")
    if confirma == "s":
        dbconnect = db.connect()
        cursor = dbconnect.cursor()
        cursor.execute(f"DELETE FROM productos WHERE id = %s;",(resp,))
        dbconnect.commit()
        db.close(dbconnect)
        print("Producto eliminado . . .")