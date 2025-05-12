import sqlite3
from flask import g

class ExpenseRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db_path)
            db.row_factory = sqlite3.Row
        return db

    def create_table(self):
        cursor = self.get_db().cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.get_db().commit()

    def add_expense(self, amount, category, description):
        cursor = self.get_db().cursor()
        cursor.execute(
            "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (amount, category, description)
        )
        self.get_db().commit()

    def get_all_expenses(self):
        cursor = self.get_db().cursor()
        cursor.execute("""
            SELECT amount, category, description, date 
            FROM expenses 
            ORDER BY date DESC
        """)
        return cursor.fetchall()

    def get_daily_expenses(self):
        cursor = self.get_db().cursor()
        cursor.execute("""
            SELECT amount, category, description, date 
            FROM expenses 
            WHERE date(date) = date('now') 
            ORDER BY date DESC
        """)
        return cursor.fetchall()

    def get_weekly_expenses(self):
        cursor = self.get_db().cursor()
        cursor.execute("""
            SELECT amount, category, description, date 
            FROM expenses 
            WHERE date(date) >= date('now', 'weekday 0', '-7 days') 
            ORDER BY date DESC
        """)
        return cursor.fetchall()

    def get_monthly_expenses(self):
        cursor = self.get_db().cursor()
        cursor.execute("""
            SELECT amount, category, description, date 
            FROM expenses 
            WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') 
            ORDER BY date DESC
        """)
        return cursor.fetchall()