from dao.databseDAO import databseDAO

class VentaDAO(databseDAO):

    # ---------------- CREAR VENTA COMPLETA ----------------
    def crearVenta(self, cliente, metodo_pago, id_usuario, detalles):
        """
        detalles = [
            {"id_producto": 1, "cantidad": 2},
            {"id_producto": 3, "cantidad": 1}
        ]
        """

        # Insertar venta (total en 0 temporalmente)
        self.execute_query("""
            INSERT INTO ventas (total, metodo_pago, cliente, id_usuario)
            VALUES (0, %s, %s, %s)
            RETURNING id_venta;
        """, (metodo_pago, cliente, id_usuario))

        id_venta = self.fetchone()[0]

        # Insertar detalles + actualizar inventario
        for d in detalles:
            id_producto = d["id"]
            cantidad = d["cantidad"]

            # Validar stock
            self.execute_query("SELECT cantidad, precio FROM productos WHERE id = %s;", (id_producto,))
            prod = self.fetchone()

            if not prod:
                raise Exception("Producto no existe")

            stock = prod[0]
            precio = prod[1]

            if stock < cantidad:
                raise Exception(f"Stock insuficiente para producto {id_producto}")

            # Insertar detalle
            self.execute_query("""
                INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s);
            """, (id_venta, id_producto, cantidad, precio))

            # Restar inventario
            self.execute_query("""
                UPDATE productos
                SET cantidad = cantidad - %s
                WHERE id_producto = %s;
            """, (cantidad, id_producto))

        # Actualizar total de venta
        self.execute_query("""
            UPDATE ventas
            SET total = (
                SELECT SUM(cantidad * precio_unitario)
                FROM detalle_venta
                WHERE id_venta = %s
            )
            WHERE id_venta = %s;
        """, (id_venta, id_venta))

        return id_venta


    # ---------------- CONSULTAR VENTAS (TICKET COMPLETO) ----------------
    def consultarVentas(self):
        self.execute_query("""
            SELECT 
                v.id_venta,
                dv.id_detalle,
                v.total,
                v.metodo_pago,
                v.cliente,
                p.nombre,
                p.precio,
                dv.cantidad,
                p.tamano,
                (dv.cantidad * dv.precio_unitario) AS subtotal
            FROM ventas v
            JOIN detalle_venta dv ON v.id_venta = dv.id_venta
            JOIN productos p ON dv.id_producto = p.id_producto
            ORDER BY v.id_venta, dv.id_detalle;
        """)
        return self.fetchall()


    # ---------------- CONSULTAR SOLO VENTAS ----------------
    def consultarSoloVentas(self):
        self.execute_query("""
            SELECT id_venta, fecha, total, metodo_pago, cliente, id_usuario
            FROM ventas
            ORDER BY id_venta;
        """)
        return self.fetchall()


    # ---------------- ELIMINAR VENTA ----------------
    def eliminarVenta(self, id_venta):
        # Regresar stock antes de borrar
        self.execute_query("""
            SELECT id_producto, cantidad
            FROM detalle_venta
            WHERE id_venta = %s;
        """, (id_venta,))
        detalles = self.fetchall()

        for d in detalles:
            self.execute_query("""
                UPDATE productos
                SET cantidad = cantidad + %s
                WHERE id_producto = %s;
            """, (d[1], d[0]))

        # Borrar venta (borra detalle_venta por ON DELETE CASCADE)
        self.execute_query("DELETE FROM ventas WHERE id_venta = %s;", (id_venta,))


    # ---------------- RECALCULAR TOTAL ----------------
    def recalcularTotal(self, id_venta):
        self.execute_query("""
            UPDATE ventas
            SET total = (
                SELECT SUM(cantidad * precio_unitario)
                FROM detalle_venta
                WHERE id_venta = %s
            )
            WHERE id_venta = %s;
        """, (id_venta, id_venta))