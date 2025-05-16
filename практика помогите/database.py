import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def transportation_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Города
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS City (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        region TEXT NOT NULL
    )
    ''')
    
    # Адреса
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Adress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
    ''')
    
    # Клиенты
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        name TEXT,
        patronymic TEXT,
        address TEXT,
        phone TEXT
    )
    ''')
    
    # Грузы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Gruz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        duration INTEGER,
        base_price REAL,
        adress_id INTEGER,
        FOREIGN KEY (adress_id) REFERENCES adresses(id)
    )
    ''')
    
    # Продажи
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        gruz_id INTEGER,
        sale_date DATE,
        discount REAL DEFAULT 0,
        total_price REAL,
        departure_date DATE,
        FOREIGN KEY (client_id) REFERENCES clients(id),
        FOREIGN KEY (gruz_id) REFERENCES gruzs(id)
    )
    ''')
    
    conn.commit()
    conn.close()