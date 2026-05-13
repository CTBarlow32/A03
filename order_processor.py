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
- sum total revenue
- min/max: find most profitable order
-filter: filter from most to list profitable, finished to unfinished

Outputs:
- show orders biggest to smallest, finished to unfinished
-show total revenue accumulative
-show total finished and unfinished orders

'''

#inputs
num_orders = int(input("Number of Orders Total? "))
orders = []

for i in range(num_orders):
    dollar_amount = int(input(f"Enter dollar amount for order number {i + 1}: $ "))
    order_status = input(f"Is order completed? ")
    orders.append({"amount": dollar_amount, "status": order_status})

#sum total revenue
total_revenue = sum(order["amount"] for order in orders)
print(f"Total Revenue: ${total_revenue}") 

#find min/max
print(f"Highest Revenue Order:", max(order["amount"] for order in orders))

#Filter orders by dollar amount
for i, order in enumerate(orders):
    print(f"{i+1}. Revenue: {order['amount']}, Order Processed: {order['status']}.")