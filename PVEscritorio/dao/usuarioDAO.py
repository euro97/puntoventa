from dao.databseDAO import databseDAO


class UsuarioDAO(databseDAO):

    def login(self, correo, password):
        self.execute_query("""
            SELECT id_usuario, nombre, rol
            FROM usuarios
            WHERE correo = %s AND password = %s AND activo = TRUE;
        """, (correo, password))

        return self.fetchone()


    def consultarUsuarios(self):
        self.execute_query("""
            SELECT id_usuario, nombre, correo, rol, activo
            FROM usuarios
            ORDER BY id_usuario;
        """)
        return self.fetchall()


    def buscarUsuarioPorId(self, id_usuario):
        self.execute_query("""
            SELECT id_usuario, nombre, correo, rol, activo
            FROM usuarios
            WHERE id_usuario = %s;
        """, (id_usuario,))
        return self.fetchone()
    
    def buscarUsuarioPornombre(self, nombre):
        self.execute_query("""
            SELECT id_usuario, nombre, correo, rol, activo
            FROM usuarios
            WHERE nombre ILIKE %s;
        """, (nombre,))
        return self.fetchone()


    def agregarUsuario(self, nombre, correo, password, rol):
        self.execute_query("""
            INSERT INTO usuarios (nombre, correo, password, rol, activo)
            VALUES (%s, %s, %s, %s, TRUE);
        """, (nombre, correo, password, rol))


    def modificarUsuario(self, id_usuario, nombre, correo, rol, activo):
        self.execute_query("""
            UPDATE usuarios
            SET nombre = %s,
                correo = %s,
                rol = %s,
                activo = %s
            WHERE id_usuario = %s;
        """, (nombre, correo, rol, activo, id_usuario))


    def desactivarUsuario(self, id_usuario):
        self.execute_query("""
            UPDATE usuarios
            SET activo = FALSE
            WHERE id_usuario = %s;
        """, (id_usuario,))