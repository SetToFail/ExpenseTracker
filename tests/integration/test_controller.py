import pytest
import tempfile
from expense_tracker.controller import ExpenseController

@pytest.fixture
def controller():
    with tempfile.NamedTemporaryFile() as tmp:
        yield ExpenseController(tmp.name)

def test_add_expense(controller):
    # Проверяем что метод не возвращает строку
    result = controller.add_expense(200.0, "Books", "Python book")
    assert result is None  # Метод не должен ничего возвращать
    
    expenses = controller.get_all_expenses()
    assert isinstance(expenses, list)  # Должен возвращаться список