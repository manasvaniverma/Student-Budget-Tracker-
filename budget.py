import json
import os


class BudgetTracker:

    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        self.monthly_budget = 0.0
        self.expenses = []

        self.load_data()

    # Sets budget per month
    def set_budget(self, amount):
        self.monthly_budget = amount
        self.save_data()

    # Adds an expense
    def add_expense(self, title, amount, category, date):
        expense = {
            "title": title,
            "amount": amount,
            "category": category,
            "date": date
        }

        self.expenses.append(expense)
        self.save_data()

    # Returns expenses
    def get_expenses(self):
        return self.expenses

    # Deletes an expense
    def delete_expense(self, index):

        if 0 <= index < len(self.expenses):
            deleted_expense = self.expenses.pop(index)
            self.save_data()
            return deleted_expense

        return None

    # Searches expenses for the keyword in the title, category or date
    def search_expenses(self, keyword):

        keyword = keyword.lower()
        results = []

        for expense in self.expenses:

            if (
                keyword in expense["title"].lower()
                or keyword in expense["category"].lower()
                or keyword in expense["date"].lower()
            ):
                results.append(expense)

        return results

    # Calculates how much was spent
    def get_total_expenses(self):

        total = 0.0

        for expense in self.expenses:
            total += expense["amount"]

        return total

    # Calculates remaining budget
    def get_remaining_budget(self):

        return self.monthly_budget - self.get_total_expenses()

    # Saves current state into file
    def save_data(self):

        data = {
            "monthly_budget": self.monthly_budget,
            "expenses": self.expenses
        }

        try:

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except IOError:

            print("Error: Could not save budget data.")sssss