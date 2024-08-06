import json
from datetime import datetime

# Constants
DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

# Load data
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data
def save_data(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense(date, amount, description, category):
    expenses = load_data()
    expense = {
        "date": date,
        "amount": amount,
        "description": description,
        "category": category
    }
    expenses.append(expense)
    save_data(expenses)
    print("Expense added successfully!")

# Display expenses
def display_expenses():
    expenses = load_data()
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

# Display summary
def display_summary():
    expenses = load_data()
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")
    category_totals = {category: 0 for category in CATEGORIES}
    for expense in expenses:
        category_totals[expense['category']] += expense['amount']
    for category, total in category_totals.items():
        print(f"{category}: {total}")

# User interface
def user_interface():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                date = input("Enter the date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                amount = float(input("Enter the amount: "))
                description = input("Enter a brief description: ")
                print("Categories:", CATEGORIES)
                category = input("Enter the category: ")
                if category not in CATEGORIES:
                    raise ValueError("Invalid category")
                add_expense(date, amount, description, category)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

# Main function
if __name__ == "__main__":
    user_interface()
