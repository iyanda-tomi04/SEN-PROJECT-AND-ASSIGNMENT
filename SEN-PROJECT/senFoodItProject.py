menu = {
    1: ("Burger", 1500),
    2: ("Pizza", 3000),
    3: ("Fried Rice", 2000),
    4: ("Chicken", 2500),
    5: ("Jollof rice", 2000),
    6: ("Taco", 1500),
    7: ("Meat pie", 800),
    8: ("Boba", 1000),
    9: ("Pounded yam and egusi", 2500),
    10: ("Soft Drink", 500),
    11: ("Bottled water", 300)
}
cart = []
print("  Welcome to Foodit. You can order from our menu. ")
while True:
    print("\nMENU:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - ₦{value[1]}")
    choice = int(input("\nEnter food number (0 to checkout): "))
    if choice == 0:
        break
    if choice in menu:
        qty = int(input("Enter quantity: "))
        item_name, price = menu[choice]
        cart.append((item_name, qty, price))
        print(f"{qty} {item_name}(s) added to cart.")
    else:
        print("Invalid choice")
# Checkout
print("\n ORDER SUMMARY")
total = 0
for item in cart:
    name, qty, price = item
    cost = qty * price
    total += cost
    print(f"{name} x{qty} = ₦{cost}")
print(f"\n Total Amount: ₦{total}")
print(" Thank you for ordering from Foodit !")