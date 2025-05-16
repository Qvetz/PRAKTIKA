from database import get_connection
from Models.client import Client
from Models.city import City
from Models.adress import Adress
from Models.gruz import Gruz
from datetime import date

class Sale:
    def __init__(self, id=None, client_id=None, Gruz_id=None, sale_date=None, 
                 discount=0, total_price=0, departure_date=None):
        self.id = id
        self.client_id = client_id
        self.Gruz_id = Gruz_id
        self.sale_date = sale_date or date.today().strftime("%Y-%m-%d")
        self.discount = discount
        self.total_price = total_price
        self.departure_date = departure_date

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Рассчитываем цену с учетом скидок
        Gruz = Gruz.get_by_id(self.Gruz_id)
        City = City.get_by_id(Adress.get_by_id(Gruz.Adress_id).City_id)
        
        # Базовая цена
        base_price = Gruz.base_price
        
        # Применяем скидки (суммируются)
        total_discount = self.discount
        
        # Итоговая цена
        self.total_price = base_price * (1 - total_discount/100)

        if self.id is None:
            cursor.execute("""
            INSERT INTO sales (client_id, Gruz_id, sale_date, discount, total_price, departure_date)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (self.client_id, self.Gruz_id, self.sale_date, self.discount, 
                  self.total_price, self.departure_date))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE sales SET client_id=?, Gruz_id=?, sale_date=?, 
                            discount=?, total_price=?, departure_date=?
            WHERE id=?
            """, (self.client_id, self.Gruz_id, self.sale_date, self.discount, 
                  self.total_price, self.departure_date, self.id))
        
        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sales WHERE id=?", (self.id,))
            conn.commit()
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()
        conn.close()
        print("\n Список заказов:")
        return [Sale(*row) for row in rows]

    @staticmethod
    def get_by_id(sale_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales WHERE id=?", (sale_id,))
        row = cursor.fetchone()
        conn.close()
        return Sale(*row) if row else None

    @staticmethod
    def get_by_client(client_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales WHERE client_id=?", (client_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Sale(*row) for row in rows]