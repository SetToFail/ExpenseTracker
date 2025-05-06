# expense_tracker/controller.py

from .service import ExpenseService
from .repository import ExpenseRepository
from .report_generator import ReportGeneratorFactory
from .visualization import VisualizationService

class ExpenseController:
    def __init__(self, db_path):
        self.service = ExpenseService(ExpenseRepository(db_path))
        self.report_generator_factory = ReportGeneratorFactory()
        self.db_path = db_path

    def add_expense(self, amount, category, description):
        self.service.add_expense(amount, category, description)

    def get_all_expenses(self):
        return self.service.get_all_expenses()

    def get_report(self, report_type):
        generator = self.report_generator_factory.get_report_generator(report_type) # Исправлена опечатка
        if generator:
            expenses = self.service.get_all_expenses()
            report = generator.generate_report(expenses)
            return report
        else:
            return "Invalid report type"