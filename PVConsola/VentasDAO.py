import database as db

def consultarVentas():
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT \
    v.id_venta,\
    v.total,\
    v.metodo_pago,\
    v.cliente,\
    p.nombre,\
    p.precio,\
    dv.cantidad,\
    p.tamano,\
    (dv.precio_unitario * dv.cantidad) AS subtotal \
FROM ventas v \
JOIN detalle_venta dv ON v.id_venta = dv.id_venta \
JOIN productos p ON dv.id_producto = p.id \
ORDER BY v.id_venta;")
    result = cursor.fetchall()
    db.close(dbconnect)
    return result

def agregarVenta(venta):
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("""
                INSERT INTO Ventas (id_producto, cantidad, total)
                VALUES (%s, %s, %s)
            """, (venta.id_producto, venta.cantidad, venta.total))
    dbconnect.commit()
    db.close(dbconnect)
    return "Agregado"

def eliminarVenta():
    ven = consultarVentas()
    for i in ven:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres eliminar: \n")
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("DELETE FROM Ventas WHERE id = %s;", (resp,))
    dbconnect.commit()
    db.close(dbconnect)
    print("Venta eliminada")

def modificarVenta():
    ven = consultarVentas()
    for i in ven:
        print(f" {i[0]} \t  {i[1]}")
    resp = input(f"Dame el id que quieres editar: \n")
    print("1. Id Producto \n2. Cantidad \n3. Total")
    campo = int(input("Campo a editar: \n"))
    valor = input("Dame el nuevo valor: \n")

    columnas={
        1: "id_producto",
        2: "cantidad",
        3: "total"
    }

    if campo not in columnas:
        print("No existe el campo")
        return
    columna = columnas[campo]

    dbconnect = db.connect()
    cursor = dbconnect.cursor()

    cursor.execute(f"UPDATE Ventas SET {columna} = %s WHERE id = %s;",(valor,resp))
    dbconnect.commit()
    db.close(dbconnect)
    print("Venta actualizada")
    