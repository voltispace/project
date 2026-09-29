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
user_category = input("Choose category: \n").lower()

if user_choice == 1 and user_category == "food":
    prdt_description= input("Product name: ")
    prdt_amount = int(input("Input amount:N"))

summary= [
   "Category:" + user_category,
   "Product:" + prdt_description,
#    "Amount:"  + {prdt_amount}
]
print(summary)
def add_expense():
def del_expense():
def expense_total():
def view_summary():