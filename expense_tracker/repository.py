import sqlite3

class ExpenseRepository:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def add_expense(self, amount, category, description):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
                (amount, category, description)
            )

    def get_all_expenses(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT amount, category, description, date 
                FROM expenses 
                ORDER BY date DESC
            """)
            return cursor.fetchall()

    def close(self):
        self.conn.close()