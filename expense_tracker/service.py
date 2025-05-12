from .repository import ExpenseRepository

class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def add_expense(self, amount, category, description):
        self.repository.add_expense(amount, category, description)

    def get_all_expenses(self):
        return self.repository.get_all_expenses()

    def get_daily_expenses(self):
        return self.repository.get_daily_expenses()

    def get_weekly_expenses(self):
        return self.repository.get_weekly_expenses()

    def get_monthly_expenses(self):
        return self.repository.get_monthly_expenses()