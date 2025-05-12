from flask import Flask, render_template, request, redirect, url_for, g
from expense_tracker.controller import ExpenseController
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = 'expenses.sqlite'

# Инициализация базы данных
def init_db():
    with app.app_context():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(app.config['DATABASE'])
            db.row_factory = sqlite3.Row
        
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        db.commit()

# Создаём базу при первом запуске
if not os.path.exists(app.config['DATABASE']):
    init_db()

controller = ExpenseController(app.config['DATABASE'])

@app.route('/')
def index():
    expenses = controller.get_all_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    try:
        amount = float(request.form['amount'])
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
            
        category = request.form['category'].strip()
        if not category:
            raise ValueError("Категория не может быть пустой")
            
        description = request.form['description'].strip()
        controller.add_expense(amount, category, description)
        return redirect(url_for('index'))
    except ValueError as e:
        return str(e), 400

@app.route('/report')
def report():
    report_type = request.args.get('type', 'daily')
    report = controller.get_report(report_type)
    return render_template('report.html', report=report)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)