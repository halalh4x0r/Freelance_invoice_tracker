import sqlite3

CONN = sqlite3.connect('db/database.db')
CURSOR = CONN.cursor()

def create_tables():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT
        )
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            client_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            amount REAL,
            paid INTEGER DEFAULT 0,
            issue_date TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
    ''')
    CONN.commit()
