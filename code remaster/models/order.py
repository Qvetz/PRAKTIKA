from database.db_manager import get_connection
from datetime import datetime

class Order:
    def __init__(self, id=None, client_id=None, cargo_id=None, from_address_id=None, 
                 to_address_id=None, order_date=None, delivery_date=None, 
                 price=None, discount=0, status='new'):
        self.id = id
        self.client_id = client_id
        self.cargo_id = cargo_id
        self.from_address_id = from_address_id
        self.to_address_id = to_address_id
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.price = price
        self.discount = discount
        self.status = status
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Применяем скидку 5% для постоянных клиентов
        if self.discount == 0:
            from models.client import get_client_by_id
            client = get_client_by_id(self.client_id)
            if client and client.is_regular:
                self.discount = 5
                self.price = self.price * 0.95
        
        if self.id is None:
            cursor.execute("""INSERT INTO orders 
                            (client_id, cargo_id, from_address_id, to_address_id, 
                             order_date, delivery_date, price, discount, status) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                         (self.client_id, self.cargo_id, self.from_address_id, self.to_address_id,
                          self.order_date, self.delivery_date, self.price, self.discount, self.status))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE orders SET 
                            client_id = ?, cargo_id = ?, from_address_id = ?, to_address_id = ?,
                            order_date = ?, delivery_date = ?, price = ?, discount = ?, status = ?
                            WHERE id = ?""", 
                         (self.client_id, self.cargo_id, self.from_address_id, self.to_address_id,
                          self.order_date, self.delivery_date, self.price, self.discount, self.status, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, client_id, cargo_id, from_address_id, to_address_id,
                    order_date, delivery_date, price, discount, status FROM orders""")
    rows = cursor.fetchall()
    conn.close()
    return [Order(id=row[0], client_id=row[1], cargo_id=row[2], from_address_id=row[3], 
                 to_address_id=row[4], order_date=row[5], delivery_date=row[6], 
                 price=row[7], discount=row[8], status=row[9]) for row in rows]

def get_order_by_id(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, client_id, cargo_id, from_address_id, to_address_id,
                    order_date, delivery_date, price, discount, status FROM orders WHERE id = ?""", 
                  (order_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Order(id=row[0], client_id=row[1], cargo_id=row[2], from_address_id=row[3], 
                    to_address_id=row[4], order_date=row[5], delivery_date=row[6], 
                    price=row[7], discount=row[8], status=row[9])
    return None