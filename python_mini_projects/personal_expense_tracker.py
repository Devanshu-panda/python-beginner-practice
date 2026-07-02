"""
Personal Expense Tracker

A menu-based Python program to add, view, delete, and summarize expenses.
This project practices lists, dictionaries, loops, conditionals, and input validation.
"""
choice = 0
expenses = []

print("Welcome to Expense Tracker!")
input("Press Enter to begin...")
while choice != 8:
    print()
    print("1. Add expense\n2. View all expenses\n3. View total spent\n4. View expenses by category\n5. Show highest expense\n6. Delete an expense\n7. Category-wise summary\n8. Exit\n")
    try:
        choice = int(input("Choose an option from 1 to 8: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        print()
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid amount.")
        while True:
            print("Suggested categories: Food, Travel, Shopping, College, Medical, Entertainment, Electronics, Other")
            category = input("Enter category: ").strip().title()
            if not category:
                print("Please enter a valid category.")
                continue
            break
        description = input("Enter description: ").strip()
        if not description:
            description = "No description"
        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        print("Expense added successfully!")

    elif choice == 2:
        print()
        if expenses:
            print("All expenses:")
            print("---------------------------------------------------")
            for number, i in enumerate(expenses, start=1):
                print("Expense " + str(number))
                print(f"Amount: ₹{i['amount']:.2f}")
                print("Category: " + i["category"])
                print("Description: " + i["description"])
                print("---------------------------------------------------")
        else:
            print("No expenses found.")

    elif choice == 3:
        print()
        total_spent = 0
        if expenses:
            for i in expenses:
                total_spent += i["amount"]
            print(f"Total money spent is ₹{total_spent:.2f}")
        else:
            print("No expenses found.")

    elif choice == 4:
        print()
        if expenses:
            category_spent = 0
            found = False
            category = input("Enter category: ").strip().title()
            for i in expenses:
                if i["category"] == category:
                    if not found:
                        print("Expenses on " + category + ":")
                        print("---------------------------------------------------")
                    found = True
                    print(f"Amount: ₹{i['amount']:.2f}")
                    print("Category: " + i["category"])
                    print("Description: " + i["description"])
                    print("---------------------------------------------------")
                    category_spent += i["amount"]
            if found:
                print(f"Total money spent on {category} is ₹{category_spent:.2f}")
            else:
                print("No expenses found in this category.")
        else:
            print("No expenses found.")

    elif choice == 5:
        print()
        if expenses:
            highest_amount = expenses[0]["amount"]
            for i in expenses:
                if highest_amount < i["amount"]:
                    highest_amount = i["amount"]
            print("Highest expenses:")
            print("---------------------------------------------------")
            for i in expenses:
                if i["amount"] == highest_amount:
                    print(f"Amount: ₹{i['amount']:.2f}")
                    print("Category: " + i["category"])
                    print("Description: " + i["description"])
                    print("---------------------------------------------------")
        else:
            print("No expenses found.")

    elif choice == 6:
        print()
        if expenses:
            for number, i in enumerate(expenses, start=1):
                print("Expense " + str(number))
                print(f"Amount: ₹{i['amount']:.2f}")
                print("Category: " + i["category"])
                print("Description: " + i["description"])
                print("---------------------------------------------------")
            while True:
                try:
                    delete_expense = int(input("Enter expense number to delete: "))
                    if delete_expense < 1 or delete_expense > len(expenses):
                        print("Please enter a valid expense number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid expense number.")
            del expenses[delete_expense - 1]
            print(f"Expense {delete_expense} deleted successfully!")
        else:
            print("No expenses found.")

    elif choice == 7:
        print()
        if expenses:
            categories_summary = {}
            print("Category-wise summary:")
            print("---------------------------------------------------")
            for i in expenses:
                if i["category"] not in categories_summary:
                    categories_summary[i["category"]] = i["amount"]
                else:
                    categories_summary[i["category"]] += i["amount"]
            for category, amount in categories_summary.items():
                print(f"{category}: ₹{amount:.2f}")
        else:
            print("No expenses found.")

    elif choice == 8:
        print()
        print("Thank you for using Expense Tracker!")

    else:
        print()
        print("Please enter a choice between 1 and 8.")
