""" 
CP1404/CP5632 - Practical - Nicholas Bracher
shop calculator

Pseudocode:

amount_of_items = get user input 'Number of items: '

for item in range (amount_of_items)
    price = get user input 'Price of item: '
    total_price = total_price + price

if total_price > 100
    total_price = total_price * .9

print 'Total price for (amount_of_items) items is $(total_price)'
"""

amount_of_items = int(input('Number of items: '))
total_price = 0

while amount_of_items < 0:
    print('Invalid number of items!')
    amount_of_items = int(input('Number of items: '))

for item in range(amount_of_items):
    price = float(input('Price of item: $'))
    total_price = total_price + price

if total_price > 100:
    total_price = total_price * .9

print(f'Total price for {amount_of_items} items is ${total_price:.2f}')
