"""
TODO: 
* Add a function which allow orders to be viewed in the kitchen.
* Log all users to a database.
* Log all orders to a database.
* Add a management function to remove / search / modify orders and user data.
* Comment and refactor code for improved readability.
* Compile code and bake dependencies for use in the restaurant.
"""

from customer import Customer, userPrompt, clearScreen
from receipt import generateRecipt
from config import Config

def formatTitle(title):                         # This function returns the title, with formatting to match the horizontal length of the splash text.
    length = conf.get("splash").index('\n')     # Get the length of the first line by reading up to the newline indicator.
    length -= len(title) + 2                    
    output = ''
    for iter in range(int(length)):             # Loop for every character in the length of the first line.
        output += '-'                           # Add a minus sign to each empty space for pretty formatting.
        if iter == int(length / 2):             # Must be an integer, else the statement will never be satisfied.
            output += f" {title} "              # Add the title text in the centre.
    return output

def createOrder():
    clearScreen()
    print(conf.get("splash") + formatTitle("ORDERING SERVICE") + "\nWelcome to our restaurant, to begin ordering please enter your information below!\n")
    firstName = input("First name > ")
    lastName = input("Last name > ")
    postcode = input("Postcode > ")
    deliveryDistance = int(input("Distance from restaurant (in miles) > "))
    if deliveryDistance > 10:
        print("⚠️ We are unable to deliver to your location ⚠️")
    else:
        deliveryFee = getDeliveryFee(deliveryDistance)
        print("⚠️  You will incur a £{} delivery fee! ⚠️".format(deliveryFee))
        if not userPrompt():
            createOrder()

    customer = Customer(firstName + lastName, postcode)
    customer.getMealDeal(conf.get("mealDeals"))
    customer.getStarters(conf.get("starters"))  
    customer.getMeals(conf.get("meals"))

    generateRecipt(customer.selectedItems, conf.get("taxRate"), deliveryFee)

def main():
    clearScreen()
    print(conf.get("splash") + formatTitle("CLI") + "\nWelcome to our restaurant, what would you like to do today?")
    selection = input("""
    1 - Create an order
    2 - Manage current orders

Select an option >
    """)

    if selection == "1":
        createOrder()
    elif selection == "2":
        return                      #TODO
    else:
        main()

def getDeliveryFee(amount):
    for i in conf.get("deliveryFees"):
       if amount < i[0]:
           return i[1]
    return False

if __name__ == "__main__":
    conf = Config('./config.yml')
    main()