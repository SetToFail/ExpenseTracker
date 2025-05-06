# expense_tracker/model.py
from datetime import datetime

class Expense:
  def __init__(self, amount: float, category: str, description: str = "", date: datetime = None):
    self.amount = amount
    self.category = category
    self.description = description
    self.date = date if date else datetime.now()

  def __repr__(self): # repr для удобной отладки
    return f"Expense(amount={self.amount}, category='{self.category}', description='{self.description}', date='{self.date}')"