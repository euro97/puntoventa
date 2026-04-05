import database as db
import productoDAO as pd
import UsuariosDAO as ud

def consultarVentas():
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("SELECT \
    v.id_venta, \
    dv.id_detalle,\
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
ORDER BY v.id_venta, dv.id_detalle;")
    result = cursor.fetchall()
    db.close(dbconnect)
    return result

def agregarVenta():
    vender = []
    opciones = ["Efectivo", "Tarjeta", "Transferencia"]
    idus = 0
    terminaventa = 'n'
    while True:
        vendedor = input("Nombre de vendedor:\n")
        user = ud.buscaUsuario(vendedor)

        if not user:
            print("Usuario no encontrado, por favor ingresa un usuario válido.\n")
        else:
            idus = int(user[0][0])
            break   # sale del ciclo cuando ya existe


    while terminaventa.lower() != 's':
        productos = pd.consultarProductos()
        for i in productos:
            print(f"{i[0]} \t {i[1]}")
        id_producto = int(input("Dame el id del producto que quieres vender: \n"))
        cantidad = int(input("Dame la cantidad: \n"))
        prod = pd.buscaIDProducto(id_producto)
        vender.append((id_producto, cantidad, float(prod[0][2]), prod[0][1]))
        terminaventa = input("¿Terminar venta? (s/n): \n")

    while True:
        metodopago = input("Dame el método de pago (efectivo/tarjeta/transferencia): \n").strip().lower()
        metodopago = metodopago.capitalize()

        if metodopago in opciones:
            break
        else:
            print("Método inválido. Solo puedes usar: efectivo, tarjeta o transferencia.\n")
   
    cliente = input("Dame el nombre del cliente: \n")
    
    print("\n\n\n\nDetalle de la venta:\n")
    for i in vender:
        print(f"Producto: {i[3]}, Cantidad: {i[1]}, Precio Unitario: {i[2]}, Subtotal: {i[1] * i[2]}")

    total = sum(cantidad * precio for _, cantidad, precio, _ in vender)
    print(f"Total a pagar: {total}")
    print(f"Vendedor: {vendedor}, \nMétodo de pago: {metodopago}, \nCliente: {cliente}")

    
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("""
                INSERT INTO Ventas (cliente, metodo_pago, total, id_usuario)
                VALUES (%s, %s, %s, %s)
            """, (cliente, metodopago, total, idus))
    cursor.execute("""SELECT id_venta
                    FROM ventas
                    ORDER BY id_venta DESC
                    LIMIT 1;""")
    id_venta = cursor.fetchone()[0]
    for id_producto, cantidad, precio_unitario, _ in vender:
        cursor.execute("""
                    INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario)
                    VALUES (%s, %s, %s, %s)
                """, (id_venta, id_producto, cantidad, precio_unitario))
    dbconnect.commit()
    db.close(dbconnect)
    return "Agregado"

def eliminarVenta():
    ven = consultarVentas()
    for i in ven:
        print(f" {i[0]} \t  {i[2]}")
    resp = input(f"Dame el id que quieres eliminar: \n")
    dbconnect = db.connect()
    cursor = dbconnect.cursor()
    cursor.execute("DELETE FROM Ventas WHERE id_venta = %s;", (resp,))
    cursor.execute("DELETE FROM detalle_venta WHERE id_venta = %s;", (resp,))
    dbconnect.commit()
    db.close(dbconnect)
    print("Venta eliminada")

def modificarVenta():
    ven = consultarVentas()

    for i in ven:
        print(f"ID Venta: {i[0]}, ID Detalle: {i[1]}, Cliente: {i[4]}, Producto: {i[5]}, Cantidad: {i[7]}, Método de Pago: {i[3]}, Total: {i[2]}")

    idventa = input("\nDame el ID de la venta que quieres editar: \n")

    print("\n1. Producto \n2. Cantidad \n3. Metodo de Pago \n4. Cliente")
    campo = int(input("Campo a editar: \n"))

    dbconnect = db.connect()
    cursor = dbconnect.cursor()

    # --- Producto ---
    if campo == 1:
        iddetalle = input("Dame el ID Detalle del producto a cambiar: \n")
        print("\nProductos disponibles:")
        for producto in pd.consultarProductos():
            print(f"ID: {producto[0]}, Nombre: {producto[1]}\n")
        nuevo_id_producto = input("Dame el nuevo ID del producto: \n")

        cursor.execute("""
            UPDATE detalle_venta
            SET id_producto = %s,
                precio_unitario = (SELECT precio FROM productos WHERE id = %s)
            WHERE id_detalle = %s AND id_venta = %s;
        """, (nuevo_id_producto, nuevo_id_producto, iddetalle, idventa))

        # recalcular total
        cursor.execute("""
            UPDATE ventas
            SET total = (
                SELECT SUM(cantidad * precio_unitario)
                FROM detalle_venta
                WHERE id_venta = %s
            )
            WHERE id_venta = %s;
        """, (idventa, idventa))

    # --- Cantidad ---
    elif campo == 2:
        iddetalle = input("Dame el ID Detalle del producto a cambiar: \n")
        nueva_cantidad = input("Dame la nueva cantidad: \n")

        cursor.execute("""
            UPDATE detalle_venta
            SET cantidad = %s
            WHERE id_detalle = %s AND id_venta = %s;
        """, (nueva_cantidad, iddetalle, idventa))

        # recalcular total
        cursor.execute("""
            UPDATE ventas
            SET total = (
                SELECT SUM(cantidad * precio_unitario)
                FROM detalle_venta
                WHERE id_venta = %s
            )
            WHERE id_venta = %s;
        """, (idventa, idventa))

    # --- Metodo de pago ---
    elif campo == 3:
        opciones = ["Efectivo", "Tarjeta", "Transferencia"]

        while True:
            metodopago = input("Nuevo método de pago (efectivo/tarjeta/transferencia): \n").strip().lower().capitalize()
            if metodopago in opciones:
                break
            print("Método inválido.")

        cursor.execute("""
            UPDATE ventas
            SET metodo_pago = %s
            WHERE id_venta = %s;
        """, (metodopago, idventa))

    # --- Cliente ---
    elif campo == 4:
        nuevo_cliente = input("Dame el nuevo cliente: \n")

        cursor.execute("""
            UPDATE ventas
            SET cliente = %s
            WHERE id_venta = %s;
        """, (nuevo_cliente, idventa))

    else:
        print("No existe el campo")
        db.close(dbconnect)
        return

    dbconnect.commit()
    db.close(dbconnect)
    print("\nVenta actualizada correctamente")
    