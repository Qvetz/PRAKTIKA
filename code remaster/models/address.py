from database.db_manager import get_connection

class Address:
    def __init__(self, id=None, city_id=None, street=None, building=None, apartment=None):
        self.id = id
        self.city_id = city_id
        self.street = street
        self.building = building
        self.apartment = apartment
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO addresses (city_id, street, building, apartment) 
                            VALUES (?, ?, ?, ?)""", 
                          (self.city_id, self.street, self.building, self.apartment))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE addresses SET city_id = ?, street = ?, 
                            building = ?, apartment = ? WHERE id = ?""", 
                          (self.city_id, self.street, self.building, self.apartment, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM addresses WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_addresses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, city_id, street, building, apartment FROM addresses")
    rows = cursor.fetchall()
    conn.close()
    return [Address(id=row[0], city_id=row[1], street=row[2], building=row[3], apartment=row[4]) 
            for row in rows]

def get_address_by_id(address_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, city_id, street, building, apartment FROM addresses WHERE id = ?", 
                  (address_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Address(id=row[0], city_id=row[1], street=row[2], building=row[3], apartment=row[4])
    return None