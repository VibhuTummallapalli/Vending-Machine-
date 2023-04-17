# Define the initial stock of each product
product_stock = {'Coke': 5, 'Chips': 10, 'Candy': 0}

# Define a function to check the current stock of a product
def check_stock(product_name):

    if product_name in product_stock:
        return product_stock[product_name]
    else:
        return 0

# Example usage


print("Current stock of Coke:", check_stock('Coke'))
print("Current stock of Chips:", check_stock('Chips'))
print("Current stock of Candy:", check_stock('Candy'))
