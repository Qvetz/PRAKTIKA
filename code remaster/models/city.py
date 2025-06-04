from database.db_manager import get_connection

class City:
    def __init__(self, id=None, name=None, region_id=None):
        self.id = id
        self.name = name
        self.region_id = region_id
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO cities (name, region_id) VALUES (?, ?)", 
                         (self.name, self.region_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE cities SET name = ?, region_id = ? WHERE id = ?", 
                         (self.name, self.region_id, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cities WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_cities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, region_id FROM cities")
    rows = cursor.fetchall()
    conn.close()
    return [City(id=row[0], name=row[1], region_id=row[2]) for row in rows]

def get_city_by_id(city_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, region_id FROM cities WHERE id = ?", (city_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return City(id=row[0], name=row[1], region_id=row[2])
    return None