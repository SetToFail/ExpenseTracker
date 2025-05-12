import pytest
from expense_tracker.service import ExpenseService
from expense_tracker.repository import ExpenseRepository

@pytest.fixture
def service():
    repo = ExpenseRepository(":memory:")
    yield ExpenseService(repo)
    repo.close()

def test_add_expense(service):
    service.add_expense(150.0, "Transport", "Taxi")
    expenses = service.get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0]['category'] == "Transport"