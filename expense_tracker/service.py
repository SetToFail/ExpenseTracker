# expense_tracker/service.py
from .repository import ExpenseRepository

class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def add_expense(self, amount, category, description): # Changed
        self.repository.add_expense(amount, category, description) # Changed

    def get_all_expenses(self):
        return self.repository.get_all_expenses()