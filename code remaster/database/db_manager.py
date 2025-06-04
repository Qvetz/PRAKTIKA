import sqlite3

DB_NAME = "initialize_db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица регионов
    cursor.execute('''CREATE TABLE IF NOT EXISTS regions(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL UNIQUE)''')
    
    # Таблица городов
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   region_id INTEGER NOT NULL,
                   FOREIGN KEY (region_id) REFERENCES regions(id),
                   UNIQUE(name, region_id))''')
    
    # Таблица адресов
    cursor.execute('''CREATE TABLE IF NOT EXISTS addresses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   city_id INTEGER NOT NULL,
                   street TEXT NOT NULL,
                   building TEXT NOT NULL,
                   apartment TEXT,
                   FOREIGN KEY (city_id) REFERENCES cities(id))''')
    
    # Таблица клиентов
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   surname TEXT NOT NULL,
                   name TEXT NOT NULL,
                   patronymic TEXT,
                   phone TEXT NOT NULL UNIQUE,
                   is_regular BOOLEAN NOT NULL DEFAULT 0)''')
    
    # Таблица грузов
    cursor.execute('''CREATE TABLE IF NOT EXISTS cargo(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT NOT NULL,
                   weight REAL NOT NULL CHECK(weight > 0),
                   volume REAL NOT NULL CHECK(volume > 0),
                   special_conditions TEXT)''')
    
    # Таблица заказов
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   cargo_id INTEGER NOT NULL,
                   from_address_id INTEGER NOT NULL,
                   to_address_id INTEGER NOT NULL,
                   order_date DATE NOT NULL,
                   delivery_date DATE NOT NULL,
                   price REAL NOT NULL CHECK(price >= 0),
                   discount REAL DEFAULT 0,
                   status TEXT NOT NULL DEFAULT 'new',
                   FOREIGN KEY (client_id) REFERENCES clients(id),
                   FOREIGN KEY (cargo_id) REFERENCES cargo(id),
                   FOREIGN KEY (from_address_id) REFERENCES addresses(id),
                   FOREIGN KEY (to_address_id) REFERENCES addresses(id))''')
    
    conn.commit()
    conn.close()