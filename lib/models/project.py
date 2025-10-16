from lib.database import CURSOR, CONN

class Project:
    def __init__(self, name, description, client_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.client_id = client_id

    def save(self):
        CURSOR.execute("INSERT INTO projects (name, description, client_id) VALUES (?, ?, ?)",
                       (self.name, self.description, self.client_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM projects").fetchall()
        return [cls(id=row[0], name=row[1], description=row[2], client_id=row[3]) for row in rows]
