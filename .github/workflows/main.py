class Expense:
    def __init__(self, description, amt, date):
        self.description = description
        self.amt = amt
        self.date = date
    
    def __str__(self):
        return f"{self.date}    {self.description}    {self.amt}"
    def update_amt(self, new_amt):
        self.amt = new_amt
    def update_description(self, new_description):
        self.description = new_description
    def update_date(self, new_date):
        self.date = new_date
class ExpenseList:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense):
        self.expenses.append(expense)
    def remove_expense(self, expense):
        self.expenses.remove(expense)
    def view_expenses(self):
        print("ID      Date    Description    Amount")
        for i in range(len(self.expenses)):
            print(f'ID: {i} {self.expenses[i]}')


if __name__ == "__main__":
    expense_list = ExpenseList()
    expense_list.add_expense(Expense("Rent", 1000, "2022-01-01"))
    expense_list.add_expense(Expense("Groceries", 50, "2022-01-02"))
    expense_list.view_expenses()