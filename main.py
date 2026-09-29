from budget import BudgetTracker
from analytics import BudgetAnalytics


def display_menu():
    print("\n" + "=" * 55)
    print("             STUDENT BUDGET TRACKER")
    print("=" * 55)
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View All Expenses")
    print("4. Delete Expense")
    print("5. View Budget Summary")
    print("6. View Spending Analytics")
    print("7. Search Expenses")
    print("8. Exit")
    print("=" * 55)


def set_budget(tracker):
    try:
        amount = float(input("Enter your monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than zero.")
            return

        tracker.set_budget(amount)
        print(f"Monthly budget successfully set to ₹{amount:.2f}")

    except ValueError:
        print("Please enter a valid numeric amount.")


def add_expense(tracker):
    print("\n--- ADD EXPENSE ---")

    title = input("Enter expense title: ").strip()

    if not title:
        print("Expense title cannot be empty.")
        return

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Expense amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    category = input(
        "Enter category (Food/Travel/Study/Shopping/Other): "
    ).strip()

    if not category:
        print("Category cannot be empty.")
        return

    date = input("Enter date (DD-MM-YYYY): ").strip()

    if not date:
        print("Date cannot be empty.")
        return

    tracker.add_expense(title, amount, category, date)

    print("Expense added successfully!")


def view_expenses(tracker):
    expenses = tracker.get_expenses()

    print("\n--- ALL EXPENSES ---")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("-")