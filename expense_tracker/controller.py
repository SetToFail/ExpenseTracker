from expense_tracker.service import ExpenseService
from expense_tracker.repository import ExpenseRepository
from expense_tracker.report_generator import ReportGeneratorFactory

class ExpenseController:
    def __init__(self, db_path):
        self.service = ExpenseService(ExpenseRepository(db_path))
        self.report_generator_factory = ReportGeneratorFactory()

    def add_expense(self, amount, category, description):
        """Добавляет расход и ничего не возвращает"""
        self.service.add_expense(amount, category, description)  # Не возвращаем строку

    def get_all_expenses(self):
        """Возвращает список расходов"""
        return self.service.get_all_expenses()  # Возвращаем список, а не строку

    def get_report(self, report_type):
        generator = self.report_generator_factory.get_report_generator(report_type)
        if not generator:
            return None  # Вместо строки возвращаем None при ошибке
        
        expenses = self.service.get_all_expenses()
        return generator.generate_report(expenses)