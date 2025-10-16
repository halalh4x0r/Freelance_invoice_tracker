from lib.database import CURSOR, CONN

class Client:
    def __init__(self, name, email, phone, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        CURSOR.execute("INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)",
                       (self.name, self.email, self.phone))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM clients").fetchall()
        return [cls(id=row[0], name=row[1], email=row[2], phone=row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute("SELECT * FROM clients WHERE id = ?", (id,)).fetchone()
        return cls(id=row[0], name=row[1], email=row[2], phone=row[3]) if row else None
