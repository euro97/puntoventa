from dao.databseDAO import DatabaseDAO

class UsuarioDAO(DatabaseDAO):

    def consultarProductos(self):
        self.execute("""
            SELECT id_producto, nombre, descripcion, precio, stock
            FROM productos
            ORDER BY id_producto;
        """)
        return self.fetchall()
    
    def buscarProductoPorId(self, id_producto):
        self.execute("""
            SELECT id_producto, nombre, descripcion, precio, stock
            FROM productos
            WHERE id_producto = %s;
        """, (id_producto,))
        return self.fetchone()
    
    def buscarProductoPornombre(self, nombre):
        self.execute("""
            SELECT id_producto, nombre, descripcion, precio, stock
            FROM productos
            WHERE nombre ILIKE %s;
        """, (nombre,))
        return self.fetchone()
    
    
    def agregarProducto(self, nombre, descripcion, precio, stock):
        self.execute("""
            INSERT INTO productos (nombre, descripcion, precio, stock)
            VALUES (%s, %s, %s, %s);
        """, (nombre, descripcion, precio, stock))

    def modificarProducto(self, id_producto, nombre, descripcion, precio, stock):
        self.execute("""
            UPDATE productos
            SET nombre = %s,
                descripcion = %s,
                precio = %s,
                stock = %s
            WHERE id_producto = %s;
        """, (nombre, descripcion, precio, stock, id_producto))

    def eliminarProducto(self, id_producto):
        self.execute("""
            DELETE FROM productos
            WHERE id_producto = %s;
        """, (id_producto,))
    
