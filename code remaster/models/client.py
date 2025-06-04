from database.db_manager import get_connection

class Client:
    def __init__(self, id=None, surname=None, name=None, patronymic=None, phone=None, is_regular=False):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone
        self.is_regular = is_regular
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO clients (surname, name, patronymic, phone, is_regular) 
                            VALUES (?, ?, ?, ?, ?)""", 
                         (self.surname, self.name, self.patronymic, self.phone, self.is_regular))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE clients SET surname = ?, name = ?, patronymic = ?, 
                            phone = ?, is_regular = ? WHERE id = ?""", 
                         (self.surname, self.name, self.patronymic, self.phone, self.is_regular, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, surname, name, patronymic, phone, is_regular FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return [Client(id=row[0], surname=row[1], name=row[2], patronymic=row[3], phone=row[4], is_regular=row[5]) 
            for row in rows]

def get_client_by_id(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, surname, name, patronymic, phone, is_regular 
                    FROM clients WHERE id = ?""", (client_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Client(id=row[0], surname=row[1], name=row[2], patronymic=row[3], phone=row[4], is_regular=row[5])
    return None