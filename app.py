from flask import Flask, jsonify
from expense_tracker.controller import ExpenseController

app = Flask(__name__)
app.config['DATABASE'] = 'expenses.sqlite'

def get_controller():
    # Реализация получения контроллера
    return ExpenseController(app.config['DATABASE'])

@app.route('/')
def index():
    controller = get_controller()
    expenses = controller.get_all_expenses()
    return jsonify({'expenses': expenses})  # Всегда возвращаем JSON