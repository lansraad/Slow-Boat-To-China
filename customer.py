from tabulate import tabulate   # Tabulate is a library which is useful for presenting data in a table format
import os                       # OS is a utility module which lets me interface with the host operating system.

def clearScreen():              # The function 'clearScreen' clears the terminal to make the progam easier to read and use for the user.
    try:
        if(os.name == "nt"):        # If windows is the host operating system, run the 'cls' command to clear the console.
            os.system("cls")
        else:
            os.system("clear")      # If linux is the host operating system, run the 'clear' command to clear the.
    except: return False

def userPrompt():                                                                   # This function promts the user to validate their request
    return True if input("\nProceed? [Y/n] > ").upper() == "Y" else False          # If the user replies 'Y' or 'y', the function will return true, otherwise it will return false

class Customer:
    def __init__ (self, name, address):
        self.name = name
        self.address = address
        self.selectedItems = []
        self.remainingItems = 1
    
    def getMealDeal(self, mealDeals):
        oldRemainingItems, selected = self.remainingItems, False
        while not selected:
            self.remainingItems = oldRemainingItems
            selected = self.selectItems("Select a Meal Deal!", mealDeals ,["Option", "Meal Deal", "Items"])
        for deal in mealDeals:
            if(selected[0][0] in deal):
                self.remainingItems = int(deal[2])

    def getStarters(self, starters):
        oldRemainingItems, selected = self.remainingItems, False
        while not selected:
            self.remainingItems = oldRemainingItems
            selected = self.selectItems("Select your Starters!", starters, ["Option", "Starter", "Price (£)"])
        self.selectedItems.extend(selected)

    def getMeals(self, meals):
        oldRemainingItems, selected = self.remainingItems, False
        while not selected:
            self.remainingItems = oldRemainingItems
            selected = self.selectItems("Select your Meals!", meals, ["Option", "Meal", "Price (£)"])
        self.selectedItems.extend(selected)
    
    def selectItems(self, title, options, optionHeading):               # This function prompts the user to enter options from the menue, and returns them as a 2d array
        orderList, errorMsg, displayOptions = [], "", options

        for iter in range(len(options)):
            displayOptions[iter].insert(0, chr(65 + iter))

        while 0 in range(self.remainingItems+1):                                
            found = False
            clearScreen()
            print(title)
            if(len(errorMsg) > 0):                              # Display the error message is there is one
                print("⚠️  {} ⚠️\n\a".format(errorMsg))
            print(tabulate(displayOptions, optionHeading, tablefmt="psql", floatfmt=".2f"))           # Use tabulate to display the table
            if(self.remainingItems == 0):
                print("You have no items remaing.\n")
            elif(self.remainingItems == 1):
                print("You have 1 item remaining.\n")
            elif(self.remainingItems > 1):
                print("You have {} item(s) remaining.\n".format(self.remainingItems))                   # Tell the user how many items they can select
            for item in orderList:
                print("* {} (£{})".format(item[0], item[1]))                                   # Display the user's selection so they can see for any mistakes
            if self.remainingItems > 0:
                selection = input("\nSelect an option or type 'done' > ").upper()              # Let the user enter their selection
                if(selection == "DONE"):                                                               
                    if orderList:
                        return orderList if userPrompt() else ""
                    else:
                        errorMsg = "You must select something!"
                else:
                    for item in displayOptions:
                        if(selection in item):
                            found = True
                            errorMsg = ""
                            self.remainingItems -= 1
                            orderList.append([item[1], item[2]])
                    if(found == False):
                        errorMsg = "Invalid selection, try again!"
            else: 
                return orderList if userPrompt() else ""