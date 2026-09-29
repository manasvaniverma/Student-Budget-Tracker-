class BudgetAnalytics:

    def __init__(self, tracker):
        self.tracker = tracker

    # Calculation of average expense
    def average_expense(self):

        expenses = self.tracker.get_expenses()

        if len(expenses) == 0:
            return 0.0

        total = self.tracker.get_total_expenses()

        return total / len(expenses)

    # Get the highest expense
    def highest_expense(self):

        expenses = self.tracker.get_expenses()

        if len(expenses) == 0:
            return None

        highest = expenses[0]

        for expense in expenses:
            if expense["amount"] > highest["amount"]:
                highest = expense

        return highest

    # Calculation of spending per category
    def category_summary(self):

        expenses = self.tracker.get_expenses()

        summary = {}

        for expense in expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        return summary

    # Calculation of percentage of budget utilized
    def budget_percentage(self):

        budget = self.tracker.monthly_budget
        total = self.tracker.get_total_expenses()

        if budget <= 0:
            return 0.0

        return (total / budget) * 100

    # Return spending analysis report
    def get_analysis(self):

        total = self.tracker.get_total_expenses()
        average = self.average_expense()
        highest = self.highest_expense()
        categories = self.category_summary()
        percentage = self.budget_percentage()

        return {"total": total, "average": average, "highest": highest, "categories": categories, "percentage": percentage}