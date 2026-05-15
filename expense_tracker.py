'''
Carter Barlow IS303
This expense tracker will take inputs of category and expense, then print out total expenses, and the biggest expense.

Inputs:
- input category (string)
- input expense (int)

Processes:
- accumualte total expense (accumulater)
- validate integer is entered
- find biggest expense in all categories (min/max)
- make list of dictionaries of expenses and category.

Outputs:
- print log of total expenses
- print largest expense
'''

#find how many expenses
num_of_expenses = input("How many expenses do you have to input? ")
expenses = []

#make expenses/category into a list of dictionaries
for i in range(int(num_of_expenses)): 
    spending_category = input("What category are you spending in? ").lower()
    dollar_amount = input("How much was the expense? $ ")
    dollar_amount_wo_period = dollar_amount.replace(".", "")
    if dollar_amount_wo_period.isdigit():
        dollar_amount = float(dollar_amount)
        expenses.append({"amount": dollar_amount, "category": spending_category })
    else:
        print("You did not enter a digit.")

#sum total expense
total_expense = 0
for expense in expenses:
    total_expense += expense["amount"]
print(f"Total Expenses: ${total_expense}")

#find max expense
print(f"Highest single expense: $", max(expense["amount"] for expense in expenses))