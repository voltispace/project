expenses = []
while True:
    task= [
        'add expense',
        'View expense',
        'Total expense',
        'Exit'
    ]
    for i, value in enumerate(task):
        print(f'{i+1}.{value}')
    choice = int(input("What do you wanna do, choose 1, 2, 3 from the list \n"))

    if choice==1:
        prdt =input("Enter product name: ")
        amount =float(input("enter amount N:"))
        expenses.append({
            "item": prdt,
            "amount": amount    
        })
        print(expenses)
       
        
    elif choice==2:
        for expense in expenses:
            print(expense["item"],  "-", expense["amount"] )
    elif choice==3:
        total =sum(expense["amount"] for expense in expenses )
        print("total:", total)
    elif choice==4:
        break