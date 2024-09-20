# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

dog_type = str(input(print('Enter hot dog type: ')))
toppings = str(input(print('Any toppings?: ')))
TAX = .07

if dog_type == 'hot dog':
    price = 3.50
elif dog_type == 'chili dog':
    price = 4.50
else:
    print('invalid hot dog type')

if toppings == 'cheese':
    toppings_price = .50
elif toppings == 'peppers':
    toppings_price = .75
elif toppings == 'grilled peppers':
    toppings_price = 1
else:
    toppings_price = 0

sub_total = price + toppings_price
sales_tax = sub_total*TAX
total_cost = sub_total + sales_tax
print(f'Your sub total is: ${sub_total:.2f}')
print(f'sales tax: ${sales_tax:.2f}')
print(f'Total cost: ${total_cost:.2f}')