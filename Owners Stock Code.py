# Define the initial stock of each product
product_stock = {'coke': 5, 'pepsi': 10, 'sprite': 7}

# Define a function to check the current stock of a product
def check_stock(product_name):

    if product_name in product_stock:
        return product_stock[product_name]
    else:
        return 0

# Example usage


print("Current stock of Coke:", check_stock('coke'))
print("Current stock of Pepsi:", check_stock('pepsi'))
print("Current stock of Fanta:", check_stock('fanta'))
