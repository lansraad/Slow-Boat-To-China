from tabulate import tabulate   # Tabulate is a library which is useful for presenting data in a table format

def generateRecipt(items, taxRate, deliveryFee):
    totalCost, receiptData = 0, []                                          # Store the receipt components in an 2d array
    for item in items:
        item[1] = "{:.2f}".format(float(item[1]))                           # Format the unit price to a string with two decimal places
        item.insert(0, 1)                                                   # Give the item an initial quantity of 1
        if not any(item[1] in sublist for sublist in receiptData):
            receiptData.append(item)                                        # Append the item to receiptData unless it is already there
        else:
            for sublist in receiptData:
                if item[1] in sublist:
                    receiptData[receiptData.index(sublist)][0] += 1         # If the item is already in receiptData, raise the quantity by 1
    
    for item in receiptData:
        itemPrice = int(item[0]) * float(item[2])                           # Calculate the total price of the item by multipling the unit price by quantity
        totalCost += itemPrice                                              # Add the cost to the total
        item.append("{:.2f}".format(itemPrice))                             # Format the subtotal price for the item to a string with two decimal places

    taxAmount = totalCost * taxRate                                         # Calculate the tax cost by multiplying the total cost by the tax rate

    receiptData[-1][2] = str(receiptData[-1][2]) + "\
        \n----------------\
        \nSubtotal\
        \nVat/Tax ({:.0%})\
        \nDelivery\
        \nTotal\
        ".format(taxRate)

    receiptData[-1][3] = str(receiptData[-1][3]) + "\
        \n----------------\
        \n{:.2f}\
        \n{:.2f}\
        \n{:.2f}\
        \n{}{:.2f}{}\
        ".format(totalCost, taxAmount, deliveryFee, "\33[92m", totalCost + taxAmount + deliveryFee, "\033[0m")

    print(tabulate(receiptData, ["Quantity","Description","Unit Price (£)","Subtotal (£)"], tablefmt="simple"))

if __name__ == "__main__": # Debug
    items = [['Crispy wonton', '3.36'], ['Sizzling beef with black bean sauce', '7.3'], ['Sizzling beef with black bean sauce', '7.3'], ['Pork with sweet and sour sauce', '6.40'], ['Chicken with cashew nuts', '4.60']]
    generateRecipt(items, 0.2, 5)   # Items, tax rate, delivery fee