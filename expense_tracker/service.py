from .repository import ExpenseRepository

class ExpenseService:
    def __init__(self, repository: ExpenseRepository):  # Принимаем готовый репозиторий
        self.repository = repository

    def add_expense(self, amount, category, description):
        self.repository.add_expense(amount, category, description)

    def get_all_expenses(self):
        return self.repository.get_all_expenses()