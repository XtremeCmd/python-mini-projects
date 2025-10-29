print("### Personal Expense Calculator ###")

name = input("Enter your name: ")
date = input("Enter today's date: ")

# Taking inputs
food = float(input("Enter your food expense: "))
travel = float(input("Enter your travel expense: "))
entertainment = float(input("Enter your entertainment expense: "))
misc = float(input("Enter your miscellaneous expense: "))

# Calculating Expense
total = food + travel + entertainment + misc
average = total / 4

# Results
print("\n-----------------------------------")
print(f"Name: {name}")
print(f"Date: {date}")
print(f"Total Expenses: ${total}")
print(f"Average Expense per Category: ${average}")
print("-----------------------------------")