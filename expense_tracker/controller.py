from .service import ExpenseService
from .report_generator import ReportGeneratorFactory

class ExpenseController:
    def __init__(self, db_path):
        self.service = ExpenseService(db_path)
        self.report_generator_factory = ReportGeneratorFactory()

    def add_expense(self, amount, category, description):
        self.service.add_expense(amount, category, description)

    def get_all_expenses(self):
        return self.service.get_all_expenses()

    def get_report(self, report_type):
        generator = self.report_generator_factory.get_report_generator(report_type)
        if not generator:
            return "Invalid report type"
        expenses = self.service.get_all_expenses()
        return generator.generate_report(expenses)