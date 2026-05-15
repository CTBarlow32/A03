'''
Carter Barlow IS 303
Order Processor
This Order Processor will total revenues, find largest order, filter orders over a dollar amount, and count orders by order status

Inputs:
- Number of orders
- dollar amount (int)
- order status (str)

Processes:
- collet data into a list of dictionaries
- sum total revenue (accumulator)
- validate integer is entered
- min/max: find most profitable order (min/max)
-filter: filter from most to list profitable, finished to unfinished (transform).

Outputs:
- show orders biggest to smallest, finished to unfinished
-show total revenue accumulative
-show total finished and unfinished orders

'''

#inputs
num_orders = int(input("Number of Orders Total? "))
orders = []

for i in range(num_orders):
    dollar_amount = input(f"Enter dollar amount for order number {i + 1}: $ ")
    order_status = input(f"Is order completed? ").lower()
    dollar_amount_wo_period = dollar_amount.replace(".", "")
    if dollar_amount_wo_period.isdigit():
        dollar_amount = float(dollar_amount)
        orders.append({"amount": dollar_amount, "status": order_status})
    else:
        print("You did not enter a digit.")


#sum total revenue
total_revenue = sum(order["amount"] for order in orders)
print(f"Total Revenue: ${total_revenue}") 

#find min/max
print(f"Highest Revenue Order:", max(order["amount"] for order in orders))

#Filter orders by dollar amount & order status
def sort_key(o):
    completed = o["status"].lower() in ("yes")
    return (0 if completed else 1, -o["amount"])

for i, order in enumerate(sorted(orders, key=sort_key)):
    print(f"{i+1}. Revenue: {order['amount']}, Order Processed: {order['status']}.")