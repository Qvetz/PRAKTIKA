from database import get_connection

class City:
    def __init__(self, id=None, name=None, region=None):
        self.id = id
        self.name = name
        self.region = region

        

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

            
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO City (name, region)
            VALUES (?, ?)
            """, (self.name, self.region))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE City SET name=?, region=?
            WHERE id=?
            """, (self.name, self.region, self.id))
        
        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM City WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM City")
        rows = cursor.fetchall()
        conn.close()
        print("\n Список городов:")
        return [City(*row) for row in rows]

    @staticmethod
    def get_by_id(city_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM City WHERE id=?", (city_id,))
        row = cursor.fetchone()
        conn.close()
        return City(*row) if row else None