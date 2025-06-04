from database.db_manager import get_connection

class Cargo:
    def __init__(self, id=None, description=None, weight=None, volume=None, special_conditions=None):
        self.id = id
        self.description = description
        self.weight = weight
        self.volume = volume
        self.special_conditions = special_conditions
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO cargo (description, weight, volume, special_conditions) 
                            VALUES (?, ?, ?, ?)""", 
                         (self.description, self.weight, self.volume, self.special_conditions))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE cargo SET description = ?, weight = ?, volume = ?, 
                            special_conditions = ? WHERE id = ?""", 
                         (self.description, self.weight, self.volume, self.special_conditions, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cargo WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_cargo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, weight, volume, special_conditions FROM cargo")
    rows = cursor.fetchall()
    conn.close()
    return [Cargo(id=row[0], description=row[1], weight=row[2], volume=row[3], special_conditions=row[4]) 
            for row in rows]

def get_cargo_by_id(cargo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, description, weight, volume, special_conditions 
                    FROM cargo WHERE id = ?""", (cargo_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Cargo(id=row[0], description=row[1], weight=row[2], volume=row[3], special_conditions=row[4])
    return None