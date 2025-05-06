# app.py

from flask import Flask, render_template, request, redirect, url_for
from expense_tracker.controller import ExpenseController
from expense_tracker.report_generator import ReportGeneratorFactory
import expense_tracker.repository

app = Flask(__name__)
app.config['DATABASE'] = 'expenses.sqlite'

controller = ExpenseController(app.config['DATABASE'])
report_factory = ReportGeneratorFactory()

@app.route('/')
def index():
    expenses = controller.get_all_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    description = request.form['description']
    controller.add_expense(amount, category, description)
    return redirect(url_for('index'))

@app.route('/report')
def report():
    report_type = request.args.get('type', 'daily')
    report = controller.get_report(report_type)
    print(report)
    return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)