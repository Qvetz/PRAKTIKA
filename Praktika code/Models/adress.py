from database import get_connection
from Models.city import City
import sqlite3


class Adress:
    def __init__(self, id=None, name=None, address=None, city_id=None):
        self.id = id
        self.name = name
        self.address = address
        self.city_id = city_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO Adress (address, city_id)
            VALUES (?, ?)
            """, (self.address, self.city_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE Adress SET address=?, city=?
            WHERE id=?
            """, (self.address, self.city_id, self.id))
        
        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Adress WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Adress")
        rows = cursor.fetchall()
        conn.close()
        print("\n Адреса доставки:")
        return [Adress(*row) for row in rows]

    @staticmethod
    def get_by_id(Adress_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Adress WHERE id=?", (Adress_id,))
        row = cursor.fetchone()
        conn.close()
        return Adress(*row) if row else None

    @staticmethod
    def get_by_country(city):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Adress WHERE city=?", (city,))
        rows = cursor.fetchall()
        conn.close()
        return [Adress(*row) for row in rows]
    
    