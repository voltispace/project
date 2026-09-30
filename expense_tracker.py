print(f"\033[35mMONEY TRACKER\033[0m")
print("\n")

task = [
    "Add Expense ",
    "Delete Expense ",
    "View Summary "
    ]
for i, value in enumerate(task):
   print(f"{i + 1}. {value}")

user_choice = int(input('What do you want to do? Choose a task(1,2,3): \n'))

if user_choice == 1:
    category = [
        "Food",
        "Transport",
        "Utility",
        "Donations",
        "Miscellaneous",
        "Add category"
    ]
    for i, value in enumerate(category):
        print(f"{i + 1}. {value}")
    user_category = input("Choose category: \n").strip().lower()
    
    # def food():
    if user_category == "food":
        description = input("Product name: ")
        prdt_amount = int(input("Input amount:N"))
        print(f"You spent {prdt_amount} on {description}")

    elif user_category == "transport":
        description = input("Where are you going to? ")
        prdt_amount = int(input("Input amount:N"))
        print(f"You spent {prdt_amount} on transtport to {description}")

    elif user_category == "utility":
        description = input("What are you paying for? ")
        prdt_amount = int(input("Input amount:N"))
        print(f"You spent {prdt_amount} on {description}")
    else:
        print("Select a category for the expenses")
elif user_choice == 2:
    print("Delete Expense feature coming soon!")

elif user_choice == 3:
    print("View Summary feature coming soon!")

else:
    print("Invalid task choice!")



# food()
# summary= [
#    "Category:" + user_category,
#    "Product:" + prdt_description,
# #    "Amount:"  + {prdt_amount}
# ]
# print(summary)

   
# def del_expense():
# def expense_total():
# def view_summary():