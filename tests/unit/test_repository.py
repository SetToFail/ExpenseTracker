import pytest
from expense_tracker.repository import ExpenseRepository

@pytest.fixture
def repo():
    repo = ExpenseRepository(":memory:")
    yield repo
    repo.close()

def test_add_expense(repo):
    repo.add_expense(100.0, "Food", "Lunch")
    expenses = repo.get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 100.0
    assert expenses[0]['category'] == "Food"