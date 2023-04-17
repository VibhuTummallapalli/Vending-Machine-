# Define the initial stock and price of each product
product_stock = {'Coke': {'stock': 5, 'price': 1.50},
                 'Chips': {'stock': 10, 'price': 1.25},
                 'Candy': {'stock': 7, 'price': .75}}

# Define the initial total profit
total_profit = 0.0

# Define a function to check the current stock of a product
def check_stock(product_name):
    if product_name in product_stock:
        return product_stock[product_name]['stock']
    else:
        return 0

# Define a function to calculate the total profit
def calculate_profit(sales):
    global total_profit
    total_profit += sales

# Example usage
print("Current stock of Coke:", check_stock('Coke'))
print("Current stock of Chips:", check_stock('Chips'))
print("Current stock of Candy:", check_stock('Candy'))

# Make a sale
product_name = 'Coke'
quantity = 5
price = product_stock[product_name]['price'] * quantity
product_stock[product_name]['stock'] -= quantity
calculate_profit(price)

# Print updated stock and profit
print("Current stock of", product_name.capitalize() + ":", check_stock(product_name))
print("Total profit made:", total_profit)
