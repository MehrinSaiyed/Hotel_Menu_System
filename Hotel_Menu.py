menu = {"French Fries": 40, "Veg Manchurian" : 50, "Pizza":60, "Pasta": 65, "Burger" : 70, "Schezwan Fried Veg Noodles": 75,
        "Coffee": 80, "Cold coffee": 100}
print("Welcome to our Restaurant")
print("Menu is as follow :")
print("French Fries : 40\nVeg Manchurian : 50\nPizza :60\nPasta : 65\nBurger : 70\nSchezwan Fried Veg Noodles : 75\nCoffee : 80\nCold Coffee : 100")
item_1 = input("Enter the food item you want to order : ")
order_total = 0
if item_1 in menu :
    order_total += menu[item_1]
    print(f"{item_1} has been added to your order")
else :
    print(f"{item_1} is not available. Please order from the available menu")
another_order = input("Do you want other item ? (Yes/No)")
if another_order == "Yes" :
    item_2 = input("Enter another item you want to add : ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"{item_2} has been added to your order")
    else :
        print(f"Sorry {item_2} is not avaliable")
elif another_order == "No" :
    print("Hope you enjoyed the food.")
else :
    print("Kindly enter either 'Yes' or 'No' " )
print(f"Your total bill is {order_total} Rs")
print("Thanks for visiting.")