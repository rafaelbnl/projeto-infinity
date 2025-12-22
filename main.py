from netvalue import monthly_income_calculator

december = monthly_income_calculator()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Incomes menu")
        print("2. Variable Expenses menu")
        print("3. Fixed Expenses menu")
        print("4. Monthly Summary")
        print("0. Exit")

        choice = input("Select an option: ")
        match choice:
            case "1":
                while True:
                    try:
                        print("\nIncomes Menu:")
                        print("1. Add Income Source")
                        print("2. Read Income Sources")
                        print("3. Update Income Source")
                        print("4. Delete Income Source")
                        print("5. Back to Main Menu")

                        income_choice = input("Select an option: ")
                        match income_choice:
                            case "1":
                                december.add_income_source()
                            case "2":
                                december.read_incomes()
                            case "3":
                                december.update_income_source()
                            case "4":
                                december.delete_income_source()
                            case "5":
                                break
                            case _:
                                print("Invalid option. Please try again.")
                    except Exception as e:
                                    print(f"An error occurred: {e}")    
            case "2":
                while True:
                    try:
                        print("\nVariable Expenses Menu:")
                        print("1. Add Variable Expense")
                        print("2. Read Variable Expenses")
                        print("3. Update Variable Expense")
                        print("4. Delete Variable Expense")
                        print("5. Back to Main Menu")

                        expense_choice = input("Select an option: ")
                        match expense_choice:
                            case "1":
                                december.add_variable_expense()
                            case "2":
                                december.read_variable_expenses()
                            case "3":
                                december.update_variable_expense()
                            case "4":
                                december.delete_variable_expense()
                            case "5":
                                break
                            case _:
                                print("Invalid option. Please try again.")
                    except Exception as e:
                                    print(f"An error occurred: {e}")
            case "3":
                  while True:
                    try:
                        print("\nFixed Expenses Menu:")
                        print("1. Add Fixed Expense")
                        print("2. Read Fixed Expenses")
                        print("3. Update Fixed Expense")
                        print("4. Delete Fixed Expense")
                        print("5. Back to Main Menu")

                        fixed_choice = input("Select an option: ")
                        match fixed_choice:
                            case "1":
                                december.add_fixed_expense()
                            case "2":
                                december.read_fixed_expenses()
                            case "3":
                                december.update_fixed_expense()
                            case "4":
                                december.delete_fixed_expense()
                            case "5":
                                break
                            case _:
                                print("Invalid option. Please try again.")
                    except Exception as e:
                                    print(f"An error occurred: {e}")
            case "4":
                december.monthly_summary()
            case "0":
                print("Exiting the program. Goodbye!")
                return
            case _:
                print("Invalid option. Please try again.")

main_menu()