from dao.databseDAO import databseDAO

class ProductoDAO(databseDAO):

    def consultarProductos(self):
        self.execute_query("""
            SELECT id, nombre, marca, precio, cantidad, tamano
            FROM productos
            ORDER BY id;
        """)
        return self.fetchall()
    
    def buscarProductoPorId(self, id_producto):
        self.execute_query("""
            SELECT id, nombre, marca, precio, cantidad, tamano
            FROM productos
            WHERE id = %s;
        """, (id_producto,))
        return self.fetchone()
    
    def buscarProductoPornombre(self, nombre):
        self.execute_query("""
            SELECT id, nombre, marca, precio, cantidad, tamano
            FROM productos
            WHERE nombre ILIKE %s;
        """, (nombre,))
        return self.fetchone()
    
    
    def agregarProducto(self, nombre, marca, precio, cantidad, tamano):
        self.execute_query("""
            INSERT INTO productos (nombre, marca, precio, cantidad, tamano)
            VALUES (%s, %s, %s, %s, %s);
        """, (nombre, marca, precio, cantidad, tamano))

    def modificarProducto(self, id_producto, nombre, marca, precio, cantidad, tamano):
        self.execute_query("""
            UPDATE productos
            SET nombre = %s,
                marca = %s,
                precio = %s,
                cantidad = %s,
                tamano = %s
            WHERE id = %s;
        """, (nombre, marca, precio, cantidad, tamano, id_producto))

    def eliminarProducto(self, id_producto):
        self.execute_query("""
            DELETE FROM productos
            WHERE id = %s;
        """, (id_producto,))
    
