from database import get_connection
from Models.adress import Adress

class Gruz:
    def __init__(self, id=None, base_price=0, duration=0, adress_id=None):
        self.id = id
        self.base_price = base_price
        self.duration = duration
        self.adress_id= adress_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
    
        if self.id is None:
            cursor.execute("""
            INSERT INTO Gruz (duration, base_price, adress_id)
            VALUES (?, ?, ?)
            """, (self.duration, self.base_price, self.adress_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE Gruz SET duration=?, base_price=?, adress_id=?
            WHERE id=?
            """, (self.duration, self.base_price, self.adress_id, self.id))
    
        conn.commit()
        conn.close()


    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Gruz WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Gruz")
        rows = cursor.fetchall()
        conn.close()
        print("\n Список грузов:")
        return [Gruz(*row) for row in rows]

    @staticmethod
    def get_by_id(Gruz_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Gruz WHERE id=?", (Gruz_id,))
        row = cursor.fetchone()
        conn.close()
        return Gruz(*row) if row else None

    @staticmethod
    def get_by_hotel(city):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Gruz WHERE city=?", (city,))
        rows = cursor.fetchall()
        conn.close()
        return [Gruz(*row) for row in rows]
    

    