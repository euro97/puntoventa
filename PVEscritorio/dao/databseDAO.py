import db

class databseDAO:

    def __enter__(self):
        self.conn = db.connect()
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        db.close(self.conn)

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
    
    def fechone(self):
        return self.cursor.fetchone()
    

    def fechall(self):
        return self.cursor.fetchall()
    
    
