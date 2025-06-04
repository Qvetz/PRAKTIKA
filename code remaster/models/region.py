from database.db_manager import get_connection

class Region:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO regions (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE regions SET name = ? WHERE id = ?", (self.name, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM regions WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_regions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM regions")
    rows = cursor.fetchall()
    conn.close()
    return [Region(id=row[0], name=row[1]) for row in rows]

def get_region_by_id(region_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM regions WHERE id = ?", (region_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Region(id=row[0], name=row[1])
    return None