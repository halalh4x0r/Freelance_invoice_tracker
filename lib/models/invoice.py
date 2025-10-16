from lib.database import CURSOR, CONN

class Invoice:
    def __init__(self, project_id, amount, issue_date, paid=0, id=None):
        self.id = id
        self.project_id = project_id
        self.amount = amount
        self.issue_date = issue_date
        self.paid = paid

    def save(self):
        CURSOR.execute(
            "INSERT INTO invoices (project_id, amount, issue_date, paid) VALUES (?, ?, ?, ?)",
            (self.project_id, self.amount, self.issue_date, self.paid)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_unpaid(cls):
        rows = CURSOR.execute("SELECT * FROM invoices WHERE paid = 0").fetchall()
        return [cls(id=row[0], project_id=row[1], amount=row[2], paid=row[3], issue_date=row[4]) for row in rows]

    @classmethod
    def mark_paid(cls, invoice_id):
        CURSOR.execute("UPDATE invoices SET paid = 1 WHERE id = ?", (invoice_id,))
        CONN.commit()
