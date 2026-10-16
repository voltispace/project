import json
import os

FILE_NAME = "expenses.json"

# ================= DATA PERSISTENCE =================
def load_expenses():
    """Loads expenses from file if it exists, otherwise returns empty list."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    """Saves the current expenses list to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

# ================= MAIN APP =================
print("\033[35m=== MONEY TRACKER ===\033[0m\n")

# Load saved expenses at startup
expenses = load_expenses()

categories = ["Food", "Transport", "Utility", "Donations", "Miscellaneous"]

while True:
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

    try:
        user_choice = int(input("\nChoose an option (1-5): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # 1. ADD EXPENSE
    if user_choice == 1:
        print("\nSelect Category:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")
        
        try:
            cat_choice = int(input("Choose category number: "))
            if 1 <= cat_choice <= len(categories):
                selected_category = categories[cat_choice - 1]
            else:
                selected_category = "Miscellaneous"
        except ValueError:
            # print("Please enter a valid number!")
            # continue
            selected_category = "Miscellaneous"

        description = input("Enter description/product name: ").strip()
        while True:
            try:
                amount = float(input("Enter amount (N): "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please enter a valid amount.")

        # Save record
        new_expense = {
            "category": selected_category,
            "description": description,
            "amount": amount
        }
        expenses.append(new_expense)
        save_expenses(expenses)
        print(f"Added: N{amount:.2f} for '{description}' under [{selected_category}]")
        with open("money.json", "w", encoding='UTF-8') as file:
            json.dump(expenses, file, indent=4)
            
    # 2. VIEW ALL EXPENSES
    elif user_choice == 2:
        print("\n--- ALL EXPENSES ---")
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. [{exp['category']}] {exp['description']} - N{exp['amount']:.2f}")

    # 3. SUMMARY & CATEGORY TOTALS
    elif user_choice == 3:
        print("\n--- SPENDING SUMMARY ---")
        if not expenses:
            print("No expenses to calculate.")
        else:
            # Overall Total
            total_spent = sum(item["amount"] for item in expenses)
            print(f"Total Spending: \033[32mN{total_spent:.2f}\033[0m")
            
            # Totals by Category
            print("\nSpending by Category:")
            category_totals = {}
            for item in expenses:
                cat = item["category"]
                category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

            for cat, amount in category_totals.items():
                print(f"  - {cat}: N{amount:.2f}")

    # 4. DELETE AN EXPENSE
    elif user_choice == 4:
        print("\n--- DELETE EXPENSE ---")
        if not expenses:
            print("No expenses to delete.")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. [{exp['category']}] {exp['description']} - N{exp['amount']:.2f}")
            
            try:
                delete_index = int(input("\nEnter the number of the expense to delete: "))
                if 1 <= delete_index <= len(expenses):
                    removed = expenses.pop(delete_index - 1)
                    save_expenses(expenses)
                    print(f"Removed: '{removed['description']}' (N{removed['amount']:.2f})")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

    # 5. EXIT
    elif user_choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select between 1 and 5.")