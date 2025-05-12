import pytest
import tempfile
from expense_tracker.controller import ExpenseController

@pytest.fixture
def controller():
    with tempfile.NamedTemporaryFile() as tmp:
        yield ExpenseController(tmp.name)

def test_add_expense(controller):
    controller.add_expense(200.0, "Books", "Python book")
    expenses = controller.get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 200.0