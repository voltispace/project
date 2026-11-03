import json
import os

FILE_NAME = "expenses.json"
CATEGORIES = ["Food", "Transport", "Utility", "Donations", "Miscellaneous"]

# ================= DATA PERSISTENCE =================

def load_expenses():
    """Loads expenses from file, returning an empty list if not found or corrupted."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    """Saves the expenses list to disk."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

# ================= HELPER PROMPTS =================

def select_category():
    """Displays categories and returns the chosen category name."""
    print("\nSelect Category:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

    try:
        choice = int(input("Choose category number: "))
        if 1 <= choice <= len(CATEGORIES):
            return CATEGORIES[choice - 1]
    except ValueError:
        pass
    
    print("Defaulted to 'Miscellaneous'.")
    return "Miscellaneous"

def get_positive_amount():
    """Repeatedly prompts until a valid positive float amount is entered."""
    while True:
        try:
            amount = float(input("Enter amount (N): "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# ================= FEATURE FUNCTIONS =================

def add_expense(expenses):
    """Handles category selection, description, amount input, and saving."""
    category = select_category()
    description = input("Enter description/product name: ").strip()
    amount = get_positive_amount()

    new_item = {
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(new_item)
    save_expenses(expenses)
    print(f"Added: N{amount:.2f} for '{description}' under [{category}]")

def view_expenses(expenses):
    """Prints a numbered list of all recorded expenses."""
    print("\n--- ALL EXPENSES ---")
    if not expenses:
        print("No expenses recorded yet.")
        return False

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. [{exp['category']}] {exp['description']} - N{exp['amount']:.2f}")
    return True

def view_summary(expenses):
    """Calculates and displays total spending and category breakdown."""
    print("\n--- SPENDING SUMMARY ---")
    if not expenses:
        print("No expenses to calculate.")
        return

    # 1. Total
    total_spent = sum(item["amount"] for item in expenses)
    print(f"Total Spending: \033[32mN{total_spent:.2f}\033[0m")

    # 2. Breakdown by Category
    category_totals = {}
    for item in expenses:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

    print("\nSpending by Category:")
    for cat, amount in category_totals.items():
        print(f"  - {cat}: N{amount:.2f}")

def delete_expense(expenses):
    """Lists current expenses and deletes one selected by index."""
    print("\n--- DELETE EXPENSE ---")
    has_items = view_expenses(expenses)
    if not has_items:
        return

    try:
        delete_index = int(input("\nEnter the number of the expense to delete: "))
        if 1 <= delete_index <= len(expenses):
            removed = expenses.pop(delete_index - 1)
            save_expenses(expenses)
            print(f"Removed: '{removed['description']}' (N{removed['amount']:.2f})")
        else:
            print("Invalid number selection.")
    except ValueError:
        print("Please enter a valid integer.")

# ================= MAIN MENU LOOP =================

def display_menu():
    print("\n--- MENU ---")
    tasks = [
        "Add Expense",
        "View All Expenses",
        "View Spending Summary",
        "Delete Expense",
        "Exit"
    ]
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    print("\033[35m=== MONEY TRACKER ===\033[0m")
    expenses = load_expenses()

    while True:
        display_menu()
        try:
            choice = int(input("\nChoose an option (1-5): "))
        except ValueError:
            print("Please enter a valid number (1-5)!")
            continue

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            view_summary(expenses)
        elif choice == 4:
            delete_expense(expenses)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select between 1 and 5.")

# if __name__ == "__main__":
main()