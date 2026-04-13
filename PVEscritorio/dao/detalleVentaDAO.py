from dao.databseDAO import databseDAO

class UsuarioDAO(databseDAO):

    def consultadetalleVenta(self, id_venta):
        self.execute_query("""
            SELECT dv.id_detalle_venta, dv.id_venta, dv.id_producto, p.nombre AS nombre_producto, dv.cantidad, dv.precio_unitario
            FROM detalle_ventas dv
            JOIN productos p ON dv.id_producto = p.id_producto
            WHERE dv.id_venta = %s;
        """, (id_venta,))
        return self.fetchall()
    

    def modificardetalleVenta(self, id_detalle_venta, id_venta, id_producto, cantidad, precio_unitario):
        self.execute_query("""
            UPDATE detalle_ventas
            SET id_venta = %s,
                id_producto = %s,
                cantidad = %s,
                precio_unitario = %s
            WHERE id_detalle_venta = %s;
        """, (id_venta, id_producto, cantidad, precio_unitario, id_detalle_venta))
    
    def eliminardetalleVenta(self, id_detalle_venta):
        self.execute_query("""
            DELETE FROM detalle_ventas
            WHERE id_detalle_venta = %s;
        """, (id_detalle_venta,))

    