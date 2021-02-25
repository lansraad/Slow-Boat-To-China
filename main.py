"""
TODO: 
* Add a function which allow orders to be viewed in the kitchen.
* Log all users to a database.
* Log all orders to a database.
* Add a management function to remove / search / modify orders and user data.
* Comment and refactor code for improved readability.
* Compile code and bake dependencies for use in the restaurant.
"""

from customer import Customer, userPrompt
from receipt import generateRecipt
from config import Config
import yaml

def getUserInfo():
    print(conf.get("splash")+"Welcome to our restaurant, to begin ordering please enter your information below!\n")
    firstName = input("First name > ")
    lastName = input("Last name > ")
    postcode = input("Postcode > ")
    deliveryDistance = int(input("Distance from restaurant (in miles) > "))
    if deliveryDistance > 10:
        print("⚠️ We are unable to deliver to your location ⚠️")
    else:
        deliveryFee = getDeliveryFee(deliveryDistance)
        print("⚠️  You will incur a £{} delivery fee! ⚠️".format(deliveryFee))
        if userPrompt():
            main(firstName + lastName, postcode, deliveryFee)
        else: getUserInfo()

def main(name, postcode, deliveryFee): 
    customer = Customer(name, postcode)
    customer.getMealDeal(conf.get("mealDeals"))
    customer.getStarters(conf.get("starters"))  
    customer.getMeals(conf.get("meals"))

    generateRecipt(customer.selectedItems, conf.get("taxRate"), deliveryFee)

def getDeliveryFee(amount):
    for i in conf.get("deliveryFees"):
       if amount < i[0]:
           return i[1]
    return False

if __name__ == "__main__":
    conf = Config('./config.yml')
    getUserInfo()