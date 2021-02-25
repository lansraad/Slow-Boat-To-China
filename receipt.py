from tabulate import tabulate   # Tabulate is a library which is useful for presenting data in a table format
from colours import *           #TODO add to config.yml

def generateRecipt(items, taxRate, deliveryFee):
    totalCost, receiptData = 0, []
    for item in items:
        item.insert(0, 1)
        if not any(item[1] in sublist for sublist in receiptData):
            receiptData.append(item)
        else:
            for sublist in receiptData:
                if item[1] in sublist:
                    receiptData[receiptData.index(sublist)][0] += 1
    
    for item in receiptData:
        itemPrice = int(item[0]) * float(item[2])
        totalCost += itemPrice
        item.append("{:.2f}".format(itemPrice))

    taxAmount = totalCost * taxRate

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
        \n{}\
        \n{}{:.2f}{}\
        ".format(totalCost, taxAmount, deliveryFee, GREEN, totalCost + taxAmount + deliveryFee, DEFAULT)

    print(tabulate(receiptData, ["Quantity","Description","Unit Price (£)","Subtotal (£)"], tablefmt="simple"))

if __name__ == "__main__": # Debug
    x = [['Crispy wonton', '3.36'], ['Sizzling beef with black bean sauce', '7.30'], ['Sizzling beef with black bean sauce', '7.30'], ['Pork with sweet and sour sauce', '6.40'], ['Chicken with cashew nuts', '4.60']]
    generateRecipt(x, 0.2, 5)