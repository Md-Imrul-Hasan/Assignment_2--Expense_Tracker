import os


# expense_tracker.py


# The project will have these parts:

# 1. Create file setup
# 2. `add_expense()`
# 3. `view_expenses()`
# 4. `search_expense()`
# 5. `update_expense()
# 6. `delete_expense()`
# 7. `expense_summary()
# 8. `main()` menu


# Step 1: File Setup

# Create the Python file and write:


FILE_NAME = "expenses.txt"


# Step 2: Add Expense Function


def add_expense():
    try:
        expense_id = input("Expense ID: ")
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        description = input("Description: ")

        amount = float(input("Amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        with open(FILE_NAME, "a") as file:
            file.write(
                f"{expense_id},{date},{category},{description},{amount}\n"
            )

        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount! Please enter a valid number.")


### Test:


# Step 3: View All Expenses


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:

            expenses = file.readlines()

            if not expenses:
                print("No expenses available.")
                return

            for expense in expenses:

                data = expense.strip().split(",")

                print("------------------------------------")
                print("Expense ID :", data[0])
                print("Date       :", data[1])
                print("Category   :", data[2])
                print("Description:", data[3])
                print("Amount     :", data[4])
                print("------------------------------------")

    except FileNotFoundError:
        print("No expense records found.")


# Step 4: Search Expense


def search_expense():

    try:
        search_id = input("Enter Expense ID: ")

        with open(FILE_NAME, "r") as file:

            found = False

            for expense in file:

                data = expense.strip().split(",")

                if data[0] == search_id:

                    print("Expense Found")
                    print("Expense ID :", data[0])
                    print("Date       :", data[1])
                    print("Category   :", data[2])
                    print("Description:", data[3])
                    print("Amount     :", data[4])

                    found = True
                    break

            if not found:
                print("Expense not found.")

    except FileNotFoundError:
        print("No expense records found.")
        
        
# Step 5: Update Expense


def update_expense():

    try:

        expense_id = input("Enter Expense ID to update: ")

        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        updated = []
        found = False


        for expense in expenses:

            data = expense.strip().split(",")

            if data[0] == expense_id:

                date = input("Date: ")
                category = input("Category: ")
                description = input("Description: ")

                try:
                    amount = float(input("Amount: "))

                    if amount < 0:
                        print("Amount cannot be negative.")
                        return

                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    return


                updated.append(
                    f"{expense_id},{date},{category},{description},{amount}\n"
                )

                found = True

            else:
                updated.append(expense)


        if found:

            with open(FILE_NAME,"w") as file:
                file.writelines(updated)

            print("Expense updated successfully.")

        else:
            print("Expense not found.")


    except FileNotFoundError:
        print("No expense records found.")




# Step 6: Delete Expense

def delete_expense():

    try:

        expense_id = input("Enter Expense ID to delete: ")

        with open(FILE_NAME,"r") as file:
            expenses = file.readlines()


        remaining = []
        found = False


        for expense in expenses:

            data = expense.strip().split(",")

            if data[0] == expense_id:
                found = True

            else:
                remaining.append(expense)


        if found:

            with open(FILE_NAME,"w") as file:
                file.writelines(remaining)

            print("Expense deleted successfully.")

        else:
            print("Expense not found.")


    except FileNotFoundError:
        print("No expense records found.")


# Step 7: Expense Summary

def expense_summary():

    try:

        with open(FILE_NAME,"r") as file:

            expenses = file.readlines()


            if not expenses:
                print("No expenses available.")
                return


            amounts=[]


            for expense in expenses:

                data = expense.strip().split(",")

                amounts.append(float(data[4]))


            total = len(amounts)
            spending = sum(amounts)
            average = spending / total


            print("========= Expense Summary =========")
            print("Total Expenses :", total)
            print("Total Spending :", spending, "BDT")
            print("Average Expense :", round(average,2), "BDT")
            print("Highest Expense :", max(amounts), "BDT")
            print("Lowest Expense :", min(amounts), "BDT")


    except FileNotFoundError:
        print("No expense records found.")

# Step 8: Main Menu

def main():

    while True:

        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Expense Summary")
        print("7. Exit")


        choice = input("Choose an option: ")


        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            update_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            expense_summary()

        elif choice == "7":
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice! Please select a valid option.")


main()
