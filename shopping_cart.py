# shopping_cart.py
# from pprint import pprint

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
#pprint(products)

#
# INFO CAPTURE / INPUTS
#

total_price = 0
selected_ids = []  #empty list

while  True:
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    #> "DONE"
    if selected_id == "DONE":
        break
    else:
        selected_ids.append(selected_id)

        # print(selected_id)
        # print(type(selected_id))  #input is a string datatype
        # given selected identifier, find its matching product
        # matching_products = [p for p in products if str(p["id"]) == str(selected_id)]  #id is an integer while selected_id is a string, convert both to string to compare
        # matching_product = matching_products[0]  #select the first matching product
        # total_price = total_price + matching_product["price"]
        # print("SELECTED PRODUCT: " + str(matching_product["name"]) + " " + str(matching_product["price"]))
        #print(type(matching_product))

# print(selected_ids)
#
# INFO DISPLAY / OUTPUT
#
# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
print("---------------------------------")
print("NEW YORK MARKET")
print("WWW.NEW-YORK-MARKET.COM")
print("50 E 4TH ST, NEW YORK, NY 10009")
print("---------------------------------")

# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
now = datetime.datetime.now()
print("CHECKOUT AT: " + str(now))
print("---------------------------------")

# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
print("SELECTED PRODUCTS: ") 
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]  #id is an integer while selected_id is a string, convert both to string to compare
    matching_product = matching_products[0]  #select the first matching product
    price_usd = '${0:.2f}'.format(matching_product["price"]) #USD format
    total_price = total_price + matching_product["price"]
    print("... " + str(matching_product["name"]) + " " + str(price_usd))
print("---------------------------------")

# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
total_price_usd = '${0:.2f}'.format(total_price) 
print("SUBTOTAL: " + str(total_price_usd))

# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
tax = total_price * 0.0875
tax_usd = '${0:.2f}'.format(tax) 
print("TAX: " + str(tax_usd))

# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
grand_total = total_price + tax
grand_total_usd = '${0:.2f}'.format(grand_total) 
print("TOTAL: " + str(grand_total_usd))

# A friendly message thanking the customer and/or encouraging the customer to shop again
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
