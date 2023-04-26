# Define the available items and their prices
items = {'Coke': 1.5, 'Chips': 1.25, 'Candy': 0.75}
total_profits =0
stock = {'Coke': 5, 'Chips': 10, 'Candy': 15}

    
# Define the function to check the stock of each item
def check_stock(item):
    # Check if the selected item exists
    if item in items:
        # Check if the item is in stock
        if stock[item] > 0:
            # Return the remaining stock and a message that the item is in stock
            return stock[item], "Item is in stock and ready to be vended."
        else:
            # Return a message that the item is out of stock
            return 0, "Item is out of stock and cannot be vended."
    else:
        # Invalid item
        return 0, "Invalid item selection. Please choose another item."
# Define the function for selecting items and making payment
def vend(item, payment):
    # Check if the selected item exists
    if item in items:
        # Check if the payment is sufficient
        while payment < items[item]:
            # Ask the customer to insert more coins
            print("Insufficient payment. Please insert more coins.")
            additional_payment = float(input())
            payment += additional_payment
        # Calculate the change
        change = round(payment - items[item], 2)
        # Update the profits
        profits = round(items[item], 2)
        # Return the item and the change
        return item, change, profits
    else:
        # Invalid item
        return "Invalid item selection. Please choose another item."

# Main program
while True:
    # Display the available items and remaining stock
    print("Available items:")
    for item in items:
        remaining_stock, message = check_stock(item)
        print(item, "$" + str(items[item]), "Stock:", remaining_stock, message)
    # Prompt the customer to make a selection
    selection = input("Please select an item: ")
    # Prompt the customer to insert coins
    payment = float(input("Please insert coins: "))
    # Vend the item
    result = vend(selection, payment)
    # Check if the transaction was successful
    if type(result) == tuple:
        # Print the result
        print("Thank you for purchasing", result[0])
        print("Change:", result[1])
        # Update the total profits and stock level
        total_profits += result[2]
        stock[selection] = stock[selection] - 1
    else:
        # Print the error message
        print(result)
    # Prompt the customer to continue or cancel the transaction
    print("Press '1' to continue or '2' to cancel the transaction.")
    response = input()
    # Check the response
    if response == '2':
        # Return the remaining coins
        return_money = payment - items[selection]
        print("Transaction canceled. Returning coins:", return_money)
        break
