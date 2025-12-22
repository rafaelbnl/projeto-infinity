class monthly_income_calculator:
    def __init__(self):
        self.total_incomes_value = 0
        self.total_incomes_list = []
        self.total_variable_expenses = 0
        self.total_variable_expenses_list = []
        self.total_fixed_expenses = 0
        self.total_fixed_expenses_list = []

    def add_income_source(self):
        income_source = input("Enter the income source: ")
        income_value = float(input("Enter the income value: "))
        self.total_incomes_list.append((income_source, income_value))
        self.total_incomes_value += income_value
        print(f"Income source '{income_source}' with value {income_value} added.")

    def read_incomes(self):
        if not self.total_incomes_list:
            print("No income sources added yet.")
        else:
            print("Income Sources:")
            for source, value in self.total_incomes_list:
                print(f"- {source}: {value}")
            print(f"Total Income: {self.total_incomes_value}")

    def update_income_source(self):
        income_source = input("Enter the income source to update: ")
        for i, (source, value) in enumerate(self.total_incomes_list):
            if source == income_source:
                new_value = float(input(f"Enter the new value for '{income_source}': "))
                self.total_incomes_value += new_value - value
                self.total_incomes_list[i] = (income_source, new_value)
                print(f"Income source '{income_source}' updated to {new_value}.")
                return
        print(f"Income source '{income_source}' not found.")

    def delete_income_source(self):
        income_source = input("Enter the income source to delete: ")
        for i, (source, value) in enumerate(self.total_incomes_list):
            if source == income_source:
                self.total_incomes_value -= value
                del self.total_incomes_list[i]
                print(f"Income source '{income_source}' deleted.")
                return
        print(f"Income source '{income_source}' not found.")

    def add_variable_expense(self):
        expense_name = input("Enter the variable expense name: ")
        expense_value = float(input("Enter the variable expense value: "))
        self.total_variable_expenses_list.append((expense_name, expense_value))
        self.total_variable_expenses += expense_value
        print(f"Variable expense '{expense_name}' with value {expense_value} added.")

    def read_variable_expenses(self):
        if not self.total_variable_expenses_list:
            print("No variable expenses added yet.")
        else:
            print("Variable Expenses:")
            for name, value in self.total_variable_expenses_list:
                print(f"- {name}: {value}")
            print(f"Total Variable Expenses: {self.total_variable_expenses}")

    def update_variable_expense(self):
        expense_name = input("Enter the variable expense name to update: ")
        for i, (name, value) in enumerate(self.total_variable_expenses_list):
            if name == expense_name:
                new_value = float(input(f"Enter the new value for '{expense_name}': "))
                self.total_variable_expenses += new_value - value
                self.total_variable_expenses_list[i] = (expense_name, new_value)
                print(f"Variable expense '{expense_name}' updated to {new_value}.")
                return
        print(f"Variable expense '{expense_name}' not found.")

    def delete_variable_expense(self):  
        expense_name = input("Enter the variable expense name to delete: ")
        for i, (name, value) in enumerate(self.total_variable_expenses_list):
            if name == expense_name:
                self.total_variable_expenses -= value
                del self.total_variable_expenses_list[i]
                print(f"Variable expense '{expense_name}' deleted.")
                return
        print(f"Variable expense '{expense_name}' not found.")

    def add_fixed_expense(self):
        expense_name = input("Enter the fixed expense name: ")
        expense_value = float(input("Enter the fixed expense value: "))
        self.total_fixed_expenses_list.append((expense_name, expense_value))
        self.total_fixed_expenses += expense_value
        print(f"Fixed expense '{expense_name}' with value {expense_value} added.")

    def read_fixed_expenses(self):
        if not self.total_fixed_expenses_list:
            print("No fixed expenses added yet.")
        else:
            print("Fixed Expenses:")
            for name, value in self.total_fixed_expenses_list:
                print(f"- {name}: {value}")
            print(f"Total Fixed Expenses: {self.total_fixed_expenses}")

    def update_fixed_expense(self): 
        expense_name = input("Enter the fixed expense name to update: ")
        for i, (name, value) in enumerate(self.total_fixed_expenses_list):
            if name == expense_name:
                new_value = float(input(f"Enter the new value for '{expense_name}': "))
                self.total_fixed_expenses += new_value - value
                self.total_fixed_expenses_list[i] = (expense_name, new_value)
                print(f"Fixed expense '{expense_name}' updated to {new_value}.")
                return
        print(f"Fixed expense '{expense_name}' not found.")

    def delete_fixed_expense(self): 
        expense_name = input("Enter the fixed expense name to delete: ")
        for i, (name, value) in enumerate(self.total_fixed_expenses_list):
            if name == expense_name:
                self.total_fixed_expenses -= value
                del self.total_fixed_expenses_list[i]
                print(f"Fixed expense '{expense_name}' deleted.")
                return
        print(f"Fixed expense '{expense_name}' not found.")

    def calculate_net_income(self):
        net_income = self.total_incomes_value - (self.total_variable_expenses + self.total_fixed_expenses)
        print(f"Net Income: {net_income}")
        return net_income